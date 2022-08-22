from flask import Blueprint, jsonify, render_template, request
from .cafes_table import Cafe
import random
from .db import db
from .cafes_table import Cafe
from .cafes_forms import NewCafeForm, EditCafeForm

bp = Blueprint('cafes', __name__)


@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/random", methods=('GET',))
def random_cafe():
    # record_count = Cafe.query.count()
    # rand_result = random.randint(1,record_count)
    cafes = db.session.query(Cafe).all()
    rand_cafe = random.choice(cafes)
    # response = jsonify(cafe=jsonify(name=rand_cafe.name, map_url=rand_cafe.map_url)
    # return render_template('index.html', random_cafe=cafe, cafe_ct=record_count)
    return jsonify(cafe=rand_cafe.to_dict())

@bp.route('/all', methods=('GET',))
def all():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_list.append(cafe.to_dict())
    # should use list comprehension!
    # cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe_list)

## HTTP GET - Read Record
@bp.route('/search', methods=('GET',))
def search():
    cafe_list = []
    loc = request.args.get('loc')
    has_toilet = request.args.get('has_toilet')
    name = request.args.get('name')
    if loc:
        if has_toilet:
            cafe_location_w_toilet = db.session.query(Cafe).filter_by(location=loc, has_toilet=1).all()
            if cafe_location_w_toilet:
                for cafe in cafe_location_w_toilet:
                    cafe_list.append(cafe.to_dict())
            else:
                return render_template('index.html', term=f"No Record Found for {loc} with toilet.")
        else:
            cafe_location = db.session.query(Cafe).filter_by(location=loc).all()
            if cafe_location:
                for cafe in cafe_location:
                    cafe_list.append(cafe.to_dict())
            else:
                return render_template('index.html', term=f"No Record Found for {loc}")
    elif has_toilet:
        cafe_has_toilet = db.session.query(Cafe).filter_by(has_toilet=1).all()
        for cafe in cafe_has_toilet:
            cafe_list.append(cafe.to_dict())

    return jsonify(cafe_list)


## HTTP POST - Create Record
@bp.route('/add', methods=['POST'])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@bp.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
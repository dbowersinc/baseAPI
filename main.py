from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random", methods=('GET',))
def random_cafe():
    # record_count = Cafe.query.count()
    # rand_result = random.randint(1,record_count)
    cafes = db.session.query(Cafe).all()
    rand_cafe = random.choice(cafes)
    # response = jsonify(cafe=jsonify(name=rand_cafe.name, map_url=rand_cafe.map_url)
    # return render_template('index.html', random_cafe=cafe, cafe_ct=record_count)
    return jsonify(cafe=rand_cafe.to_dict())

@app.route('/all', methods=('GET',))
def all():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_list.append(cafe.to_dict())
    # should use list comprehension!
    # cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe_list)

## HTTP GET - Read Record
@app.route('/search', methods=('GET',))
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

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

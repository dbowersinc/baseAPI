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
    # response = jsonify({'cafe':{
    #     'name':rand_cafe.name,
    #     'img_url':rand_cafe.img_url,
    #     'map_url':rand_cafe.map_url,
    #     'location':rand_cafe.location,
    #     'seats':rand_cafe.seats,
    #     'has_toilet':rand_cafe.has_toilet,
    #     'can_take_calls':rand_cafe.can_take_calls,
    #     'coffee_price':rand_cafe.coffee_price,
    # }})
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
    search_for = request.args.get('test')
    return render_template('index.html', term=search_for)
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Cafe name is required.')])
    map_url = StringField('Name', validators=[DataRequired(message='Cafe name is required.')])
    img_url = StringField('Name', validators=[DataRequired(message='Cafe name is required.')])
    location = StringField('Name', validators=[DataRequired(message='Cafe name is required.')])
    seats = StringField('Name', validators=[DataRequired(message='Cafe name is required.')])
    has_toilet = BooleanField('Has toilet', validators=[DataRequired(message='Select if there is a toilet.')])
    has_wifi = BooleanField('Has WiFi', validators=[DataRequired(message='Select if there is a WiFi.')])
    has_sockets = BooleanField('Has sockets', validators=[DataRequired(message='Select if there are sockets.')])
    can_take_calls = BooleanField('Can take calls', validators=[DataRequired(message='Select if can take calls.')])
    coffee_price = StringField('Coffee Price', validators=[DataRequired(message='Coffee price is required.')])


class NewCafeForm(CafeForm):
    submit = SubmitField('Create New Cafe')

class EditCafeForm(CafeForm):
    submit = SubmitField('Save Changes')


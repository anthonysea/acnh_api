from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()


class Critter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    image_url = db.Column(db.String(512))
    price = db.Column(db.Integer)
    location = db.Column(db.String(128))
    shadow_size = db.Column(db.String(4))
    timeday = db.Column(db.String(64))
    seasonality_n = db.Column(db.String(12))
    seasonality_s = db.Column(db.String(12))
    critter_type = db.Column(db.String(4))


class CritterSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Critter
    
    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    location = ma.auto_field()
    shadow_size = ma.auto_field()
    timeday = ma.auto_field()
    seasonality_n = fields.Function(lambda obj: [1 if '1' == i else 0 for i in obj.seasonality_n])
    seasonality_s = fields.Function(lambda obj: [1 if '1' == i else 0 for i in obj.seasonality_s])
    critter_type = ma.auto_field()
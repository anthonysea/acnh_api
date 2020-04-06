from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

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


class CritterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Critter
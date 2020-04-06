import connexion, scrapy, os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from models import db, ma

def create_app():
    connexion_app = connexion.App(__name__, specification_dir='./')
    # Connexion stores the Flask app reference in .app member
    flask_app = connexion_app.app

    basedir = os.path.abspath(os.path.dirname(__file__))
    print('basedir: ', basedir)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    print(flask_app.config['SQLALCHEMY_DATABASE_URI'])
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_ECHO'] = True
    CORS(flask_app)

    # Use the api.yml for REST API definition
    connexion_app.add_api("api.yml")

    db.init_app(flask_app)
    ma.init_app(flask_app)

    return flask_app

if __name__ == '__main__':
    app = create_app()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 



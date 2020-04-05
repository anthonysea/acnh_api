import connexion, scrapy, os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from scrapy.crawler import CrawlerProcess

from acnh_scraper.spiders.critter_spider import CritterSpider
from models import db, ma

def create_app():
    app = connexion.App(__name__, specification_dir='./')
    # Connexion stores the Flask app reference in .app member
    flask_app = app.app

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_ECHO'] = True
    CORS(flask_app)
    app.add_api("api.yml")

    db.init_app(flask_app)
    ma.init_app(flask_app)

    return flask_app

def get_data():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'critters.json'
    })

    process.crawl(CritterSpider)
    process.start()

if __name__ == '__main__':
    json_files = ['critters.json']

    # scrape and create json data files
    for file in json_files:
        if not os.path.isfile(file):
            get_data()

    app = create_app()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 



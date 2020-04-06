import os
from app import create_app

from models import db, Critter, CritterSchema
from scrapy.crawler import CrawlerProcess
from acnh_scraper.spiders.critter_spider import CritterSpider


def get_data():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'critters.json'
    })

    process.crawl(CritterSpider)
    process.start()

### Start of DB creation
if os.path.exists('test.db'):
    os.remove('test.db')

app = create_app()
with app.app_context():
    db.create_all()
    db.session.commit()

    # Testing
    # c1 = Critter(name='fish1', price=100, location='river', shadow_size='1')
    # db.session.add(c1)
    # db.session.commit()

    critters = Critter.query.all()
    critter_schema = CritterSchema(many=True)
    print(critter_schema.dump(critters))


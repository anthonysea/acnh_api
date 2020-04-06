import os, json
from app import create_app

from models import db, Critter, CritterSchema
from scrapy.crawler import CrawlerProcess
from acnh_scraper.spiders.critter_spider import CritterSpider


def create_json():
    '''Calls the crawler process and scrapes data using the CritterSpider. Creates critters.json'''
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'critters.json'
    })

    process.crawl(CritterSpider)
    process.start()


def load_json_data():
    try:
        with open('critters.json') as f:
            data = json.load(f)
            return data
    except IOError as err:
        print("critters.json does not exist")


def main():
    if not os.path.isfile('critters.json'):
        create_json()
        
    data = load_json_data()
    ### Start of DB creation
    if os.path.exists('test.db'):
        os.remove('test.db')

    app = create_app()
    with app.app_context():
        db.create_all()
        print(data[0])
        # TODO: insert all json entries into database
        for critter in data:
            shadow_size = critter['shadow_size'] if 'shadow_size' in critter else None
            temp_critter = Critter(
                name=critter['name'],
                image_url=critter['image_url'],
                price=critter['price'],
                location=critter['location'],
                shadow_size=shadow_size,
                timeday=critter['timeday'],
                seasonality_n=''.join([str(x) for x in critter['seasonality_n']]),
                seasonality_s=''.join([str(x) for x in critter['seasonality_s']]),
                critter_type=critter['type']
            )
            db.session.add(temp_critter)

        db.session.commit()

        # Testing
        # c1 = Critter(name='fish1', price=100, location='river', shadow_size='1')
        # db.session.add(c1)
        # db.session.commit()

        critters = Critter.query.all()
        critter_schema = CritterSchema(many=True)
        print(critter_schema.dump(critters))

if __name__ == '__main__':
    main()
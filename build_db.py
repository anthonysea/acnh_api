import os, json
from app import create_app

from models import (
    db,
    Critter, CritterSchema,
    Fossil, FossilSchema
)
from scrapy.crawler import CrawlerProcess
from acnh_scraper.spiders.critter_spider import CritterSpider
from acnh_scraper.spiders.fossil_spider import FossilSpider


def create_json():
    """Calls the crawler process and scrapes data using the CritterSpider. Creates critters.json"""
    process = CrawlerProcess()

    process.crawl(CritterSpider)
    process.crawl(FossilSpider)
    process.start()


def load_json_data(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
            return data
    except IOError as err:
        print(f"{filename} does not exist")
        return -1


def main():
    # Create json files if do not exist
    json_files = ["critters.json", "fossils.json", "villagers.json"]
    if not all(map(os.path.isfile, json_files)):
        create_json()
    
    ### Start of DB creation
    if os.path.exists("test.db"):
        os.remove("test.db")

    app = create_app()
    with app.app_context():
        db.create_all()

        for filename in json_files:
            data = load_json_data(filename)
            if data is -1:
                print(f"Failed to load {filename}")
                return

            # insert all json entries into database
            if filename == "critters.json":
                for critter in data:
                    shadow_size = critter["shadow_size"] if "shadow_size" in critter else None
                    temp_critter = Critter(
                        name=critter["name"],
                        image_url=critter["image_url"],
                        price=critter["price"],
                        location=critter["location"],
                        shadow_size=shadow_size,
                        timeday=critter["timeday"],
                        seasonality_n="".join([str(x) for x in critter["seasonality_n"]]),
                        seasonality_s="".join([str(x) for x in critter["seasonality_s"]]),
                        critter_type=critter["critter_type"]
                    )
                    db.session.add(temp_critter)
                db.session.commit()
            
            elif filename == "fossils.json":
                for fossil in data:
                    temp_fossil = Fossil(
                        name=fossil["name"],
                        image_url=fossil["image_url"],
                        price=fossil["price"],
                        fossil_type=fossil["fossil_type"],
                        group=fossil["group"]
                    )
                    db.session.add(temp_fossil)
                db.session.commit()

        # debugging
        # critters = Critter.query.all()
        # critter_schema = CritterSchema(many=True)
        # print(critter_schema.dump(critters))

        fossils = Fossil.query.all()
        fossil_schema = FossilSchema(many=True)
        print(fossil_schema.dump(fossils))

if __name__ == "__main__":
    main()
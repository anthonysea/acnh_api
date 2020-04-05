import connexion, scrapy, os

from flask import Flask, render_template
from flask_cors import CORS
from scrapy.crawler import CrawlerProcess
from acnh_scraper.spiders.critter_spider import CritterSpider


app = connexion.App(__name__, specification_dir='./')
CORS(app.app)
app.add_api("api.yml")

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

    
    app.run(debug=True, host='0.0.0.0', port=5000) 



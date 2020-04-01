import scrapy

class FishSpider(scrapy.Spider):
    name = "fish"
    start_urls = [
        "https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)",
    ]

    def parse(self, response):
        fish_links = response.css("table.roundy.sortable tr td:first-child a::attr(href)")
        yield from response.follow_all(fish_links, self.parse_fish)

    def parse_fish(self, response):
        # There are two types of stylings that the page uses for their data cards, have to check if a class exists on a element to decide

        if (response.css("aside.portable-infobox").get() is not None):
            if response.css("div.pi-item[data-source='location']").get() is None:
                yield {
                    "name": response.css("h2.pi-item[data-source='name']::text").get(),
                    "location": response.css("div.pi-smart-data-value[data-source='location'] ::text").getall(),
                    "price": int(('').join(response.css("div.pi-smart-data-value[data-source='price']::text").get().strip().split(','))),
                    "shadow_size": ('/').join([x.strip() for x in response.css("div.pi-smart-data-value[data-source='shadow']::text").getall() if x is not ' ']),
                    "seasonality_n": ('').join(response.css("div.pi-smart-data-value[data-source='timeyear'] ::text").getall()),
                    "seasonality_s": ('').join(response.css("div.pi-smart-data-value[data-source='timeyear'] ::text").getall()),
                    "time_of_day": response.css("div.pi-smart-data-value[data-source='timeday']::text").get(),
                    "rarity": response.css("div.pi-item[data-source='rarity'] > div::text").get(),
                }
            else: 
                yield {
                    "name": response.css("h2.pi-item[data-source='name']::text").get(),
                    "location": response.css("div.pi-item[data-source='location'] > div > a::text").getall(),
                    # int(('').join(response.css("div.pi-item[data-source='price-nook'] > div::text").get().strip().split(',')))
                    "price": int(('').join(response.css("div.pi-item[data-source='price-nook'] > div::text").get().strip().split(','))),
                    "shadow_size": response.css("div.pi-item[data-source='shadow'] > div::text").get(),
                    # *::text selector selects the text of the current tag and all it's children
                    "seasonality_n": ('').join(response.css("div.pi-item[data-source='timeyear-north'] > div *::text").getall()),
                    "seasonality_s": ('').join(response.css("div.pi-item[data-source='timeyear-south'] > div *::text").getall()),
                    "time_of_day": response.css("div.pi-item[data-source='timeday'] > div::text").get(),
                    "rarity": response.css("div.pi-item[data-source='rarity'] > div::text").get(),
                }
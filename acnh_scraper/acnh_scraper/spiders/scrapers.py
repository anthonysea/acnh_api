import scrapy

class FishSpider(scrapy.Spider):
    # Currently does get sea horse or frog page or great white shark
    name = "fish"
    start_urls = [
        "https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)",
    ]


    def parse(self, response):
        fish_tables = response.css("table.roundy.sortable")
        fishes = []

        for hemisphere in fish_tables:
            rows = hemisphere.css("tr")
            for item in rows[1:]:
                fish = {}
                fish['name'] = item.css("td:first-child > a::text").get()
                fish['image_url'] = item.css("td:nth-child(2) > a::attr(href)").get()
                fish['price'] = int(item.css("td:nth-child(3)::text").get().strip())
                fish['location'] = item.css("td:nth-child(4)::text").get().strip()
                fish['shadow_size'] = item.css("td:nth-child(5)::text").get().strip()
                fish['timeday'] = item.css("td:nth-child(6) small::text").get()

                fish['seasonality_n'] = [1 if month.strip() == '\u2713' else 0 for month in item.css("td:nth-child(n+7)::text").getall() ]
                fishes.append(fish)
        
        print(fishes)
        return fishes

        

    def old_parse(self, response):
        fish_links = response.css("table.roundy.sortable tr td:first-child a::attr(href)")
        yield from response.follow_all(fish_links, self.parse_fish)
        # Hard code data for great white shark and sea horse as there is no data on them currently
        yield {
            "name": "Great white shark",
            "location": ["Sea"],
            "price": 15000,
            "shadow_size": "Huge (with fin)",
            "seasonality_n": "June to September",
            "seasonality_s": "June to September",
            "time_of_day": "4 PM - 9 AM",
            "rarity": "",
        }

        yield {
            "name": "Sea horse",
            "location": ["Sea"],
            "price": 1100,
            "shadow_size": "Tiny",
            "seasonality_n": "April to November",
            "seasonality_s": "April to November",
            "time_of_day": "All day",
            "rarity": "",
        }

    def parse_fish(self, response):

        # There are two types of stylings that the page uses for their data cards, have to check if a class exists on a element to decide
        if (response.css("aside.portable-infobox").get() is not None):
            if response.css("div.pi-item[data-source='location']").get() is None:
                yield {
                    "name": response.css("h2.pi-item[data-source='name']::text").get(),
                    "location": response.css("div.pi-smart-data-value[data-source='location'] a::text").getall(),
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
        else:
            # Reached disambiguation page for frogs
            frog_link = response.css("ul > li:nth-child(2) > a[title='Frog (fish)']::attr(href)").get()
            if frog_link is not None:
                yield response.follow(frog_link, self.parse_fish)

        
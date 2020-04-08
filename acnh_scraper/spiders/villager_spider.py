import scrapy
MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
class VillagerSpider(scrapy.Spider):
    name = "villager"
    custom_settings = {
        "FEED_FORMAT": "json",
        "FEED_URI": "villagers.json",
    }
    start_urls = [
        "https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)"
    ]

    def parse(self, response):
        villagers = []
        table = response.css("table.roundy.sortable")
        rows = table.css("tr")[1:]

        for row in rows:
            villager = {}
            villager["name"] = row.css("td:first-child > b > a::text").get()
            villager["image_url"] = row.css("td:nth-child(2) > a::attr(href)").get()
            villager["personality"] = row.css("td:nth-child(3) > a::text").get().split()[1]
            villager["species"] = row.css("td:nth-child(4) > a::text").get()

            birthdate_month, birthdate_day = row.css("td:nth-child(5)::text").get().strip().split()
            birthdate_month = MONTHS[birthdate_month]
            birthdate_day = int(birthdate_day)
            villager["birthdate_month"] = birthdate_month
            villager["birthdate_day"] = birthdate_day
            villager["catchphrase"] = row.css("td:nth-child(6) > i::text").get()

            villagers.append(villager)

        return villagers


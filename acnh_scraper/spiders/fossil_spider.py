import scrapy

class FossilSpider(scrapy.Spider):
    name = "fossil"
    start_urls = [
        "https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)"
    ]

    def parse(self, response):
        fossils = []

        sa_fossil_table, mp_fossil_table = response.css("table.sortable")

        # Get the rows for each table
        # First row is the heading row so leave it out
        sa_rows = sa_fossil_table.css("tr")[1:] 
        mp_rows = mp_fossil_table.css("tr")[1:]

        # Build stand-alone fossil and append to fossil list
        for row in sa_rows:
            fossil = {}
            fossil["name"] = row.css("td:first-child > a::text").get()
            fossil["image_url"] = row.css("td:nth-child(2) > a::attr(href)").get()
            fossil["price"] = int("".join(row.css("td:nth-child(3)::text").get().strip().split()[0].split(",")))
            fossil["type"] = "stand-alone"
            fossil["group"] = None

            fossils.append(fossil)

        # Build multi-part fossils and append to fossil list
        current_fossil_group = ''
        for row in mp_rows:
            fossil = {}

            # Check if current row is a new fossil group
            if row.css("th > a::text").get():
                current_fossil_group = row.css("th > a::text").get()
                continue

            fossil["name"] = row.css("td:first-child > a::text").get()
            fossil["image_url"] = row.css("td:nth-child(2) > a::attr(href)").get()
            fossil["price"] = int("".join(row.css("td:nth-child(3)::text").get().strip().split()[0].split(",")))
            fossil["type"] = "multi-part"
            fossil["group"] = current_fossil_group

            fossils.append(fossil)

        return fossils


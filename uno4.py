import metasrcape_gen as mg
import json

with open('buyNow.json') as json_file:
    list = json.load(json_file)

mg.meta_scrape(3200,4000,list,"lst5.json","dict5.json")
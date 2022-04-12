import metasrcape_gen as mg
import json

with open('buyNow.json') as json_file:
    list = json.load(json_file)

mg.meta_scrape(4800,5600,list,"lst7.json","dict7.json")
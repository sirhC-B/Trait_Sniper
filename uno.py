import metasrcape_gen as mg
import json

with open('buyNow.json') as json_file:
    list = json.load(json_file)

mg.meta_scrape(0,800,list,"lst1.json","dict1.json")
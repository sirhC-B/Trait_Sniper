import metasrcape_gen as mg
import json

with open('buyNow.json') as json_file:
    list = json.load(json_file)

mg.meta_scrape(800,1600,list,"lst2.json","dict2.json")
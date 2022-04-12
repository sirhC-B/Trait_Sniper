import metasrcape_gen as mg
import json

with open('buyNow.json') as json_file:
    list = json.load(json_file)

mg.meta_scrape(2400,3200,list,"lst4.json","dict4.json")
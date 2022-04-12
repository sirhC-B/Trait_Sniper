import requests
from bs4 import BeautifulSoup
import json

text = open('text.txt', 'r')

content = text.read()

content = content.replace("EnigmaV4 ", "")

content = content.replace("opensea","")
content = content.replace(" ","")
content = content.split('\n')
print(content)
list = []
for i in content:
    if i.startswith('#'):
        list.append(i)

list1 = []
for i in list:
    if not int(i[1:]) in list1:
        list1.append(int(i[1:]))

print(list1)
print(len(list1))

with open('buyNow.json', 'w') as f:
    json.dump(list1, f)



with open('buyNow.json') as json_file:
    buyNow = json.load(json_file)

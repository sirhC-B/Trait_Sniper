import requests
import json
import webbrowser


def meta_scrape(START, END, LIST, METANAME='metadata.json', DICTNAME='traitDict.json'):

    list = LIST
    url = "https://enigmav4.s3.amazonaws.com/"
    osurl = "https://opensea.io/assets/0x0027fcb9c3605f30bfadaa32a63d92dc62a94360/"

    meta = {}
    traitDict = {"Expert": [], "Apprentice": [], "Novice": [],"Partner": []}

    for i in range(START, END):
        r = requests.get(url + str(i))

        attributes = r.json()['attributes']
        meta[i] = attributes

        if "Expert" in str(attributes):
            print("Expert:")
            print(osurl + str(i))
            traitDict["Expert"].append(i)
            if i in list:
                print("BUY NOW HIT!")
                webbrowser.open(osurl + str(i))

        elif "Apprentice" in str(attributes):
            print("Apprentice:")
            print(print(osurl + str(i)))
            traitDict["Apprentice"].append(i)
            if i in list:
                print("BUY NOW HIT!")
                webbrowser.open(osurl + str(i))

        elif "Novice" in str(attributes):
            print("Novice:")
            print(print(osurl + str(i)))
            traitDict["Novice"].append(i)
            if i in list:
                print("BUY NOW HIT!")

        elif not ("Worker" or "Novice" or "Apprentice" or "Expert") in str(attributes) and r.json()['attributes']:
            print("LLAMA,JIRA:")
            print(print(osurl + str(i)))
            traitDict["Partner"].append(i)
            if i in list:
                print("BUY NOW HIT! TURE")
                webbrowser.open(osurl + str(i))

        else:
            print(str(i) + " - Statuscode: " + str(r.status_code))

    with open(METANAME, 'w') as f:
        json.dump(meta, f)
    with open(DICTNAME, 'w') as f:
        json.dump(traitDict, f)


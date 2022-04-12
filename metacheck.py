import requests
import sendingMail
import time
import metascrape

url1 = "https://enigmaminer.s3.amazonaws.com/"
url = "https://enigmav4.s3.amazonaws.com/"

found = False
round = 0

while found == False:
    for i in range(0, 5550, 250):
        r = requests.get(url + str(i))
        attributes = r.json()['attributes']

        if attributes:
            print("FOUND!!!")
            print(r.json()['name'])
            print(attributes)
            sendingMail.sending_mail(["chris_boesener@gmx.net","maxi.schelske@web.de"], ("Metadaten gefunden bei token" + str(i) + "!"))
            found = True
        else:
            print(str(i) + " nothing there... (" + str(r.status_code) + ")")
            print(r.text[0:500])
    if found == False:
        round += 1
        print("Round: " + str(round))
        time.sleep(60)
    if found == True:
        metascrape.meta_scrape(0,5555)

print("done")

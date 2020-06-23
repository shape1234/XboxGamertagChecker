import time
import itertools
import requests
import random
numbers = '0123456789'
alnum = 'abcdefghijklmnopqrstuvwxyz' + numbers
letters = 'abcdefghijklmnopqrstuvwxyz'
#You can specify what you want in. EX: len2 = itertools.product(letters, letters, letters, letters) will return every 4 letter word
len2 = itertools.product(letters, letters, letters, letters)
list1 = [''.join(p) for p in itertools.chain(len2)]
url = 'https://gamertag.xboxlive.com/gamertags/reserve'
#Cookies for the Request
header = {"Accept": "application/json, text/plain, */*", 
"Content-Type":"application/json",
#Change this value to your accounts Specific still dont know how to get these automatically
"authorization":"",
"x-xbl-contract-version":"1",
"MS-CV":""}
for x in list1:
    payload = {"gamertag": x ,"reservationId":"2535450194591598","targetGamertagFields":"gamertag"}
    response = requests.post(url, json=payload, headers=header)
    print(response.text)
    if response.json().get("description") == "Gamertag is unacceptable":
        continue
    if response.status_code == 429:
        print(response.json())
        # Wait 30 minutes
        time.sleep(30*60)
    classicGamertag = response.json().get("classicGamertag")
    print("Status code: " + str(response.status_code))
    print("Testing Gamertag: " + x)
    print("Xbox Generated Gamertag: " + classicGamertag)
    if classicGamertag == x:
        print("Added: " + str(x))
        with open('good.txt', 'w') as file:
            file.write(x)
        print("Found valid Gamertag: {}".format(x))
    print("Waiting: {}\n".format(20))
    time.sleep(20)

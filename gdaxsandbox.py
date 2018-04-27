#Trying to get output from the GDAX REST API

import requests
import json

#get a response from GDAX
prods = requests.get('https://api-public.sandbox.gdax.com/products')

#format response from json to a list of dicts
prodsdata = json.loads(prods.text)

for i in range(0, len(prodsdata)):
    print("Entry {0}: {1}".format(i, prodsdata[i]["id"]))

#Trying to get output from the GDAX REST API

import requests
import json

#get a response from GDAX
prods = requests.get('https://api-public.sandbox.gdax.com/products')

#format response from json to a list of dicts
prodsdata = json.loads(prods.text)

#for i in range(0, len(prodsdata)):
    #print("Entry {0}: {1}".format(i, prodsdata[i]["id"]))

btcusd = prodsdata[0]

with open('gdaxproducts.txt', 'w') as f:
    f.write("The products offered from the GDAX REST API:\n\n\n")
    f.write("The GDAX REST API offers conversion rates between the following currencies:\n")
    for i in range(0, len(prodsdata)):
        f.write("{0}\n".format(prodsdata[i]["id"]))
    f.write("\n")

    f.write("For each of these currency pairings, the following attributes are available:\n")
    for i in prodsdata[0]:
        f.write("{0}\n".format(i))
        

"""Working module for GDAX Rest API"""

import json
import requests
import datetime

base_URL = 'https://api.gdax.com/products/'
    
prodlist = ["BTC-USD", "BTC-GBP", "BTC-EUR",
            "ETH-BTC", "ETH-USD", "LTC-BTC", "LTC-USD", "LTC-EUR", "ETH-EUR"]

def getprods():
    """getprods() get the list of products along with associated stats. 
    Returns a dictionary"""
    products = requests.get(base_URL)

    if products.status_code == 200:
        productsdata = json.loads(products.text)
        return productsdata
    else:
        raise Exception('Bad response from GDAX.')


def getticker(product_id):
    """getticker(product_id) get the ticker readout of product_id in dict form"""
    product_id = product_id.upper()

    if product_id in prodlist:
        #Form URL
        requrl = base_URL + product_id + '/ticker'

        #get a response from GDAX
        ticker = requests.get(requrl)

    if ticker.status_code == 200:
        tickerdata = json.loads(ticker.text)
        return tickerdata
    else:
        raise Exception('Bad response from GDAX.')


def gethist(product_id, starttime, endtime, resolution):
    """gethist(product_id, starttime, endtime, resolution) 

    starttime and endtime MUST be in ISO 8601 format
    
    get historical pricing on product_id from starttime to endtime with resolution
    this output may be large. prepare."""

    

    #if starttime - endtime / resolution < 200
        #__histhelper()
    #else 
        #break the elapsed time into 200 bit requests
        #for requests
            #__histhelper
            #append this request to the previous one
            #wait 1/3 sec to avoid getting blacklisted
    
    #return a dict. maybe enforce writing to a file


def __histhelper(product_id, starttime, endtime, resolution):
    """__histhelper(product_id, starttime, endtime, resolution)

    helper function for gethist that actually gets a history.
    returns a dict."""

    reqparams = {'start' : starttime, #Starttime in ISO 8601
                 'end' : endtime, #endtime in ISO 8601
                 'granularity' : resolution} #resolution in seconds

    #get history. must be less than 200 data points, or the request will fail
    hist = requests.get(base_URL + product_id + '/candles', reqparams)

    #if response == 200, return history
    if hist.status_code == 200:
        histdata = json.loads(hist.text)
        return histdata
    else:
        raise Exception('Bad response from GDAX.')
    
    #else raise exception or notify user 
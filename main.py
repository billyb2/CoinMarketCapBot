import coinmarketcap as cmc
import time
import json
import threading

currencies = {
        "time" : time.time(),
        "BAT" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 0.19
        },
        "ETH" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 202.37
        },
        "DASH" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 73.14
        },
        "DOGE" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 0.002
        },
        "STEEM" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 0.19
        },    
        "XMR" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 55.4547276051
        },
        "ETN" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 0.002
        },
        "SBD" : {
            "price" : 1
        },
        "GRC" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : 0.002
        }

}

def logPriceData():
    historicalData = open("data.txt", "a")
    historicalData.write(json.dumps(currencies) + "\n")
    historicalData.close()
    print(json.dumps(currencies))
    threading.Timer(60, logPriceData).start()


logPriceData()


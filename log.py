import coinmarketcap as cmc
import time
import json
import threading
import logging

#Whether the thread should be killed or not
#Set by default to false 
kill = False
#The number of lines added 
numberOfLines = 0

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

def stopLogging():
    global kill
    kill = True


def logPriceData():
    global kill
    global numberOfLines
    if kill == False:
        if numberOfLines < 43800:
            numberOfLines += 1
            historicalData = open("data.txt", "a")
            historicalData.write(json.dumps(currencies) + "\n")
            historicalData.close()
            logging.debug(json.dumps(currencies))
            threading.Timer(1, logPriceData).start()
        else:
            print("Reached maximum number of lines")
    else:
        print("Done collecting data")
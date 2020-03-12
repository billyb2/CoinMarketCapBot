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

def stopLogging():
    global kill
    kill = True


def logPriceData():

currencies = {
        "time" : time.time(),
        "BAT" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('BAT', 1)
        },
        "ETH" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('ETH', 1)
        },
        "DASH" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('DASH', 1)
        },
        "DOGE" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('DOGE', 1)
        },
        "STEEM" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('STEEM', 1)
        },    
        "XMR" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('XMR', 1)
        },
        "ETN" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('ETN', 1)
        },
        "SBD" : {
            "price" : cmc.convert('SBD', 1)
        },
        "GRC" : {
            #Remember to actually change the price, I'm just keeping it like this to save credits
            #"price" : cmc.convert('XMR', 1),
            "price" : cmc.convert('GRC', 1)
        }

}


    global kill
    global numberOfLines
    if kill == False:
        if numberOfLines < 43800:
            numberOfLines += 1
            historicalData = open("data.txt", "a")
            historicalData.write(json.dumps(currencies) + "\n")
            historicalData.close()
            logging.debug(json.dumps(currencies))
            threading.Timer(300, logPriceData).start()
        else:
            print("Reached maximum number of lines")
    else:
        print("Done collecting data")
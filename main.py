from log import logPriceData, stopLogging
import time
import json

#Start logging price data every minute or so
logPriceData()

latestLine = None

data = []
sum = 0

with open('data.txt') as f:
    for line in f:
        data.append(json.loads(line))


sizeOfData = len(data)

for data in data:
    sum += data['BAT']['price']

print(sum)
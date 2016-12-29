#!/anaconda/bin/python
from __future__ import print_function
import datetime
import requests
import json
import pprint
import sys,os
'''
- script to read data from Twitch for a list a channels'id
- save data into a id.csv file
'''

today = str(datetime.datetime.now().strftime('%Y-%m-%d'))
#insert your twitch credential 
headers = {'Client-ID': ''}

myUrl = 'https://api.twitch.tv/kraken/games/top?limit=100'
#insert channels' ID
channelsId=[369579, 492930, 21779, 29595, 488552, 491599, 19180, 280721,417752]
#channelsId=[19180]
allChan = requests.get(myUrl,headers = headers)  
allList = allChan.json()
#pprint.pprint(allList)
gameList = {}
for chan in channelsId :
    counter=0
    for game in allList['top'] :
        counter = counter + 1
        if (chan == game['game']['_id']):
            currentgame =[]
            currentgame.append(game['game']['name'].encode('utf-8'))
            currentgame.append(game['viewers'])
            currentgame.append(game['game']['popularity'])
            currentgame.append(game['channels'])
            currentgame.append(counter)
            gameList[game['game']['_id']] = currentgame
            break

for key in gameList:
    out = '/mydir/' + str(key) + '.csv'
    fileOut = open(out,"a")
    sys.stdout = fileOut
    if(os.stat(out).st_size != 0):
        print('')
    print (str(datetime.datetime.now().strftime('%Y-%m-%d')),',',str(datetime.datetime.now().strftime('%H:%M')),end=",")
    print (','.join(map(str,gameList[key])),end="")
    fileOut.close()
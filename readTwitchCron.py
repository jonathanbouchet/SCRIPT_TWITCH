#!/usr/bin/python
import datetime
import requests
import json

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

channels=['Destiny','Overwatch','League%20of%20Legends']
 
for chan in channels :

    outputname = timeStamped('.json')
    fullName = './JSON/' + str(chan) + '-' + outputname
    tempo = []
    with open(fullName,'w') as outf:

        tempoUrl= 'https://api.twitch.tv/kraken/streams/summary?game='+ str(chan)
        print tempoUrl

        response = requests.get(tempoUrl)  

        timeFormat = '%Y-%m-%d %H:%M:%S'
        response = requests.get(tempoUrl)
        tempo = response.json()
        tempo['datetime'] = str(datetime.datetime.now().strftime(timeFormat))
        tempo['date'] = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        tempo['time'] = str(datetime.datetime.now().strftime('%H:%M:%S'))
        tempo['game'] = str(chan)
        print response.json()
        json.dump(tempo,outf,ensure_ascii=False)

outf.close()
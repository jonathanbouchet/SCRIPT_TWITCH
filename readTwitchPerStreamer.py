#!/usr/bin/python

import requests
import json
import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

channels=['Destiny','Overwatch','League%20of%20Legends']

for chan in channels :
    headers = {'Accept': 'application/vnd.twitchtv.v2+json'}
    hs_url = 'https://api.twitch.tv/kraken/streams?game='+str(chan)+'&limit=50'
    print hs_url
    r = requests.get(hs_url, headers = headers)
    rjson = r.json()['streams']
    outputname = timeStamped('.csv')
    fullName = './TopStreamers-' + str(chan) + '-' + outputname
    print fullName
    twitch = open(fullName, 'w')
    for stream in rjson:
        name = stream['channel']['display_name']
        viewers = stream['viewers']
        url = stream['channel']['url']
        status = stream['channel']['status'].encode('utf-8')
        twitch.write(name + ',' + str(viewers) + ',' + str(datetime.datetime.now()) + '\n')
    twitch.close()

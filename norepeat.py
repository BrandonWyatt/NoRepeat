from win32 import win32api
import urllib.request
import json
import time
import pickle
from datetime import date,datetime

today_play = {}
np_artist = ""
np_song = ""

lastday = pickle.load( open( "date.p", "rb" ) )

today = str(date.today())

if today == lastday:
    today_play = pickle.load(open("lastdump.p", "rb"))
else:
    pickle.dump(today, open( "date.p", "wb" ) )

debug = False

while not debug:
    
    page = urllib.request.urlopen("http://radio-api.mediaworks.nz/radio-api/v3/station/therock/web").read()
    page2 = json.loads(page)
    nowplay = page2["nowPlaying"][0]
    nowtype = nowplay["type"]
    if nowtype=="Song":
        if (not np_artist == (nowplay["artist"]) and (not np_song == nowplay["name"])):
            np_song = nowplay["name"]
            np_artist = nowplay["artist"]
            print(nowtype)
            print(nowplay["name"])
            print(nowplay["artist"])
            print(nowplay["played_time"])
            if np_artist not in today_play:
                today_play[np_artist] = {}
            if np_song not in today_play[np_artist]:
                today_play[np_artist][np_song] = []
                today_play[np_artist][np_song].append(nowplay["played_time"])
            else:
                if nowplay["played_time"] not in today_play[np_artist][np_song]:
                    today_play[np_artist][np_song].append(nowplay["played_time"])
                message = 'Possible Duplicate: "' + str(np_song) + '" by ' + str(np_artist) + '\n' + str(today_play[np_artist][np_song])
                win32api.MessageBox(0, str(message), 'Alert', 4096)
                
    else:
        print(nowtype,datetime.now().time())
        for x in range(20):
            time.sleep(1)
    pickle.dump(today_play, open( "lastdump.p", "wb" ) )
    for x in range(10):
        time.sleep(1)
    
    

if debug:
    pass
    

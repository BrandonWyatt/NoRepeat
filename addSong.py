import pickle

today_play = pickle.load(open("lastdump.p", "rb"))

artist = input("Artist name: ")
song = input("Song name: ")
time = input("Time: ")

today_play[artist] = {}
today_play[artist][song] = []
today_play[artist][song].append(time)

pickle.dump(today_play, open( "lastdump.p", "wb" ) )

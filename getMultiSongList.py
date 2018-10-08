import pickle

today_play = pickle.load(open("lastdump.p", "rb"))

for band in today_play:
    
    for song in today_play[band]:
        
        if len(today_play[band][song])>1:
            print(band)
            print(str("    ")+ str(song))
            for time in today_play[band][song]:
                print(str("        ")+ str(time))

input("Press enter to exit")

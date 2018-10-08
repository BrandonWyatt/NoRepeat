import pickle

today_play = pickle.load(open("lastdump.p", "rb"))

for band in today_play:
    print(band)
    for song in today_play[band]:
        print(str("    ")+ str(song))
        for time in today_play[band][song]:
            print(str("        ")+ str(time))

input("Press enter to exit")

## NoRepeat

# Running Requirements
This project has a few requirements; it has been written using Python 2.7.14, and as such, will not run in Python 3. It may run in other versions of Python 2, but these are untested. The alert system is configured for a Windows computer, and is tested on Windows 7 and Windows 10. It is likely to work on Windows 8, or 8.1, as well, but will produce unknown output on other operating systems when a repeat song is discovered (most likely, crash)

The following packages may also be required to be installed:
  - pypiwin32
  - pywin32
  - urllib3

# How To
To get started, simply run "*norepeat.py*" in a terminal, or your preferred alternative. The program will list songs as they begin to play. It will only detect songs while running, however, it it terminates for any reason, the database will persist. This will only be deleted if the script is run on a different date.

There are 3 helper scripts included; *addSong.py*, *getSongList.py*, and *getMultiSongList.py*.

*addSong.py* should be used if *noRepeat.py* has crashed for any reason and you'd like to add a song manually. Follow the prompts, being careful to not make any spelling mistakes, and to follow the conventions of the other songs in the dataset.

*getSongList.py* returns the full list of all songs in the database for the day, nested under the artist names. *getMultiSongList.py* does the same, but only returns songs that have been recorded more than once.

# Limitations
  - It is possible to have a false positive, where a song registers more than once for the same timestamp. This can be easily mitigated by checking the multilist.
  - Requires the user to start running the script at 9am or earlier each day. Planned future improvements to negate this.

from bs4 import BeautifulSoup
import lyricsgenius

""" 
LyricsGenius wrapper can be found here -> https://github.com/johnwmillr/LyricsGenius

We are using this wrapper to unsure that there are no mistakes in the URL because when the user 
inputs the song name and artist, they may be missing information and then when the program
builds the URL for scraping, it will be incorrect and then crash

lyricsscrape will demonstrate the use of the wrapper and the use of the beautifulsoup4
module that searches web pages

"""

# This is a quick example of the wrapper in use

genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")

song = genius.search_song("Without Me (Remix)", "Halsey")

print(song.lyrics)




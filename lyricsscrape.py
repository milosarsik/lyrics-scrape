from bs4 import BeautifulSoup
import lyricsgenius

base_url = 'https://api.genius.com/'

genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")

artist = genius.search_artist("Halsey", max_songs=10)
song = genius.search_song("Without Me", artist.name)
print(song.lyrics)


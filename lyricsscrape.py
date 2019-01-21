from bs4 import BeautifulSoup
import lyricsgenius
from tkinter import *

""" 
LyricsGenius wrapper can be found here -> https://github.com/johnwmillr/LyricsGenius

We are using this wrapper to unsure that there are no mistakes in the URL because when the user 
inputs the song name and artist, they may be missing information and then when the program
builds the URL for scraping, it will be incorrect and then crash

lyricsscrape will demonstrate the use of the wrapper and the use of the beautifulsoup4
module that searches web pages

"""

# master
master = Tk()
master.geometry("300x300")
master.title("Lyrics Scrape")

# master.iconbitmap(r'C:\Users\milos\Documents\A-Z\G\GitHub\lyricsscrape\pythonlogo.png')

# creating menu bar
menuBar = Menu(master)
master.config(menu=menuBar, bg="black")

# this is the sub menu that shows up on the menu bar
subMenu = Menu(menuBar)
menuBar.add_cascade(label="Options", menu=subMenu)

# adding separator
subMenu.add_separator()

# adding "Exit" to the subMenu "Options"
subMenu.add_cascade(label="Exit", command=master.quit)

Label(master, text="Artist Name: ", fg="yellow", bg="black").grid(row=0, sticky=N)          # sticky take N, E, S, W
Label(master, text="Song Name: ", fg="yellow", bg="black").grid(row=1, sticky=N)

artistNameEntry = Entry(master, bg="yellow")
songeNameEntry = Entry(master, bg="yellow")

artistNameEntry.grid(row=0, column=1)
songeNameEntry.grid(row=1, column=1)

searchButton = Button(text="Search", bg="yellow")
searchButton.grid(row=3, column=1)



# showing the gui
master.mainloop()


# genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")

#artistName = input("Artist: ")
#songName = input("Song name:")

#song = genius.search_song(songName, artistName)

#print(song.lyrics)

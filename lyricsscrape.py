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

So far:
-> There is a working GUI with 2 entries that take the artist and song
-> There is a search button that runs getlyrics() method to search for the song
-> NEXT -> Implement a box with scroll view so that all the lyrics fit on one screen to prevent resize

"""

# genius lyrics code
genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")


def getlyrics():
    song = genius.search_song(songNameEntry.get(), artistNameEntry.get())
    print(song.lyrics)                                                      # printing to the screen

    Label(master, text=song.lyrics, fg="yellow", bg="black").grid(row=4, sticky=E)


# master
master = Tk()
master.geometry("500x600")
master.title("Lyrics Scrape")

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

# creating entry labels
Label(master, text="Artist Name: ", fg="yellow", bg="black").grid(row=0, sticky=N)          # sticky take N, E, S, W
Label(master, text="Song Name: ", fg="yellow", bg="black").grid(row=1, sticky=N)

# creating entries for song and artist name
artistNameEntry = Entry(master, bg="yellow")
songNameEntry = Entry(master, bg="yellow")

artistNameEntry.grid(row=0, column=1)
songNameEntry.grid(row=1, column=1)

# creating the search button
searchButton = Button(text="Search", bg="yellow", command=getlyrics)
searchButton.grid(row=3, column=1)

# showing the gui
master.mainloop()

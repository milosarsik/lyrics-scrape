import body as body
import lyricsgenius
import smtplib
import ssl
import time

from tkinter import *

from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

""" 
LyricsGenius wrapper can be found here -> https://github.com/johnwmillr/LyricsGenius

We are using this Genius API wrapper to unsure that there are no mistakes in the URL because when the user 
inputs the song name and artist, they may be missing information and then when the program
builds the URL for scraping, it will be incorrect and then crash

lyricsscrape will demonstrate the use of the wrapper and the use of the beautifulsoup4
module that searches web pages

"""

# genius lyrics api code
genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")

# port for SSL
port = 465

context = ssl.create_default_context()                          # create a secure SSL context


# variables
emails = []
sender_email = "yourpylyrics@gmail.com"

# functions
def clearentries():
    artistNameEntry.delete(0, 'end')
    songNameEntry.delete(0, 'end')
    timesSentEntry.delete(0, 'end')


def getArtist():
    return artistNameEntry.get()


def getSong():
    return songNameEntry.get()


def getEmail():
    return emailEntry.get()


def getTimesSent():
    return int(timesSentEntry.get())


def getlyrics():
    song = genius.search_song(songNameEntry.get(), artistNameEntry.get())
    lyrics = songNameEntry.get() + " by " + artistNameEntry.get() + "\n" + "\n" + song.lyrics

    print(song.lyrics)

    return lyrics


def writelyrics():
    file = open("yourlyrics.txt", "w+")

    lyrics = getlyrics()

    file.write(lyrics)

    file.close()


def sendemail():
    msg = MIMEMultipart()                                       # creating a multi part message

    msg["To"] = getEmail()
    msg["From"] = sender_email
    msg["Subject"] = "The lyrics to the song " + getSong() + " by " + getArtist() + "... "

    bodylyrics = getlyrics()

    msgText = MIMEText(bodylyrics, 'plain')

    msg.attach(msgText)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "lyricsscrape")
        # TODO: Send email here
        for i in range(getTimesSent()):
            server.sendmail(sender_email, getEmail(), msg.as_string())


# master
master = Tk()
master.geometry("250x200")
master.title("Lyrics Scrape")

# button frame
buttonFrame = Frame(master)
buttonFrame.config(bg="black")
buttonFrame.grid(row=4, column=0)


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
Label(master, text="Email: ", fg="yellow", bg="black").grid(row=2, sticky=N)
Label(master, text="Send __ emails (#): ", fg="yellow", bg="black").grid(row=3, sticky=N)

# creating entries for song, artist and email
artistNameEntry = Entry(master, bg="yellow")
songNameEntry = Entry(master, bg="yellow")
emailEntry = Entry(master, bg="yellow")
timesSentEntry = Entry(master, bg="yellow")

artistNameEntry.grid(row=0, column=1)
songNameEntry.grid(row=1, column=1)
emailEntry.grid(row=2, column=1)
timesSentEntry.grid(row=3, column=1)

# search button
searchButton = Button(buttonFrame, text="Search", bg="yellow", command=getlyrics)
searchButton.grid(row=3, column=0)

# write button
writeButton = Button(buttonFrame, text="Write", bg="yellow", command=writelyrics)
writeButton.grid(row=4, column=0)

# clear button
clearButton = Button(buttonFrame, text="Clear", bg="yellow", command=clearentries)
clearButton.grid(row=5, column=0)

# send email button
emailButton = Button(buttonFrame, text="Send Email", bg="yellow", command=sendemail)
emailButton.grid(row=6, column=0)

# showing the gui
master.mainloop()

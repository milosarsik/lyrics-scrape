import body as body
import lyricsgenius
import smtplib
import ssl

from tkinter import *

from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

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
# port for SSL
port = 465

# create a secure SSL context
context = ssl.create_default_context()

# creating the message (multi part)
#attachment =

msg = MIMEMultipart()
msg["To"] = "EMAIL"
msg["From"] = "EMAIL"
msg["Subject"] = "Your lyrics to the song... "

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % body, 'html')
msg.attach(msgText)   # Added, and edited the previous line

#fp = open(attachment, 'rb')
#img = MIMEImage(fp.read())
#fp.close()
#img.add_header('Content-ID', '<{}>'.format(attachment))
#msg.attach(img)

# string
                                                                                                                                                                                    #emails = ["szwejz_hadvid@hotmail.com", "cdevito2@uwo.ca", "marcdejesus03@gmail.com", "habsfansrock@gmail.com", "connorbh111@gmail.com", "mjnsammut@gmail.com", "elia413buragina@gmail.com", "michaeltriluong@gmail.com", "cyriacjinson968@gmail.com"]

#
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("EMAIL", "PASS")
    # TODO: Send email here
#    for i in range(15):
#        for k in range(2):
#            server.sendmail("EMAIL", emails[k], msg.as_string())






# genius lyrics code
genius = lyricsgenius.Genius("W35CW_FDSRpwxHZ8oh27GGtG3dAEt66EAcNG6S0zjRS26YZkueVELFwbulTLiEWl")

def clearentries():
    artistNameEntry.delete(0, 'end')
    songNameEntry.delete(0, 'end')

def getlyrics():
    song = genius.search_song(songNameEntry.get(), artistNameEntry.get())
    print(song.lyrics)                                                      # printing to the screen

    return song.lyrics
    #Label(master, text=song.lyrics, fg="yellow", bg="black").grid(row=4, sticky=E)

def writelyrics():
    file = open("yourlyrics.txt", "w+")
    song = genius.search_song(songNameEntry.get(), artistNameEntry.get())
    lyrics = song.lyrics
    file.write(lyrics)

    file.close()

# master
master = Tk()
master.geometry("400x400")
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
searchButton.grid(row=3, column=3)

# write to textfile button
writeButton = Button(text="Write", bg="yellow", command=writelyrics)
writeButton.grid(row=4, column=3)

# clear button
clearButton = Button(text="Clear", bg="yellow", command=clearentries)
clearButton.grid(row=3, column=5)



# showing the gui
master.mainloop()

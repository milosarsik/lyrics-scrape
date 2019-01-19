from tkinter import *

# you cannot use grid and pack together in the same program, idk why, they just don't work

# quick test function to see if the button can run it
def create():
    button5 = Button(topFrame, text="Search(Button 5)", fg="black")
    button5.pack(side=BOTTOM)

root = Tk()                                     # this is a blank window

# this creates a frame, it is an invisible contatiner that we have set to be in the root
topFrame = Frame(root)
#topFrame.pack()

bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

# creating a bunch of buttons, setting the text, foreground and background
button1 = Button(topFrame, text="Search(Button 1)", fg="red", bg="blue")
button2 = Button(topFrame, text="Search(Button 2)", fg="blue")
button3 = Button(topFrame, text="Search(Button 3)", fg="green")
button4 = Button(bottomFrame, text="Search(Button 4)", fg="purple", command=create)             # here we add a command

# button1.pack(side=LEFT)                         # side sets where the button will be packed in to
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)


# this is how to create a label
theLabel = Label(topFrame, text="Lyrics Scraper")
# theLabel.pack()                                 # pack means pack it in to the first place that it fits

# fitting widgets in your layout section
one = Label(root, text="One", bg="red", fg="white")
# one.pack()

two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)                                # fill means that it will adjust to the size of the screen

three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)


# grid layout
Label(root, text="Name").grid(row=0, sticky=E)
Label(root, text="Password").grid(row=1, sticky=E)

entry1 = Entry(root)
entry2 = Entry(root)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()                                     # constant loop to show the frames



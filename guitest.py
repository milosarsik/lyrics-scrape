from tkinter import *
import tkinter.messagebox

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

# button1.pack(side=LEFT)                               # side sets where the button will be packed in to
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)


# this is how to create a label
theLabel = Label(topFrame, text="Lyrics Scraper")
# theLabel.pack()                                       # pack means pack it in to the first place that it fits

# fitting widgets in your layout section
one = Label(root, text="One", bg="red", fg="white")
# one.pack()

two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)                                      # fill means that it will adjust to the size of the screen

three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# grid layout
#Label(root, text="Name").grid(row=0, sticky=E)          # sticky take N, E, S, W
#Label(root, text="Password").grid(row=1, sticky=E)

entry1 = Entry(root)
entry2 = Entry(root)


#entry1.grid(row=0, column=1)
#entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)                                    # this merges two cells




# binding functions to layouts
def printname(event):
    print("Milos")

clickbutton = Button(root, text="Click to print")
clickbutton.bind("<Button-1>", printname)   # we can do either command, or we can do it this way, this means left mouse button
#clickbutton.pack()



# mouse click events (tut 7)
def leftClick(event):
    print("left")

def middleClick(event):
    print("mid")

def rightClick(event):
    print("right")

#frame = Frame(root, width=300, height=250)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)
#frame.pack()


#using classes (tut 8) use this to create the gui at once, jsut pass in the main frame
#class TestClass:
    #def __init__(self, master):                 # called automatically, special, master takes in the root
        #frame = Frame(master)
        #frame.pack()

        #self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        #self.printButton.pack(side=LEFT)

        #self.quitButton = Button(frame, text="Quit", command=frame.quit)
        #self.quitButton.pack(side=LEFT)

    #def printMessage(self):
        #print("DAMN, it works")

#test = TestClass(root)









# creating drop down menus (tut 9)
#       **MAIN MENU**

def donothing():
    print("not doing anything")

#menu = Menu(root)
#root.config(menu=menu)

#submenu = Menu(menu)
#menu.add_cascade(label="File", menu=submenu)            # File(drop down functionality) is the button, and then the sub is submenu

#submenu.add_command(label="New Project...", command=donothing)      # adds the following options to the file menu
#submenu.add_command(label="Add", command=donothing)
#submenu.add_command(label="OTHER", command=donothing)

#submenu.add_separator()                                 # just adds a separation line
#submenu.add_command(label="Exit", command=root.quit)

#editmenu = Menu(menu)
#menu.add_cascade(label="Edit", menu=editmenu)
#editmenu.add_command(label="Redo", command=donothing)

# creating a toolbar
#           **TOOLBAR**
#toolbar = Frame(root, bg="blue")                # frame stretches across main menu

#insertbutton = Button(toolbar, text="Insert Image", command=donothing)
#insertbutton.pack(side=LEFT, padx=2, pady=2)
#printbutton = Button(toolbar, text="Print", command=donothing)
#printbutton.pack(side=LEFT, padx=2, pady=2)

#toolbar.pack(side=TOP, fill=X)




# adding the status bar
#           **STATUS BAR**

#status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)           # bd is the border, relief makes it look better
#status.pack(side=BOTTOM, fill=X)




# messageboxes
#tkinter.messagebox.showinfo('Window Title', 'Heellloooo')

#answer = tkinter.messagebox.askquestion('Question 1', 'How are you?')

#if answer == 'yes':
    #print("GOOD, IM GLAD")

# shapes and graphics (tut 13)

#canvas = Canvas(root, width=200, height=100)
#canvas.pack()

#blackline = canvas.create_line(0,0, 200, 50)                # starts at top left remember this
#redline = canvas.create_line(0,100, 200, 50, fill="red")

#greenbox = canvas.create_rectangle(25, 25, 130, 60, fill="green")                        # param: top left, top left, width, height
#canvas.delete(redline)

#canvas.delete(ALL)                     # deletes all of the drawings



# images and icons (tut 14)

#photo = PhotoImage(file="another.png")
#labelimage = Label(root, image=photo)
#labelimage.pack()

root.mainloop()                                         # constant loop to show the frames



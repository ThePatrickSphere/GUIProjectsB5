from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())
    E1.delete(0, END)
    
def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()
        
def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column= 0, row= 1)
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column= 0, row= 2)
    B2Main = Button(text = "Week 2", bg = "#f0a1e9")
    B2Main.grid(column= 0, row= 3)
    B3Main = Button(text = "Week 3", bg = "#54cf17")
    B3Main.grid(column= 0, row= 4)

def week1():
    clearWindow()
    #This is a label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column= 0, row= 1)

    #This is an entry widget for text entry
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    #This is a button widget
    B1 = Button(text = " + ", bg = "white", command = addTrack)
    B1.grid(column= 1, row= 2)

    #This is another button widget
    B2 = Button(text = "Playlist", bg = "#d4850f", command = printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text = "Export", bg= "#4940e6", command=exportList)
    B3.grid(column= 1, row= 3)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

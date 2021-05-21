from tkinter import *
import random

top = Tk()
songList = []
myRolls = []
rollTimes = 0
dieType = 0
toDoList = []


    
def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)            

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def taskList():
    with open("To-Do List.txt", "w") as f:
        for item in toDoList:
            f.write("%s\n" % item)
    f = open("To-Do List.txt", "r")
    print(f.read())

def showList():
    clearWindow()
    L3W3 = Label(top, text = "Here's your to-do list!")
    L3W3.pack()
    
    L4W3 = Label(top, text = "{}".format(toDoList))
    L4W3.grid(column = 0, row = 1)

    B3W3 = Button(text = "Export", bg = "#4ae0e8", command = taskList)
    B3W3.grid(column = 1, row = 3)

    B4W3 = Button(text = "Main Menu", bg = "yellow", command = mainMenu)
    B4W3.grid(column = 0, row = 3)
           
def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column= 0, row= 1)
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column= 0, row= 2)
    B2Main = Button(text = "Week 2", bg = "#f0a1e9", command = week2)
    B2Main.grid(column= 0, row= 3)
    B3Main = Button(text = "Week 3", bg = "#54cf17", command = week3)
    B3Main.grid(column= 0, row= 4)

def week1():
    
    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)
    
    clearWindow()
    #This is a label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column= 0, row= 1)

    #This is an entry widget for text entry
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    #This is a button widget
    B1 = Button(text = "Add", bg = "white", command = addTrack)
    B1.grid(column= 1, row= 2)

    #This is another button widget
    B2 = Button(text = "Print", bg = "#c78bc7", command = printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text = "Export", bg= "#ccc423", command=exportList)
    B3.grid(column= 1, row= 3)

    B4 = Button(text = "Main Menu", bg = "yellow", command = mainMenu)
    B4.grid(column = 0, row = 3)

def week2():
    def rollDice():
        rollTimes = E1W2.get()
        dieType = E2W2.get()
        clearWindow()
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        L4W2 = Label(top, text = "Here are your rolls!")
        L4W2.grid(column = 0, row = 1)
        
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text = "Main Menu", bg = "yellow", command = mainMenu)
        B2W2.grid(column = 0, row = 3)
        
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller")
    L1W2.grid(column= 2, row= 1)
    
    L2W2 = Label(top, text = "# of Rolls")
    L2W2.grid(column= 0, row= 2)
    
    L3W2 = Label(top, text = "# of Sides")
    L3W2.grid(column= 3, row= 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column= 0, row= 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column= 3, row= 3)
    
    B1W2 = Button(text = "Roll them!", bg = "#e787ff", command = rollDice)
    B1W2.grid(column= 2, row= 4)
    
def week3():
    def addTask():
        toDoList.append(E1W3.get())
        E1W3.delete(0, END)

    def showList():
        clearWindow()
        L3W3 = Label(top, text = "Here's your to-do list!")
        L3W3.grid(column = 0, row = 1)
        
        L4W3 = Label(top, text = "{}".format(toDoList))
        L4W3.grid(column = 0, row = 2)

        B3W3 = Button(text = "Export", bg = "#4ae0e8", command = taskList)
        B3W3.grid(column = 1, row = 3)

        B4W3 = Button(text = "Main Menu", bg = "yellow", command = mainMenu)
        B4W3.grid(column = 0, row = 3)
        
    clearWindow()

    L1W3 = Label(top, text = "Task Manager")
    L1W3.grid(column = 2, row = 0)

    L2W3 = Label(top, text = "What do you have to do today?")
    L2W3.grid(column= 2, row= 2)
    
    E1W3 = Entry(top, bd = 5)
    E1W3.grid(column= 2, row= 3)

    B1W3 = Button(text = "Add", bg = "#4ae0e8", command = addTask)
    B1W3.grid(column = 3, row = 3)

    B2W3 = Button(text = "Show", bg = "#4ae0e8", command = showList)
    B2W3.grid(column = 2, row = 4)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

from tkinter import *
from tkinter import ttk
import os

root = Tk(screenName="File Deleter", baseName=None,className='Tk', useTk=True, sync = False, use=None)

#setting the size of a window
root.geometry("400x400")
root.minsize(300,300)
root.maxsize(600,600)

#Create a label
label = Label(root, text = "Directory path", font =("Arial", 14))

#Create an Entry widget
entry = Entry(root, font=("Arial",14), width=30)

#Create button
enter_path_btn = Button(root, font=("Arial", 14), width=15,height=1,anchor="center", text = "Enter")

#2nd label
label2 = Label(root, text = "File extensions to exclude: ", font =("Arial", 14))

#listing files
directory_path = entry.get()
files = os.listdir(directory_path)


label.pack()
entry.pack()
enter_path_btn.pack()
root.mainloop()
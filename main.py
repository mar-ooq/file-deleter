from tkinter import *
from tkinter import ttk, filedialog
import os
import configparser
import os
from pathlib import Path
from setup import create_config
from delete_files import delete_files

#listing files
def list_files():
    file = configparser.ConfigParser()
    file.read('config.conf')
    directory_path = file.get('path','file_path')
    
    # TERAZ TUTAJ - WPISZ DO FRAME'a
    files = os.listdir(directory_path)
    for f in files:
        text = Label(scrollable_frame, text=f, width=30, anchor='w')
        text.pack(pady=2, fill="x")
def get_path():
    path = entry.get()
    config = configparser.ConfigParser()
    config.read('config.conf')
    config.set('path','file_path', path)
    with open('config.conf','w') as f:
            config.write(f)

def browse_folder():
    folder = filedialog.askdirectory(title="Wybierz folder")
    if folder:
        entry.delete(0, END)
        entry.insert(0, folder)

create_config()

root = Tk(screenName="File Deleter", baseName=None,className='Tk', useTk=True, sync = False, use=None)

#setting the size of a window
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(600,600)

#Create a label
label = Label(root, text = "Directory path", font =("Arial", 14))
label.pack()
#Putting Entry and browse_btn next to each other
input_frame = Frame(root)
input_frame.pack(pady=5)

#Create an Entry widget
entry = Entry(input_frame, font=("Arial",14), width=25)
entry.pack(side=RIGHT, padx=5, fill=X, expand=True)

#browsing directories
browse_btn = Button(input_frame, text="Search", command=browse_folder, font=("Arial", 12))
browse_btn.pack(side=LEFT, padx=5)

#Create button
enter_path_btn = Button(root, font=("Arial", 14), width=15,height=1,anchor="center", text = "Enter", command=lambda:[get_path(), list_files()])
enter_path_btn.pack()

#Create Frame
frame=Frame(root,width=300,height=150)
frame.pack(expand=False, fill=BOTH)
    
canvas=Canvas(frame,width=300,height=150)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

vbar_container = Frame(frame, height=150, width=16)
vbar_container.pack_propagate(False)
vbar_container.pack(side=RIGHT, fill="y")


vbar=Scrollbar(vbar_container,orient=VERTICAL, width=12)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(yscrollcommand=vbar.set)

# SCROLLABLE FRAME W Canvas
scrollable_frame = Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
    
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

#2nd label
label2 = Label(root, text = "File extensions to exclude: ", font =("Arial", 14))


root.mainloop()
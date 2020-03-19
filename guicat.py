import subprocess
import os
import tkinter
import shutil

from os import path
from shutil import copy
from tkinter import *
from tkinter import filedialog

###
# Global Variables
rootdir = "./"
hccapxpath = ''
wordlistpath = ''


# Main Config:
window = Tk()
window.title("GUICAT Hashcat GUI")
window.configure(background="black")
window.geometry("485x250+700+300")


# R0 - Logo (get rid of background in .gif)
logo = PhotoImage(file="guihashcatlogo.gif")
Label(window, image=logo, bg="black") .grid(row=0, column=1, sticky=N)


# R1 - Label - Select .hccapx file from .\hccapx-files\
Label(window, text="Choose .hccapx File:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=1, pady=2, sticky=S)


# R2 - Search Directories Button - Opens file explorer in .\hccapxfiles, deletes previous .hccapx file, saves output to variable and renames the file within hashcat directory
def browsehccapx():
    if path.exists(".\selected.hccapx"):
        os.remove(".\selected.hccapx")
    else:
        pass
    hccapxpath = filedialog.askopenfilename(initialdir=".\hccapxfiles", title="Select handshake .hccapx file",filetypes=((".hccapx files","*.hccapx"),("all files","*.*")))
    hccapxpath = shutil.copy(hccapxpath, rootdir)
    os.rename("{}".format(hccapxpath), ".\selected.hccapx")

Button(window, text="Browse", width=6, command=browsehccapx) .grid(row=2, column=1, sticky=W)


# R2 - Text entry for .hccapx file path (Change to display selected file path(figuring this out))
if hccapxpath != '':
    hccapxpathtxt = Entry(window, textvariable=hccapxpath, width=65, bg="white")
    hccapxpathtxt.grid(row=2, column=1, padx=3, sticky=E)
else:
    hccapxpathtxt = Entry(window, width=65, bg="white")
    hccapxpathtxt.grid(row=2, column=1, padx=3, sticky=E)


# R3 - Spacer 10

# R4 - Label - Choose Wordlist
Label(window, text="Choose Wordlist:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=1, pady=2, sticky=S)


# R5 - Search Directories Button - Opens file explorer in ./wordlists, deletes previous wordlist, saves output to variable, and renames file within hashcat directory
def browsewordlists():
    global wordlistpath
    if path.exists(".\selected.dict"):
        os.remove(".\selected.dict")
    else:
        pass
    wordlistpath = filedialog.askopenfilename(initialdir=".\wordlists", title="Select wordlist .dict file",filetypes=((".dict files","*.dict"),("all files","*.*")))
    wordlistpath = shutil.copy(wordlistpath, rootdir)
    os.rename("{}".format(wordlistpath), ".\selected.dict")

Button(window, text="Browse", width=6, command=browsewordlists) .grid(row=5, column=1, sticky=W)


# R5 - Text entry for wordlist file path (Change to display selected file path(figuring this out))
if wordlistpath != '':
    wordlistpathtxt = Entry(window, textvariable=wordlistpath, width=65, bg="white")
    wordlistpathtxt.grid(row=5, column=1, padx=3, sticky=S)
else:
    wordlistpathtxt = Entry(window, width=65, bg="white")
    wordlistpathtxt.grid(row=5, column=1, padx=3, sticky=E)


# R6 - Spacer 20

# R7 - Submit/Start Hashcat Button - Runs Hashcat with input variables, then outputs the cracked hccapx file password into CRACKED.txt
def clicksubmit():
    subprocess.call(".\hashcat64.exe -m 2500 selected.hccapx selected.dict -o CRACKED.txt", shell=True)
Button(window, text="BEGIN CRACKING", width=13, padx=3, pady=3, command=clicksubmit) .grid(row=7, column=1, sticky=S)


### R7 - Show Potfile Button - Opens hashcat.potfile in notepad
def clickpotfile():
    os.system("notepad.exe hashcat.potfile")
Button(window, text="Cracked Hashes", width=13, padx=2, pady=2, command=clickpotfile) .grid(row=7, column=1, sticky=W)


# R7 - Exit Button
def clickexit():
    window.destroy()
Button(window, text="Exit", width=13, padx=2, pady=2, command=clickexit) .grid(row=7, column=1, sticky=E)


### Grid Spacers ###
# Rows:
window.grid_rowconfigure(3, minsize=10)
window.grid_rowconfigure(6, minsize=20)
# Columns:
window.grid_columnconfigure(0, minsize=15) # 15px margin on left
window.grid_columnconfigure(2, minsize=15) # 15px margin on right


##### Main Loop
window.mainloop()

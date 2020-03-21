import subprocess
import os
import tkinter
import shutil

from tkinter import *
from tkinter import filedialog
from os import path
from shutil import copy

#####
# Global Variables
rootdir = "./"
hccapxpath = ""
wordlistpath = ""

# Functions:
# Select .hccapx File Button:
# Open file explorer, select .hccapx file, copy .hccapx file to root hashcat dir, then renames to selected.hccapx.
# If selected.hccapx is already in the root dir, then it is deleted upon pressing the browse hccapx button.
########### THIS IS THE FUNCTION IN QUESTION, problem area marked below #############
def browsehccapx():
    if path.exists(".\selected.hccapx"):
        os.remove(".\selected.hccapx")
    else:
        pass
    hccapxpath = filedialog.askopenfilename(initialdir=".\hccapxfiles", title="Select handshake .hccapx file",filetypes=((".hccapx files","*.hccapx"),("all files","*.*")))
    hccapxpath = shutil.copy(hccapxpath, rootdir)
    os.rename("{}".format(hccapxpath), ".\selected.hccapx")
#####################################################################################

# Select Wordlist Button - Open file explorer, select .dict file, copy .dict file to root hashcat dir, then renames to selected.dict.
# If selected.dict is already in the root dir, then it is deleted upon pressing the browse wordlist button.
########### SAME ISSUE ##############################################################
def browsewordlists():
    if path.exists(".\selected.dict"):
        os.remove(".\selected.dict")
    else:
        pass
    wordlistpath = filedialog.askopenfilename(initialdir=".\wordlists", title="Select wordlist .dict file",filetypes=((".dict files","*.dict"),("all files","*.*")))
    wordlistpath = shutil.copy(wordlistpath, rootdir)
    os.rename("{}".format(wordlistpath), ".\selected.dict")
#####################################################################################

# Start Hashcat Button - runs selected.hccapx and selected.dict in hashcat64.exe
def clicksubmit():
    subprocess.call(".\hashcat64.exe -m 2500 selected.hccapx selected.dict", shell=True)

# Open hashcat.potfile in Notepad Button - Reveils cracked hashes/passwords
def clickpotfile():
    os.system("notepad.exe hashcat.potfile")

# Exit Button - Exits GUI and CMD
def clickexit():
    window.destroy()

# Main Config:
window = Tk()
window.title("GUICAT - Minimal Hashcat GUI")
window.configure(background="black")
window.geometry("485x250+700+300")

# R0 - Logo (get rid of background in .gif)
logo = PhotoImage(file="guihashcatlogo.gif")
Label(window, image=logo, bg="black") .grid(row=0, column=1, sticky=N)

# R1 - Label - Select .hccapx file from .\hccapx-files\
Label(window, text="Choose .hccapx File:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=1, pady=2, sticky=S)

# R2 - Search Directories Button - Opens file explorer in .\hccapxfiles, deletes previous .hccapx file, saves output to variable and renames the file within hashcat directory
Button(window, text="Browse", width=6, command=browsehccapx) .grid(row=2, column=1, sticky=W)

# R2 - Text entry for .hccapx file path (Change to display selected file path(figuring this out))
######## THE ISSUE ########
# The textvariable is set to the proper variable containing the path to the .hccapx file, however
# when the browsehccapx() function is called, the blank entry is not updated.
# Same issue with the same type of function but for variable wordlistpathtxt.
hccapxpathtxt = Entry(window, textvariable=hccapxpath, width=64, bg="white")
hccapxpathtxt.grid(row=2, column=1, padx=3, sticky=E)
###########################

# R3 - Spacer 10

# R4 - Label - Choose Wordlist
Label(window, text="Choose Wordlist:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=1, pady=2, sticky=S)

# R5 - Search Directories Button - Opens file explorer in ./wordlists, deletes previous wordlist, saves output to variable, and renames file within hashcat directory
Button(window, text="Browse", width=6, command=browsewordlists) .grid(row=5, column=1, sticky=W)

# R5 - Text entry for wordlist file path (Change to display selected file path(figuring this out))
####### SAME ISSUE #########
wordlistpathtxt = Entry(window, width=64, bg="white")
wordlistpathtxt.grid(row=5, column=1, padx=3, sticky=E)
############################

# R6 - Spacer 20

# R7 - Submit/Start Hashcat Button - Runs Hashcat with input variables, then outputs the cracked hccapx file password into CRACKED.txt
Button(window, text="BEGIN CRACKING", width=13, padx=3, pady=3, command=clicksubmit) .grid(row=7, column=1, sticky=S)

### R7 - Show Potfile Button - Opens hashcat.potfile in notepad
Button(window, text="Cracked Hashes", width=13, padx=2, pady=2, command=clickpotfile) .grid(row=7, column=1, sticky=W)

# R7 - Exit Button
Button(window, text="Exit", width=13, padx=2, pady=2, command=clickexit) .grid(row=7, column=1, sticky=E)

### Grid Spacers ###
# Rows:
window.grid_rowconfigure(3, minsize=10)
window.grid_rowconfigure(6, minsize=20)
# Columns:
window.grid_columnconfigure(0, minsize=15) # 15px margin on left
window.grid_columnconfigure(2, minsize=15) # 15px margin on right
###

##### Main Loop
window.mainloop()

GUICAT-package
WINDOWS HASHCAT GUI
by FreedmanRy

NOTICE:
Currently working on a fix to display selected file paths to the text boxes. updates will come soon.


GUICAT is a simple python file using the Tkinter library
To use GUICAT, just paste all files contained in this package into your hashcat-x.x.x directory. It is important that all the files be inside the same directory as hashcat64.exe or you will receive an error.

Since GUICAT is designed for Windows use, you may double click the GUICAT.bat file to begin the program.
GUICAT.bat is a batch file that can be clicked in file explorer to run guicat.py without CMD or PowerShell.

GUICAT takes 2 inputs:
  1 .hccapx file from ./hccapxfiles/
  1 wordlist from ./wordlists/

Clicking 'BEGIN CRACKING' will run Hashcat64.exe in CMD using your GPU(s) and selected file paths.

Clicking 'Cracked Hashes' will open hashcat.potfile in notepad, containing all successfully cracked hashes
  with no duplicates.

You may create a Desktop Shortcut linked to this batch file, as long as the batch file remains in the
root hashcat directory. Right-click GUICAT.bat and click "Create Shortcut".
GUICAT - MINIMAL WINDOWS HASHCAT GUI
by FreedmanRy

GUICAT is a simple python file using the tkinter library

To use GUICAT, just paste all files contained in this package into your hashcat-x.x.x directory. It is important that all the files be inside the same directory as hashcat64.exe or you will receive an error.

NOTE:
GUICAT has python dependencies that will be available as a setup file as this program grows

Since GUICAT is designed for Windows use, you may double click the GUICAT.bat file to begin the program.
GUICAT.bat is a batch file that can be double-clicked in file explorer to run guicat.py without CMD or PowerShell.

GUICAT takes 2 inputs:
  1 .hccapx file from ./hccapxfiles/
  1 wordlist from ./wordlists/
Add your files to these directories for use.
(.cap files can be converted to .hccapx with hashcat-utils or at https://hashcat.net/cap2hccapx/)

Clicking 'BEGIN CRACKING' will run Hashcat64.exe in CMD using your GPU(s) and selected file paths.

Clicking 'Cracked Hashes' will open hashcat.potfile in notepad, containing all successfully cracked hashes
  with no duplicates.

You may create a Desktop Shortcut linked to this batch file, as long as the batch file remains in the
root hashcat directory. Right-click GUICAT.bat and click "Create Shortcut".

Any comments, concerns, or reccomendations may be e-mailed to ryanfreedman.dev@gmail.com

Enjoy!
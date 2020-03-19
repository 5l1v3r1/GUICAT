GUICAT-package
WINDOWS HASHCAT GUI
by Ryan Freedman

GUICAT is a python file using the Tkinter library
To use GUICAT, just paste all files contained in this package into your hashcat-x.x.x directory. It is important that all the files be inside the same directory as hashcat64.exe or you will receive an error.

GUICAT takes 2 inputs:
  1 .hccapx file from ./hccapxfiles/
  1 wordlist from ./wordlists/

Clicking 'Release the Cracken!' will run Hashcat64.exe in CMD using your GPU(s) and selected file paths.

Clicking 'Cracked Hashes' will open hashcat.potfile in notepad, containing all successfully cracked hashes
  with no duplicates.

GUICAT.bat is a batch file that can be clicked in file explorer to run guicat.py without CMD or PowerShell.

You may create a Desktop Shortcut linked to this batch file, as long as the batch file remains in the
root hashcat directory. Right-click GUICAT.bat and click "Create Shortcut".
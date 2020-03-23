GUICAT - MINIMAL WINDOWS HASHCAT GUI
by FreedmanRy

GUICAT is a simple python file that uses the tkinter library. It is a minimalistic GUI that takes 1 .hccapx file (custom Hashcat format for WPA/WPA2 handshakes) and 1 .dict file (Dictionary wordlist file, 1 entry on each line), then runs them through Hashcat, a popular bruteforcing tool found here:

https://github.com/hashcat/hashcat

To use GUICAT, just paste all files contained in this package into your hashcat-x.x.x directory. 
It is important that all the files be inside the same directory as hashcat64.exe or you will receive an error.

place your .hccapx files in .\hashcat-x.x.x\hccapxfiles\
place your wordlists in .\hashcat-x.x.x\wordlists\

TIP: .cap files can be converted to .hccapx with hashcat-utils or at https://hashcat.net/cap2hccapx/

GUICAT.bat is a batch file that can be double-clicked in file explorer to run guicat.py without using the command line. You may also make a shortcut of this file and place it on your desktop for easy access.

Click 'BEGIN CRACKING' to run Hashcat64.exe in CMD using the files you have selected. 
Hashcat will automatically utilize your GPUs for cracking speed.

NOTE: I WILL NOT BE HELD ACCOUNTABLE FOR ANY MALICIOUS THINGS YOU DO WHILE USING THIS TOOL. USE AT YOUR OWN RISK.

Click 'Cracked Hashes' to open hashcat.potfile in notepad, which contains all successfully cracked hashes with no duplicates.

Any comments, concerns, or recommendations may be e-mailed to ryanfreedman.dev@gmail.com

Enjoy!

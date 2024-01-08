* INFORMATION *

What does this script do?
- Detects the country, location, city... etc of the players inside your multiplayer lobby and prints everything in console.

It can also work for any other P2P game, you just need to change the UDP port.

* PREREQUISITES *

Install python from the official website.
- https://www.python.org/downloads/windows/
- Go into the latest release and download the installer 64-bit version.
- Make sure you have the 'Add Python to PATH' checkbox enabled when installing (https://files.catbox.moe/lshxcs.png)

You will also need to download an npcap driver to your system.
- https://npcap.com/
- Download the installer version

* RUNNING *

Open the CMD.
- You can do this by pressing the WIN+R combination and entering 'cmd'.
- CD inside of the directory with your 'grabber.py' file (https://files.catbox.moe/qohfhf.png)
- Type 'pip install -r requirements.txt' into the console and hit enter.
- After doing all those steps, keep the console open.

Open 'grabber.py' file in any text editor.
- Find this line (https://files.catbox.moe/syszr0.png)
- Open up a new CMD window (instructions on how to do so above)
- Type 'ipconfig'.
- Look for the IPv4 Address line (https://files.catbox.moe/oaueqa.png)
- Replace the text in the brackets that we have found inside the file to your IPv4 Address.

Run 'grabber.py'
- Go into the first CMD window that we have opened.
- Type 'python grabber.py' and join any multiplayer game.
- Now you should see locations of people popping up inside of the console window.

* YOU'VE DONE EVERYTHING CORRECTLY, BUT IT STILL DOES NOT WORK? *

It's probably because the UDP port for Dying Light is different for you.
- Download and open TCPView. (https://learn.microsoft.com/en-us/sysinternals/downloads/tcpview)
- Unselect 'TCP v4' and 'TCP v6'.
- Type 'dyinglight' into the search bar.
- Join any multiplayer game looking at the program in the same time.
  (Green colored connections should appear in the program, LOOK AT WHICH PORT THEY USE)
  (Example: https://files.catbox.moe/3i0ta0.png)
- Replace the default 7777 port inside 'grabber.py' with the one you saw in the program. (https://files.catbox.moe/ulpfr3.png)
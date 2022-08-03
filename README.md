# PVZ-NDS-Manipulator
Manipulates the three (3) data files in the NDS version of Plants vs. Zombies. Yes, really, everything is inside of three "pack" bins (well, not the sound, or assembly,
or any of the other usual stuff).

This program uses the Command Line, although a helpful drag and drog batch file is provided for Windows users. First, you obviously need to install Python. Then run
```python arcvUnpacker.py name-of-bin``` to unpack the bin. OR you can run ```python arcvUnpacker.py name-of-bin name-of-file``` to make a copy of the bin with
the file you entered inside it.

WARNING: do not rename the files! The name is how the program knows where to insert the file so that it overwrites itself, as it were,
and nothing else is messed up.

Also, you cannot change file sizes for insertion. Larger files are truncated, while smaller files get a bunch of 0x00's added to the end. If this becomes a problem, do 
let me know.

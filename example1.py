#!python3

"""

demonstration of clearing your terminal
using 

import os
os.system("cls")

"""

import os

print("This is some output")

pause = input("Press return to continue")

os.system("cls")
# note that to use the command in Linux/MacOS, you would use
# os.system("clear") instead

print("Cleared the screen!")
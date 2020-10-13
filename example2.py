#!python3

""" 
random number generation using the random module

import random
random.randin(x,y) creates a random integer from x to y, which could include both 
numbers as the upper and lower limits.
"""

import random

for i in range(0,1000):
    x = random.randint(0,4)

    print(x, end=" ")
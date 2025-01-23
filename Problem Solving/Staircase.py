#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    staircase = ""

    # Iterate over the rows of the staircase.
    for i in range(n):
        # Add the required number of spaces to the staircase.
        staircase += " " * (n - i - 1)

        # Add the required number of `#` symbols to the staircase.
        staircase += "#" * (i + 1)

        # Add a newline character to the staircase.
        staircase += "\n"

    # Print the staircase to the console.
    print(staircase)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

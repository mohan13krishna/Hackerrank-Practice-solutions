

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0

    # Iterate over the apples and count the number of apples that fall on Sam's house.
    for apple in apples:
        # Calculate the position of the apple.
        apple_position = a + apple

        # If the apple falls on Sam's house, increment the count.
        if s <= apple_position <= t:
            apple_count += 1

    # Iterate over the oranges and count the number of oranges that fall on Sam's house.
    for orange in oranges:
        # Calculate the position of the orange.
        orange_position = b + orange

        # If the orange falls on Sam's house, increment the count.
        if s <= orange_position <= t:
            orange_count += 1

    # Print the count of apples and oranges that fall on Sam's house to the console.
    print(apple_count)
    print(orange_count)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

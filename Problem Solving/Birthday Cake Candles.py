#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    tallest_candle_height = 0

    # Initialize the number of tallest candles.
    number_of_tallest_candles = 0

    # Iterate over the candles and count the number of tallest candles.
    for candle_height in candles:
        if candle_height > tallest_candle_height:
            tallest_candle_height = candle_height
            number_of_tallest_candles = 1
        elif candle_height == tallest_candle_height:
            number_of_tallest_candles += 1

    # Return the number of tallest candles.
    return number_of_tallest_candles
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

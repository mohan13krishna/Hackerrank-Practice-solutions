#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    # Calculate the minimum and maximum sums.
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])

    # Print the minimum and maximum sums to the console.
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

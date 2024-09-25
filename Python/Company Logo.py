#author:mohan13krishna

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d = {}

    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    three_most_common = sorted(d.items(), key = lambda x: (-x[1], x[0]))[:3]

    for i in three_most_common:
        print(i[0], i[1])

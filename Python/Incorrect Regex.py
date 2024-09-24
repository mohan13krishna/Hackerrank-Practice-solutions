// author: mohan13krishna

import re
n = int(input())
for i in range(0,n):  
    try:
        input_ = input()
        a = (re.compile(input_))
        print(bool(a))
    except re.error:
        print('False')

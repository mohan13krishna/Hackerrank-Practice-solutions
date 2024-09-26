#author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re, sys
n = int(input())
for line in sys.stdin:
    remove_and = re.sub(r'(?<= )(&&)(?= )',"and",line)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )',"or",remove_and)
    print(remove_or,end='')

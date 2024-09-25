#author:mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

from itertools import groupby

for k, g in groupby(s):
    print((len(list(g)), int(k)), end=' ')

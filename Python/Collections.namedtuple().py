#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
columns=input().split()
marks=namedtuple('marks',columns)
avg=sum([int(marks(*input().split()).MARKS) for _ in range(n)])/n
print("{:.2f}".format(avg))

// author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    method, *val = input().split()
    getattr(d, method)(*val)

print(*d)

#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in product(A,B):
    print(i, end=" ")

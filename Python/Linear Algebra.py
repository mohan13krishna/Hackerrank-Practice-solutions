# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
a = []
for i in range(n):
    row = list(map(float,input().split()))
    a.append(row)

print(round(numpy.linalg.det(a),2))

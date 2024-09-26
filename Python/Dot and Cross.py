# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

A = numpy.array(A)
B = numpy.array(B)

print(numpy.dot(A, B))

# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

X, Y = map(int, input().split())
arr = numpy.array([input().split() for _ in range(X)], int)

sum_arr = numpy.sum(arr, axis = 0)
print(numpy.prod(sum_arr))

# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT'
import numpy

arr = list(map(int, input().split()))

print(numpy.zeros(arr, dtype = numpy.int))
print(numpy.ones(arr, dtype = numpy.int))

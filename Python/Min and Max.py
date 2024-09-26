# author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

arr = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
result = numpy.max(numpy.min(arr, axis=1))

print(result)

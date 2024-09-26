# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

x, y = map(int, input().split())

a = numpy.array([input().split() for _ in range(x)], int)
b = numpy.array([input().split() for _ in range(x)], int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))

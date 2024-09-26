# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

coefficients = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coefficients, x))

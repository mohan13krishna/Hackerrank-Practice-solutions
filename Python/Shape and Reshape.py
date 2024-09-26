# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
ar = list(map(int,input().split()))
np_ar = numpy.array(ar)
print(numpy.reshape(np_ar,(3,3)))

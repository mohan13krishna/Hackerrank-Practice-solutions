# author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

arr_dim = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(arr_dim[0])]
arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())

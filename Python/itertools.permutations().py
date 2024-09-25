#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

str1,n = input().split()
str1 = list(str1)
str1 = sorted(str1)
str1 = ''.join(str1)

for i in list(permutations(str1, int(n))):
 print(''.join(i))

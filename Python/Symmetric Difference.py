// author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

# Symmetric Difference
result = a.symmetric_difference(b)

# Output
for i in sorted(result):
    print(i)
    

# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT


k = int(input())

arr = list(map(int, input().split()))

my_set = set(arr)

print(((sum(my_set)*k)-(sum(arr)))//(k-1))

# author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n1 = int(input())
    set1 = set(map(int, input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))
    if set1.issubset(set2):
        print(True)
    else:
        print(False)

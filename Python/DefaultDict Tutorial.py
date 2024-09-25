#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import defaultdict

n, m = map(int, input().split())

groupA = defaultdict(list)
for i in range(n):
    groupA[input()].append(i+1)

for i in range(m):
    word = input()
    if word in groupA:
        print(*groupA[word])
    else:
        print(-1)

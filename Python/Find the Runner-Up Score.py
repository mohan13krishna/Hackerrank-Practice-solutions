#author:mohan13krishna


#input
n = int(input())
arr = list(map(int, input().split()))

#sort elements in descending order
arr.sort(reverse=True)

#find runner-up
runner_up = -101
for i in arr:
    if i<arr[0]:
        runner_up = i
        break

#output
print(runner_up)

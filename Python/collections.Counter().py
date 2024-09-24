//author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

numShoes = int(input())
shoeSizeList = list(map(int, input().split()))

numCustomers = int(input())

totalAmountEarned = 0

for i in range(numCustomers):
    custSize, custPrice = map(int, input().split())
    if custSize in shoeSizeList:
        totalAmountEarned += custPrice
        shoeSizeList.remove(custSize)

print(totalAmountEarned)

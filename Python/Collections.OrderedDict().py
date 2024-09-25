#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

d = OrderedDict()

for _ in range(n):
    item_name, net_price = input().rsplit(' ', 1)
    d[item_name] = d.get(item_name, 0) + int(net_price)

for item_name, net_price in d.items():
    print(item_name, net_price)

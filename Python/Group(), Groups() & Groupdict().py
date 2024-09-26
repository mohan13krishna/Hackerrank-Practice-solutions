#author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = input()
res = re.search(r'([A-Za-z0-9])\1',s)
if res == None:
    print(-1)
else:
    print(res.group(1))

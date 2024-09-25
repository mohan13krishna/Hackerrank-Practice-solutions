# author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/env python3

if __name__ == "__main__":
    st_num, sb_num = map(int, input().strip().split())
    scores = []
    
    for _ in range(sb_num):
        scores.append(map(float, input().strip().split()))
        
    for el in zip(*scores):
        print(sum(el)/sb_num)

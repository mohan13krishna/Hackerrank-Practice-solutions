#author:mohan13krishna



# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
eng_roll = set(map(int,input().split()))

n_fre = int(input())
fre_roll = set(map(int,input().split()))

total_roll = eng_roll.union(fre_roll)

print(len(total_roll))

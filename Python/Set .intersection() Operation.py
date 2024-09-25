#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

english_count = int(input())
english_set = set(map(int, input().split()))

french_count = int(input())
french_set = set(map(int, input().split()))

print(len(english_set.intersection(french_set)))

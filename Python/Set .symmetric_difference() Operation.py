# author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT



eng_subscriber = int(input())
eng_students = set(map(int, input().split()))

french_subscriber = int(input())
french_students = set(map(int, input().split()))

not_both = eng_students.symmetric_difference(french_students)
print(len(not_both))

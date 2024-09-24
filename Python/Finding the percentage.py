// author : mohan13krishna


n = int(input())
students = {}
for _ in range(n):
    name, *marks = input().split()
    scores = list(map(float, marks))
    students[name] = scores
query_name = input()

average = sum(students[query_name]) / len(students[query_name])
print("{:.2f}".format(average))

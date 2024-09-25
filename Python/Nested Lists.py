#author:mohan13krishna


n = int(input())
list_of_students = []
for _ in range(n):
    name = input()
    score = float(input())
    list_of_students.append([name, score])

list_of_scores = []
for student in list_of_students:
    list_of_scores.append(student[1])

second_lowest_score = sorted(list(set(list_of_scores)))[1]

result = []
for student in list_of_students:
    if student[1] == second_lowest_score:
        result.append(student[0])

print(*sorted(result), sep='\n')

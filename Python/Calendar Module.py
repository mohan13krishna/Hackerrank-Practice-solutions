#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar 

month, day, year = map(int, input().split()) 

dayNumber = calendar.weekday(year, month, day) 

days =["MONDAY", "TUESDAY", "WEDNESDAY", 
        "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"] 

print(days[dayNumber])

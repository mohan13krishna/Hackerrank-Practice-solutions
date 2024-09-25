#author:mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Python Program to design a Door Mat with Welcome written in the center

# Inputs for the program
n, m = map(int, input().split())

# Top section of the design
for i in range(1, n, 2):
    print((i * '.|.').center(m, '-'))

# Middle section of the design
print('WELCOME'.center(m, '-'))

# Bottom section of the design
for i in range(n - 2, 0, -2):
    print((i * '.|.').center(m, '-'))

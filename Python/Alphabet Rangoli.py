#author:mohan13krishna

def print_rangoli(size):
    # your code goes here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = []
    for i in range(size):
        s = "-".join(alpha[i:n])
        alphabets.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(alphabets[:0:-1]+alphabets))


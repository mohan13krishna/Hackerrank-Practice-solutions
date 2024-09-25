#author:mohan13krishna


def swap_case(s):
    swap_string = ""
    for letter in s:
        if letter.isupper():
            swap_string += letter.lower()
        else:
            swap_string += letter.upper()
    return swap_string


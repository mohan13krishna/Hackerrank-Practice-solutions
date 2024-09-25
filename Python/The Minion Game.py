#author:mohan13krishna

def minion_game(string): 
    stuart_score=0
    kevin_score=0
    vowels=['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score+=len(string)-i
        else:
            stuart_score+=len(string)-i

    if kevin_score>stuart_score:
        print("Kevin "+str(kevin_score))
    elif stuart_score>kevin_score:
        print("Stuart "+str(stuart_score))
    else:
        print("Draw")

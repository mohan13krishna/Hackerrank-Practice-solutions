# author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if letter in "aeiouy":
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))

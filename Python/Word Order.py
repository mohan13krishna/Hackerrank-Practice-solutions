// author: mohan13krishna

# Enter your code here. Read input from STDIN. Print output to STDOUT
words_dict = {}

num_words = int(input())

for _ in range(num_words):
    word = input()
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

print(len(words_dict))

for key in words_dict:
    print(words_dict[key], end=" ")

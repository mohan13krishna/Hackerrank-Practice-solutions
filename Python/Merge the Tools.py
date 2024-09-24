// author: mohan13krishna

def merge_the_tools(string, k):
    while string:
        substring = string[:k]
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print(''.join(result))
        string = string[k:]

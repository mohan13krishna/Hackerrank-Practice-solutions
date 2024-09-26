#author: mohan13krishna


import re
def fun(s):
    # return True if s is a valid email, else return False
    '''
    n=int(input())
    e=[]
    for _ in range[n]:
        e.append(input())
    user= e.split("@")[0]
    print(user)
    '''
    '''
    l = list(map(lambda x:x.split("@")[0], s))
    l = list(filter(lambda x: x > 10 and x < 80, l))
    '''
    #print(s)
    ptrn = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
    result = ptrn.match(s)
    #l = list(filter(lambda x:x.match(ptrn) , s))
    return result






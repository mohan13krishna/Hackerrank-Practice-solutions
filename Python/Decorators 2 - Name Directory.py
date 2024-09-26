#author: mohan13krishna




def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2])) #sort by age
        return [f(person) for person in people]
    return inner


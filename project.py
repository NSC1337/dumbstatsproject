import random

def monteCarlo(f, trials):
    sum = 0
    for i in range(trials):
        sum += f()
    return sum / trials

def birthdayTest(sample):
    def foo():
        A = set([])
        for i in range(sample):
            x = random.randint(1,365)
            if x in A:
                return True
            else:
                A.add(x)
        return False
    return foo


data = list(map(lambda y : monteCarlo(birthdayTest(y), 100), range(1,30)))

print(data)
print(data[23])

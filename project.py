import random

# Estimates probability of success of experiment().
def monteCarlo(experiment, trials):
    sum = 0
    for i in range(trials):
        sum += experiment()
    return sum / trials

# Returns whether or not people share a birthday in a random sample of size n.
def birthdayTest(n):
    def foo():
        A = set([])
        for i in range(n):
            x = random.randint(1,365)
            if x in A:
                return True
            else:
                A.add(x)
        return False
    return foo

# Creates a list of probabilities using monte carlo experiments
# ex: data[23] = P(a group of 23 people will have shared bdays)
data = list(map(lambda y : monteCarlo(birthdayTest(y), 100), range(1,30)))

print(data)
print(data[23])

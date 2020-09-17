import random


def shuffle(l):
    i = 0
    while i < len(l):
        ran_index = random.randint(0, len(l) - 1)
        l[i], l[ran_index] = l[ran_index], l[i]
        i += 1


l = [i for i in range(20)]
print(l)

shuffle(l)
print(l)

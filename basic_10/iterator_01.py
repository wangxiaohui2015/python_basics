my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration as e:
        break

print()

my_tuple = [1, 2, 3, 4, 5]
my_iter = iter(my_tuple)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration as e:
        break

print()

str = "This is a string."
my_iter = iter(str)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration as e:
        break

print()

dic = {'name': 'xiaoming', 'age': 24, 'sex': 'M'}
my_iter = iter(dic)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration as e:
        break

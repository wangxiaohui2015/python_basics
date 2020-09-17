def print_info(*args, **kwargs):
    print(args)
    print(kwargs)


t = 1, 2, 3
d = {'name': 'xiaoming', 'age': 30}
print_info(t, d)

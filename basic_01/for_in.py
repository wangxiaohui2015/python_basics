l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in l:
    print(i, end=" ")

print()
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in t:
    print(i, end=" ")

print()
s = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    print(i, end=" ")

print()
m = {'name': 'xiaoming', 'age': 20}
for k in m:
    print('%s -> %s' % (k, m[k]))
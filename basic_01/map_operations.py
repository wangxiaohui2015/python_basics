m = {'name': 'xiaoming', 'age': 20}
print(m)

m['sex'] = 'M'
print(m)

m.pop('sex')
print(m)

m['age'] = 30
print(m)

print(len(m))

for k in m:
    print('%s -> %s' % (k, m[k]))
s = "This is a testing string"
print(len(s))

print(s.count('s'))

print(s.index("t"))

print(s.startswith("This"))

print(s.startswith("TThis"))

print(s.endswith("string"))

print(s.endswith("stringG"))

print(s.find("testing"))

print(s.replace('testing', 'test'))

print(s)

s2 = '  This is a testing string  '
print(s2)
print(s2.strip())

s2_list = s2.split(' ')
print(s2_list)

print('#'.join(s2_list))
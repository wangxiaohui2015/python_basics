# No need to specify variable type
num = 10

# All digital data type can calculate each other
print(num + 2.5 + True)
print(num - 2.5 + False)
print(num * 2.5 + True)
print(num / 2.5 + False)
a = 1 + 2j
print(num * a)

# Use print method to show data type
print(type(1))
print(type(1.1))
print(type(True))
print(type(1+2j))
print(type('hello'))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({'name':'xiaoming', 'age':20}))
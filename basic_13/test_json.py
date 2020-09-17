import json

# Convert a dict to JSON string
dic1 = {'name': 'xiaoming', 'age': 20, 'sex': 'm'}
str = json.dumps(dic1)
print(str)
print(type(str))

# Convert a dict to formatted JSON string
str = json.dumps(dic1, sort_keys=True, indent=4, separators=(',', ': '))
print(str)
print(type(str))

# Convert a JSON string to dict
j = json.loads(str)
print(j)
print(type(j))

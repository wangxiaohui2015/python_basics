my_list = [2, 4, 5, 1, 3, 8, 10]
print(my_list)

# Append 12
my_list.append(12)
print(my_list)

# Append 7
my_list.append(7)
print(my_list)

# Insert 22 at index 2
my_list.insert(2, 22)
print(my_list)

# Delete the last data
my_list.pop()
print(my_list)

# Delete the data which index is 2
my_list.pop(2)
print(my_list)

# Delete the data which index is 1
del(my_list[1])
print(my_list)

# Assign a new data to the first element
my_list[0] = 0
print(my_list)

# Get the first element
print(my_list[1])

# The length of my_list
print(len(my_list))

# The max value of my_list
print(max(my_list))

# The min value of my_list
print(min(my_list))

# The count of elements which value is 10
print(my_list.count(10))

# Sort
my_list.sort()
print(my_list)

# Reverse sort
my_list.sort(reverse=True)
print(my_list)

# Reverse the my_list
my_list.reverse()
print(my_list)

# Clean my_list
my_list.clear()
print(my_list)
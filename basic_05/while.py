index = 0
num = 10
while index <= num:
    index += 1
    if index == 3:
        continue
    if index == 6:
        break
    print(index * 2)

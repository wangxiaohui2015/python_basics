l = [i ** 2 for i in range(10)]
print(l)

for i in l:
    if i == 49:
        print("i is 49, then break.")
        break
    if i == 4:
        print("i is 4, then continue")
        continue
    print(i)

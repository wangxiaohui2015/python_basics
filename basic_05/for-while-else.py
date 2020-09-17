l = [i ** 2 for i in range(10)]
print(l)


def check_num(num):
    for i in l:
        if i == num:
            print("%d is in list." % num)
            break
    else:
        print("%d is not in list." % num)


def check_num2(num):
    index = 0
    while index < len(l):
        if l[index] == num:
            print("%d is in list." % num)
            break
        index += 1
    else:
        print("%d is not in list." % num)


check_num(9)
check_num(19)

check_num2(9)
check_num2(19)

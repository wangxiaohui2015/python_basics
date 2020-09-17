def cal_num(*num):
    result = 0
    for i in num:
        result += i
    return result


print(cal_num(1, 2, 3))
print(cal_num(3, 4, 6, 8))

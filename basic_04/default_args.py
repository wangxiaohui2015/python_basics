def cal_num(num=10):
    if num <= 0:
        return 0
    result = 0
    for i in range(num):
        result += (i + 1)
    return result


print(cal_num(100))
print(cal_num())

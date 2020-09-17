def cal_num(num):
    if num <= 0:
        return 0
    result_sum = 0
    result_multi = 1
    for i in range(num):
        result_sum += (i + 1)
        result_multi *= (i + 1)
    return result_sum, result_multi


sum, multi = cal_num(10)
print(sum)
print(multi)

result = cal_num(10)
print(result)
print(type(result))

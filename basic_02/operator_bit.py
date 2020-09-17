num = 100
print(bin(num))
print("%o" % num)
print("%d" % num)
print("%x" % num)

num2 = 121
print(bin(num2))
print(bin(~num2))
print(bin(~num2 & 0b1111111111111111))
print(bin(num & num2))
print(bin(num | num2))
print(bin(num ^ num2))

print(num << 3)
print(num >> 2)
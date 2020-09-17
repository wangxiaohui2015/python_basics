import time

# Get current timestamp
print(time.time())

# Construct a struct_time object
t = time.localtime(1599094704.0659297)
print(t)

# Convert struct_time to string
t_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(t_str)

# Convert string to struct_time
t = time.mktime(time.strptime('2020-09-03 08:58:24', '%Y-%m-%d %H:%M:%S'))

# Minus
t1 = time.time()
time.sleep(2)
t2 = time.time()
print(t2 - t1)
import datetime
import time

# Get current timestamp
time_stamp = datetime.datetime.now().timestamp()
print(time_stamp)

# Construct a datetime object
t = datetime.datetime.fromtimestamp(time_stamp)
print(t)

# Convert datetime to string
t_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print(t_str)

# Convert string to datetime
t = datetime.datetime.strptime("2020-09-03 09:32:00.792264", "%Y-%m-%d %H:%M:%S.%f")
print(t)

# Minus
t1 = datetime.datetime.now()
time.sleep(2)
t2 = datetime.datetime.now()
print(t2 - t1)

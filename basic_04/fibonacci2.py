import time

# Used to store fibonacci temp data
fibonacci_tmp_data = {}


def fibonacci(n):
    """
    The original fibonacci function, no cache
    :param n: A integer number
    :return: Fibonacci result
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_2(n):
    """
    The enhanced fibonacci function, use cache
    :param n: A integer number
    :return: Fibonacci result
    """
    if n in fibonacci_tmp_data:
        return fibonacci_tmp_data[n]
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_2(n - 1) + fibonacci_2(n - 2)
    fibonacci_tmp_data[n] = result
    return result


num = 38
start = time.time()
print("fibonacci(%d) = %d" % (num, fibonacci(num)))
end = time.time()
print("Spend %.2f seconds." % (end - start))
print()
start = time.time()
print("fibonacci_2(%d) = %d" % (num, fibonacci_2(num)))
end = time.time()
print("Spend %.2f seconds." % (end - start))
print()
num = 1000
start = time.time()
print("fibonacci_2(%d) = %d" % (num, fibonacci_2(num)))
end = time.time()
print("Spend %.2f seconds." % (end - start))
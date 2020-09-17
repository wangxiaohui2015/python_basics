def divide(num1, num2):
    result = 0
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print("ZeroDivisionError happened, %r" % e)
    except Exception as e:
        print("Exception happened, %r" % e)
    else:
        print("No error happened.")
    finally:
        print("Finally statement.")
    return result


print(divide(4, 2))
print()
print(divide(4, 0))
print()
print(divide(4, 'abc'))

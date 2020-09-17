class MyError(Exception):
    pass


try:
    print("Before raise error.")
    raise MyError('This is a testing error.')
    print("After raise error.")
except MyError as e:
    print("MyError occurred, %r" % e)
finally:
    print("Finally statement.")

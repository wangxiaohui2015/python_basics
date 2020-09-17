class MyList:
    def __init__(self, data=[]):
        self.__data = data
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__data) == 0 or self.__index >= len(self.__data):
            raise StopIteration
        element = self.__data[self.__index]
        self.__index += 1
        return element


my_list = MyList("Hello world!")
for i in my_list:
    print(i, end=" ")

print()

my_list = MyList([1, 2, 3, 4, 5])
my_iter = iter(my_list)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration as e:
        break

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say_hi(self):
        print("Hi, my name is %s, I'm %d years old." % (self.__name, self.__age))
        self._sing()

    def _sing(self):
        print("%s is sing." % self.__name)


p = Person('xiaoming', 20)
p.say_hi()

# Another way to invoke print method
p._sing()
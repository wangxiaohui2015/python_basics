class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi, my name is %s, I'm %d years old." % (self.name, self.age))


p = Person('xiaoming', 20)
p.say_hi()
p2 = Person('Bobbi', 30)
p2.say_hi()
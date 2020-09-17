class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("%s is walking..." % self.name)


class Person(Animal):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def say_hi(self):
        print("Hi, my name is %s, I'm %d years old, my country is %s" % (self.name, self.age, self.country))


p = Person("xiaoming", 20, "China")
p.say_hi()
p.walk()

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("Animal %s is walking." % self.name)


class Person(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print("Person %s is walking." % self.name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print("Dog %s is walking." % self.name)


def walk_now(animal):
    animal.walk()


p = Person("xiaoming")
d = Dog("ahuang")

walk_now(p)
walk_now(d)

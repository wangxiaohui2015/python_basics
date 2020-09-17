class Person:
    instance_obj = None

    def __new__(cls, *args, **kwargs):
        if cls.instance_obj is None:
            cls.instance_obj = super().__new__(cls, *args, **kwargs)
        return cls.instance_obj


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()

print(id(p1))
print(id(p2))
print(id(p3))
print(id(p4))

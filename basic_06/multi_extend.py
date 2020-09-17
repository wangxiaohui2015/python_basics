class A:
    def say_hi(self):
        print("Hi this is A.")


class B:
    def say_hi(self):
        print("Hi this is B.")


class C(A, B):
    pass


class D(A, B):
    def say_hi(self):
        print("Hi this is D.")


c = C()
c.say_hi()
print(C.__mro__)

d = D()
d.say_hi()
print(D.__mro__)

import random
import string

# float_n is a float number in [0,1)
float_n = random.random()
print(float_n)

# int_n is a int number in [1, 10]
int_n = random.randint(1, 10)
print(int_n)

# float_n is a float number in [1.2, 2.8]
float_n = random.uniform(1.2, 2.8)
print(float_n)

# Random choice
print(random.choice("abcdefghi"))
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice(('xiaoming', 'xiaohong', 'ahuang', 'tom', 'jerry')))

# Random range in [1, 10) with step 2
print(random.randrange(1, 10, 2))

# Shuffle a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(l)
print(l)


def generate_password():
    while True:
        lower_l = random.sample(string.ascii_lowercase, random.randint(1, 5))
        upper_l = random.sample(string.ascii_uppercase, random.randint(1, 5))
        punc_l = random.sample(string.punctuation, random.randint(1, 5))
        digit_l = random.sample(string.digits, random.randint(1, 5))
        password_l = lower_l + upper_l + punc_l + digit_l
        random.shuffle(password_l)
        password_str = ''.join(password_l)
        if len(password_str) >= 12:
            return password_str
        else:
            print("Generate password again...")


password = generate_password()
print(password)

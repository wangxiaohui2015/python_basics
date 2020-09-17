#!/bin/python

import random

MIN = 1
MAX = 100


def get_random_num():
    return random.randint(MIN, MAX)


def main():
    for i in range(5):
        num = get_random_num()
        print(num)


if __name__ == '__main__':
    main()

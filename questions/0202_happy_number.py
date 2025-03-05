#!/usr/bin/env python

import time

def myIsHappy(n: int) -> bool:

    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(num) **2 for num in str(n)])

    return n == 1

def otherIsHappy(n: int) -> bool:
    s = []
    while True:
        if n == 1:
            return True
        i = 0
        while n:
            i = i + (n % 10) **2
            n = n // 10
        if i in s:
            return False
        s.append(i)
        n = i

def main():

    tests = [
        19,
        2,
        7
    ]

    for (number, test) in enumerate(tests):
        start_time = time.time()
        my_result = myIsHappy(test)
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - start_time)
        )

        start_time = time.time()
        other_result = otherIsHappy(test)
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - start_time)
        )

if __name__ == "__main__":
    main()

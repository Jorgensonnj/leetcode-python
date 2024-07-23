#!/usr/bin/env python

import time

def myGcdOfStrings(str1: str, str2: str) -> str:

    (small, large) = (str1, str2) if len(str1) <= len(str2) else (str2, str1)

    copy = small
    while len(small) > 0:
        temp = large.replace(small, "")
        if len(temp) == 0 and len(copy.replace(small, "")) == 0:
            return small
        else:
            small = small[:-1]

    return small

def otherGcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ''
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        return otherGcdOfStrings(str1[len(str2):], str2)
    return otherGcdOfStrings(str1, str2[len(str1):])

def main():

    tests = [
        ("ABCABC", "ABC"),
        ("ABABAB", "ABAB"),
        ("ABA", "AB"),
        ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"),
    ]

    for (number, test) in enumerate(tests):
        my_start_time = time.time()
        my_result = myGcdOfStrings(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - my_start_time)
        )

        other_start_time = time.time()
        other_result = otherGcdOfStrings(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - other_start_time)
        )

if __name__ == "__main__":
    main()

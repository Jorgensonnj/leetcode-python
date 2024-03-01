#!/usr/bin/env python

import time

def canConstruct( ransomNote: str, magazine: str) -> bool:

    dictionary = {}
    for character in magazine:
        if character in dictionary:
            dictionary[character] = dictionary[character] + 1
        else:
            dictionary[character] = 1

    for character in ransomNote:
        if character in dictionary:
            if dictionary[character] == 1:
                dictionary.pop(character)
            else:
                dictionary[character] = dictionary[character] - 1
        else:
            return False
    return True

def main():

    tests = [
        ("a", "b"),
        ("aa", "ab"),
        ("aa", "aab")
    ]

    for (number, test) in enumerate(tests):
        start_time = time.time()
        result = canConstruct(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(result) +
            " Time: {:10.9f}".format(time.time() - start_time)
        )

if __name__ == "__main__":
    main()

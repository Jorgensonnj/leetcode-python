#!/usr/bin/env python

import time

def myWordPattern(pattern: str, s: str) -> bool:

    tokens = s.split(" ")

    pattern_middle = len(pattern) / 2
    tokens_middle  = len(tokens) / 2
    #print("pm: {}, sm: {}".format(pattern_middle, tokens_middle))

    if pattern_middle != tokens_middle:
        return False

    stack = []
    for index in range(len(pattern)):
        value = pattern[index] + tokens[index]

        #print(value)
        print(tokens_middle)

        if (0 < tokens_middle):
            stack.append(value)
            tokens_middle -= 1
        else:
            if value != stack.pop():
                return False

    return True


def main():

    tests = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("aabaa", "cat cat fish cat cat"),
    ]

    for (number, test) in enumerate(tests):
        start_time = time.time()
        result = myWordPattern(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(result) +
            " Time: {:10.9f}".format(time.time() - start_time)
        )

if __name__ == "__main__":
    main()

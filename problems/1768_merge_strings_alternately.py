#!/usr/bin/env python

import time

def myMergeAlternately(word1: str, word2: str) -> str:
    result = ""
    i = 0
    while i < len(word1) or i < len(word2):
        result += word1[i] if i < len(word1) else ""
        result += word2[i] if i < len(word2) else ""
        i += 1

    return result

def otherMergeAlternately(word1: str, word2: str) -> str:
    result = []
    len1 = len(word1)
    len2 = len(word2)

    i = 0
    j = 0

    while i < len1 and j < len2:
        result.append(word1[i])
        result.append(word2[i])

        i += 1
        j += 1

    if i < len1:
        result.append(word1[i:])
    if j < len2:
        result.append(word2[j:])
    return ''.join(result)

def main():

    tests = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("aabaa", "cat cat fish cat cat"),
    ]

    for (number, test) in enumerate(tests):
        my_start_time = time.time()
        my_result = myMergeAlternately(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - my_start_time)
        )

        other_start_time = time.time()
        other_result = otherMergeAlternately(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - other_start_time)
        )

if __name__ == "__main__":
    main()

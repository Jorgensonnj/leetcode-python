#!/usr/bin/env python

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

    for test in tests:
        result = canConstruct(test[0], test[1])
        print("Result: " + str(result))


if __name__ == "__main__":
    main()

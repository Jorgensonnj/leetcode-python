#!/usr/bin/env python

import time

def myIsValid( s: str) -> bool:

    if len(s) <= 1:
        return False

    stack = []
    for character in s:
        match character:
            case "{":
                stack.append(character)
            case "[":
                stack.append(character)
            case "(":
                stack.append(character)
            case "}":
                if (stack and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            case "]":
                if (stack and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
            case ")":
                if (stack and stack[-1] == "("):
                    stack.pop()
                else:
                    return False

    return not stack

def otherIsValid( s: str) -> bool:
    approved_char_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in s:
        if char in approved_char_dict:
            stack.append(char)
        elif char in approved_char_dict.values():
            if not stack or approved_char_dict[stack.pop()] != char:
                return False

    return not stack  # If the stack is empty, all parentheses are matched

def main():

    tests = [
        "()",
        "{}()[]",
        "[)",
        "()()((()))"
    ]

    for (number, test) in enumerate(tests):
        my_start_time = time.time()
        my_result = myIsValid(test)
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - my_start_time)
        )

        other_start_time = time.time()
        other_result = otherIsValid(test)
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - other_start_time)
        )

if __name__ == "__main__":
    main()

#!/usr/bin/env python

import time

def myContainsNearbyDuplicate(nums: List[int], k: int) -> bool:
    return False

def otherContainsNearbyDuplicate(nums: List[int], k: int) -> bool:
    return False


def main():

    tests = [
        ([1,2,3,1], 3),
        ([1,0,1,1], 1),
        ([1,2,3,1,2,3], 2),
    ]

    for (number, test) in enumerate(tests):
        my_start_time = time.time()
        my_result = myContainsNearbyDuplicate(test.0, test.1)
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - my_start_time)
        )

        other_start_time = time.time()
        other_result = otherContainsNearbyDuplicate(test.0, test.1)
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - other_start_time)
        )

if __name__ == "__main__":
    main()

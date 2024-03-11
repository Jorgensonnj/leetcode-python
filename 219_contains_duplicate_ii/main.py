#!/usr/bin/env python

# source
# https://leetcode.com/problems/contains-duplicate-ii/description

import time
from typing import List

def myContainsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dictionary = {}
    for (index, num) in enumerate(nums):
        if dictionary.get(num) is None:
            dictionary[num] = index
        elif abs(dictionary[num] - index) <= k:
            return True
        else:
            dictionary[num] = index

    return False

# other submission
# https://leetcode.com/problems/contains-duplicate-ii/submissions/1200964325

def otherContainsNearbyDuplicate(nums: List[int], k: int) -> bool:
    d = dict()
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        elif abs(d[nums[i]] - i) <= k:
            return True
        else:
            d[nums[i]] = i
    return False


def main():

    tests = [
        ([1,2,3,1],     3),
        ([1,0,1,1],     1),
        ([1,2,3,1,2,3], 2),
    ]

    for (number, test) in enumerate(tests):
        my_start_time = time.time()
        my_result = myContainsNearbyDuplicate(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(my_result) +
            " Time: {:10.9f}".format(time.time() - my_start_time)
        )

        other_start_time = time.time()
        other_result = otherContainsNearbyDuplicate(test[0], test[1])
        print(
            "Test: " + str(number) +
            " Result: " + str(other_result) +
            " Time: {:10.9f}".format(time.time() - other_start_time)
        )

if __name__ == "__main__":
    main()

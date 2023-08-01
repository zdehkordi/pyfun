import pytest

from collections import defaultdict

def func(nums: list[int]) -> int:
    numsS = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in numsS:
            length = 0
            while n + length in numsS:
                length += 1
            longest = max(longest, length)

    return longest



def test_():
    assert func([100,4,200,1,3,2]) == 4

def test__():
    assert func([0,3,7,2,5,8,4,6,0,1]) == 9

def test___():
    assert func([]) == 0
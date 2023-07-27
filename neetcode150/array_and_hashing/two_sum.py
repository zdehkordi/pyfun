import pytest

def func(nums: list[int], target: int) -> list[int]:
    m = {}

    for i in range(len(nums)):
        c = target - nums[i]
        if c in m:
            return [m[c], i]

        m[nums[i]] = i 

    return []

def test_base():
    nums, target = [1,2], 5
    assert func(nums, target) == []

def test_ez():
    nums, target = [1,2], 3
    assert func(nums, target) == [0,1]

def test_ex1():
    nums, target = [2,7,11,15], 9
    assert func(nums, target) == [0,1]

def test_ex2():
    nums, target = [3,2,4], 6
    assert func(nums, target) == [1,2]

def test_ex3():
    nums, target = [3,3], 6
    assert func(nums, target) == [0,1]
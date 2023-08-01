import pytest

def func(nums: list[int], target: int) -> list[int]:
    m = {}

    for i in range(len(nums)):
        if nums[i] in m:
            return [m[nums[i]], i]
        
        m[target - nums[i]] = i

def test_():
    nums, target = [2,7,11,15], 9
    assert func(nums, target) == [0,1]

def test__():
    nums, target = [3,2,4], 6
    assert func(nums, target) == [1,2]

def test___():
    nums, target = [3,3], 6
    assert func(nums, target) == [0,1]

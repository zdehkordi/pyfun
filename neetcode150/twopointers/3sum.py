import pytest

def func(nums: list[int]) -> list[list[int]]:
    res = set()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(x) for x in res]

def func(nums: list[int]) -> list[list[int]]:
    s = set(nums)
    res = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)-1):
            if -nums[i]-nums[j] in s:
                toad = sorted([-nums[i]-nums[j], nums[j], nums[i]])
                if toad not in res:
                    res.append(toad)
    return res



def test_():
    nums = [-1,0,1,2,-1,-4]
    assert (
        sorted([sorted(x) for x in func(nums)]) 
        == 
        sorted([sorted(x) for x in [[-1,-1,2],[-1,0,1]]])
    )

def test__():
    nums = [0,1,1]
    assert func(nums) == []

def test___():
    nums = [0,0,0]
    assert func(nums) == [[0,0,0]]
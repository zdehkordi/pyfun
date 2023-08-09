import pytest

def func(nums: list[int]) -> int:
    m = max(nums)

    i = nums.index(m)

    return 0 if i == len(nums)-1 else nums[i+1]

def func(nums: list[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) -1

    while l <= r:
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res

def test_():
    nums = [3,4,5,1,2]
    assert func(nums) == 1

def test__():
    nums = [4,5,6,7,0,1,2]
    assert func(nums) == 0
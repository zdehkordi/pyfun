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
    nums.sort()
    ans = []

    for i, a in enumerate(nums):
        if a > 0: break
        if i > 0 and a == nums[i-1]: continue

        l, r = i+1, len(nums)-1

        while l < r:
            diff = a + nums[l] + nums[r]
            if diff  == 0:
                ans.append([a, nums[l], nums[r]])
                l += 1
                r -= 1

                while nums[l] == nums[l-1] and l < r:
                    l += 1

            elif diff > 0:
                r -= 1
            else:
                l += 1

        i += 1

    return ans
        
            



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
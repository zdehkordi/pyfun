from itertools import accumulate
import pytest

from functools import reduce

def func(nums: list[int]) -> list[int]:
    """O(n^2)"""
    ans = []
    for i in range(len(nums)):
        arr = nums[:]
        arr[i] = 1
        ans.append(reduce(lambda x,y: x*y, arr))
    return ans

def func(nums: list[int]) -> list[int]:
    """O(n), but uses division..."""
    if sum(1 for x in nums if x == 0) > 1:
        return [0] * len(nums)
    if sum(1 for x in nums if x == 0) == 1:
        p = reduce(lambda x,y: x*y, [x for x in nums if x != 0])
        return [p if x == 0 else 0 for x in nums]
    else:
        p = reduce(lambda x,y: x*y, [x for x in nums if x != 0])
        return [p // x for x in nums]

def func(nums: list[int]) -> list[int]:
    """O(n)"""
    pre = list(accumulate(nums, lambda x,y: x*y))
    post = list(accumulate(nums[::-1], lambda x,y: x*y))[::-1]
    n = len(nums)

    return [(pre[i-1] if i-1 >= 0 else 1) * (post[i+1] if i+1 <= n-1 else 1) for i in range(n)]
        
def func(nums: list[int]) -> list[int]:
    """O(n), O(1), genius"""
    ans, suf, pre = [1]*len(nums), 1, 1
    for i in range(len(nums)):
        ans[i] *= pre               # prefix product from one end
        pre *= nums[i]
        ans[-1-i] *= suf            # suffix product from other end
        suf *= nums[-1-i]
    return ans


def test_():
    """[1 * 2*3*4, 1 *3*4, 1*2 * 4, 1*2*3 * 1]"""
    nums = [1,2,3,4]
    assert func(nums) == [24,12,8,6]

def test__():
    nums = [-1,1,0,-3,3]
    assert func(nums) == [0,0,9,0,0]

def test_two_zeroes():
    nums = [1,0,0]
    assert func(nums) == [0,0,0]
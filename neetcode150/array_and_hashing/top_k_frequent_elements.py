import pytest

from collections import Counter, defaultdict

def func(nums: list[int], k: int) -> list[int]:
    return [x[0] for x in Counter(nums).most_common()[:k]]

def func(nums: list[int], k: int) -> list[int]:
    """O(n + nlogn + k), n = len(nums)"""
    m = defaultdict(int)

    for n in nums:
        m[n] += 1

    sm = sorted(m.items(), key=lambda d: d[1], reverse=True)

    return [x[0] for x in sm[:k]]

def test_():
    nums, k = [1,1,1,2,2,3], 2
    assert func(nums, k ) ==  [1,2]

def test__():
    nums, k = [1], 1
    assert func(nums, k ) ==  [1]
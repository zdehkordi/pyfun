import pytest

def containsDuplicate(nums: list[int]) -> bool:
    """O(n + 1 + 1) == O(n)"""
    return len(set(nums)) != len(nums)

def test_basic():
    nums = []
    assert containsDuplicate(nums) == False

def test_one():
    nums = [1, 1]
    assert containsDuplicate(nums) == True

def test_ex1():
    nums = [1,2,3,1]
    assert containsDuplicate(nums) == True

def test_ex2():
    nums = [1,2,3,4]
    assert containsDuplicate(nums) == False

def test_ex3():
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert containsDuplicate(nums) == True
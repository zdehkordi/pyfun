import pytest

def remove_element(nums: list[int], val: int) -> int:
    """O(n^2)"""
    i = 0

    while i < len(nums): # O(n)
        if nums[i] == val:
            nums.remove(val) # O(n)
        else:
            i += 1
    
    return len(nums) # O(1)

def remove_element(nums: list[int], val: int) -> int:
    i, j = 0, len(nums) - 1

    if len(nums) == 0:
        return 0

    while i < j:
        if nums[i] == val:
            while nums[j] == val:
                j -= 1

            nums[i] = nums[j]
            j -= 1

        i += 1

    return i + 1

def remove_element(nums: list[int], val: int) -> int:
    """
    n = len(nums), k = len([i for i in nums if i != val])
    O(n + k)
    """
    rtn = []

    for i in nums: # O(n)
        if i != val:
            rtn.append(i) # O(1) * k

    nums.clear() # O(n)
    nums.extend(rtn) # O(k)

    return len(rtn) # O(1)



def test_none():
    nums = []
    assert remove_element(nums, 1) == 0
    assert nums == []

def test_one():
    nums = [1]
    assert remove_element(nums, 1) == 0
    assert nums == []


def test_ex1():
    nums = [3,2,2,3]
    assert remove_element(nums, 3) == 2
    assert sorted(nums[:2]) == sorted([2, 2])

def test_ex2():
    nums = [0,1,2,2,3,0,4,2]
    assert remove_element(nums, 2) == 5
    assert sorted(nums[:5]) == sorted([0,1,4,0,3])
    
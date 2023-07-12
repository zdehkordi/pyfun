import pytest

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """O((m+n)log(m+n))"""
    rtn = sorted(nums1[:m] + nums2)
    return rtn

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """O(m+n)"""
    rtn = []
    part1 = nums1[:m]

    m_i, n_i = 0, 0

    while m_i + n_i < m + n:
        if m_i < m and n_i < n:
            if part1[m_i] < nums2[n_i]:
                rtn.append(part1[m_i])
                m_i += 1
            else:
                rtn.append(nums2[n_i])
                n_i += 1
        elif m_i < m:
            rtn.append(part1[m_i])
            m_i += 1
        elif n_i < n:
            rtn.append(nums2[n_i])
            n_i += 1

    return rtn


def test_empty_n():
    assert merge([1], 1, [], 0) == [1]

def test_empty_m():
    assert merge([0], 0, [1], 1) == [1]

def test_two_entries():
    assert merge([1, 0], 1, [2], 1) == [1, 2]

def test_ordered():
    assert merge([1,2,3,0,0,0], 3, [4,5,6], 3) == [1,2,3,4,5,6]

def test_gold():
    assert merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]

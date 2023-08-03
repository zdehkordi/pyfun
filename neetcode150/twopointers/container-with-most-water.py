import pytest

def func(height: list[int]) -> int:
    area = 0

    for j in range(len(height)-1):
        for k in range(j+1, len(height)):
            w = k-j
            h = min(height[j], height[k])

            area = max(area, w*h)

    return area

def func(height: list[int]) -> int:
    j, k = 0, len(height)-1

    a = 0

    while j < k:
        w = k-j
        h = min(height[j], height[k])

        a = max(a, w*h)

        if height[j] > height[k]:
            k -= 1
        else:
            j += 1

    return a


def test_():
    height = [1,1]
    assert func(height) == 1

def test__():
    height = [1,8,6,2,5,4,8,3,7]
    assert func(height) == 49

def test___():
    height = [1,3,2,5,25,24,5]
    assert func(height) == 24
    
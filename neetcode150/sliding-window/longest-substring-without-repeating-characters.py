import pytest

def func(s: str) -> int:
    size = 0
    l = 0
    seen = set()

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[i])
        size = max(size, i - l + 1)

    return size

def test_():
    s = "abcabcbb"
    assert func(s) == 3

def test__():
    s = "bbbbb"
    assert func(s) == 1

def test___():
    s = "pwwkew"
    assert func(s) == 3
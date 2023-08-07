from collections import defaultdict
import pytest

def func(s: str, k: int) -> int:
    m = defaultdict(int)
    c = 0
    l = 0
    for r in range(len(s)):

        m[s[r]] += 1

        while r-l+1 - max(m.values()) > k:
            m[s[l]] -= 1
            l += 1


        c = max(c, r-l+1)
        
    
    return c


def test_____():
    s,k = "AAAB",0
    assert func(s, k) == 3

def test____():
    s,k = "AAAB",1
    assert func(s, k) == 4

def test_():
    s,k = "ABAB",2
    assert func(s, k) == 4

def test__():
    s,k = "AABABBA",1
    assert func(s,k) == 4

def test___():
    s,k = "AABABBBA",1
    assert func(s,k) == 5
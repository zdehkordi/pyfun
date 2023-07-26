import pytest

from collections import Counter

def isAnagram(s: str, t: str) -> bool:
   return Counter(s) == Counter(t)

def test_ex1():
    s, t = "anagram", "nagaram"
    assert isAnagram(s, t) == True

def test_ex2():
    s, t = "rat", "car"
    assert isAnagram(s, t) == False


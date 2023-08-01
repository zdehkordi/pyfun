import pytest

def func(s: str) -> bool:
    data = [c.lower() for c in s if c.isalnum()]

    st = "".join(data)
    
    return st == st[::-1]

def isAlphaNum(s: str) -> bool:
    return (
        ord('a') <= ord(s) <= ord('z') or
        ord('A') <= ord(s) <= ord('Z') or
        ord('0') <= ord(s) <= ord('9')
    )

def func(s: str) -> bool:
    l,r = 0, len(s) - 1

    while l < r and r > l:
        while not isAlphaNum(s[l]) and l < r:
            l += 1

        while not isAlphaNum(s[r]) and r > l:
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1

    return True


def test_():
    s = "A man, a plan, a canal: Panama"
    assert func(s) == True

def test__():
    s = "race a car"
    assert func(s) == False

def test___():
    s = "0P"
    assert func(s) == False
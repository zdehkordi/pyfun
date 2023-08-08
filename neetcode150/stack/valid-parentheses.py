import pytest

def func(s: str) -> bool:
    st = []

    for c in s:
        if c in ['(', '[', '{']:
            st.append(c)
        else:
            if len(st) == 0:
                return False
            
            last = st.pop()
            
            if c == ')' and last != '(':
                return False
            elif c == ']' and last != '[':
                return False
            elif c == '}' and last != '{':
                return False

    return len(st) == 0

def test________():
    s = "("
    assert func(s) == False

def test_():
    s = "()"
    assert func(s) == True

def test__():
    s = "()[]{}"
    assert func(s) == True

def test____():
    s = "(]"
    assert func(s) == False

def test_____():
    s = "([{}])"
    assert func(s) == True


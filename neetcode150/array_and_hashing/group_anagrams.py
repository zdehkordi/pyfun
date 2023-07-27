import pytest

from collections import defaultdict, Counter

def func(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for s in strs:
        ss = "".join(sorted(s))

        groups[ss].append(s)

    return list(groups.values())


def test_base():
    strs = [""]
    assert func(strs) == [[""]]

def test_base2():
    strs = ["a"]
    assert func(strs) == [["a"]]

def test_2():
    strs = ["ab", "bc"]
    assert func(strs) == [["ab"], ["bc"]]

def test_1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    groups = [["bat"],["nat","tan"],["ate","eat","tea"]]
    res = func(strs)
    assert len(res) == len(groups)
    assert set(len(x) for x in res) == set(len(x) for x in groups)
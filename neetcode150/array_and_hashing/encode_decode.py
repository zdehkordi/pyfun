import pytest

def encode(strs: list[str]) -> str:
    res = []
    for s in strs:
        res.append(f"{len(s)}#{s}")
    return "".join(res)

def decode(s: str) -> list[str]:
    if s:
        d = s.find("#")
        l = int(s[0:d])
        sub = s[d+1:d+1+l]
        return [sub] + decode(s[d+1+l:])
    else: 
        return []
    

def test_():
    strs = ["l#i2132t","####21313code","#lov##e;","1100you##1"]
    assert decode(encode(strs)) == strs
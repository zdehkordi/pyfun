import pytest

import math

def func(prices: list[int]) -> int:
    profit=0
    
    mi=math.inf
    ma=0

    for i in range(0, len(prices)-1):
        if min(mi, prices[i]) == prices[i]:
            mi = prices[i]
            ma = 0
        
        ma = max(ma, prices[i+1])

        profit = max(profit, ma-mi)

    return profit

def func(prices: list[int]) -> int:
    profit=0
    low=prices[0]
    
    for price in prices:
        if price < low:
            low = price
        profit = max(profit, price - low)

    return profit

    

def test_():
    prices = [7,1,5,3,6,4]
    assert func(prices) == 5

def test__():
    prices = [7,6,4,3,1]
    assert func(prices) == 0
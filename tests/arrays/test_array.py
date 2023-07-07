import pytest

import numpy as np

def test_allocate_1():
    a = np.zeros(1, dtype='int')

    assert a == np.array([0])

def test_allocate_2():
    a = np.zeros(2, dtype='int')

    assert np.array_equal(a, np.array([0] * 2))

def test_allocate_powers_of_2():
    highest_power = 10

    for i in range(1, highest_power + 1):
        a = np.zeros(2*i, dtype='int')

        assert np.array_equal(a, np.array([0] * 2*i))
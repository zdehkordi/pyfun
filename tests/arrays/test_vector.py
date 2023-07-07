import pytest

import numpy as np

from pyfun.arrays.vector import vector, array

def test_allocate_array_of_type():
    a = array(int, 1)

def test_get_length_of_array():
    a = array(int, 1)
    assert a.length == 1

def test_get_val_of_array():
    a = array(int, 1)
    assert a[0] == 0

def test_set_val_of_array():
    a = array(int, 1)
    a[0] = 1
    assert a[0] == 1

def test_make_with_vals():
    a = array.make(int, 1, 2, 3)
    assert a[0] == 1
    assert a[2] == 3

def test_can_make_vector():
    v = vector()

def test_has_set_size():
    v = vector()

    assert v.size() == 0
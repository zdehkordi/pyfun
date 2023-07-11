import pytest

import numpy as np

from pyfun.arrays.vector import vector, array

def test_allocate_array_of_type():
    a = array(int, 1)

def test_get_length_of_array():
    a = array(int, 1)
    assert a.length == 1

def test_get_and_set_val_of_array():
    a = array(int, 1)
    assert a[0] == None
    a[0] = 1
    assert a[0] == 1

def test_make_with_vals():
    a = array.make(int, 1, 2, 3)
    assert a[0] == 1
    assert a[2] == 3

def test_can_make_vector():
    v = vector(int)

def test_has_size():
    v = vector(int)

    assert v.size() == 0

def test_has_size_with_elements():
    v = vector(int)

    v.add(1)

    assert v.size() == 1

def test_capactiy():
    v = vector(int, 1)
    assert v.capacity() == 1

    v = vector(int, 32)
    assert v.capacity() == 32

def test_is_empty():
    v = vector(int)
    assert v.is_empty() == True

    v.add(1)

    assert v.is_empty() == False
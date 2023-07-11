from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')

class array(Generic[T]):
    """dum arrays!"""
    def __init__(self, cls: type[T], length: int) -> None:
        self.__data: list[T] = [None] * length
        self.length = length

    def __getitem__(self, key: int) -> T:
        return self.__data[key]
    
    def __setitem__(self, key: int, val: T) -> None:
        self.__data[key] = val
    
    @staticmethod
    def make(cls: type[T], *args: T) -> array[T]:
        a = array(cls, len(args))
        for i in range(len(args)):
            a[i] = args[i]
        return a

class vector(Generic[T]):
    """generic vectors, aka 'list'"""
    def __init__(self, cls: type[T], size: int = 1) -> None:
        self.__data = array(cls, size)

    def add(self, val: T) -> None:
        self.__data[0] = val

    def size(self) -> int:
        return sum(1 for i in range(self.__data.length) if self.__data[i] is not None)
    
    def capacity(self) -> int:
        return self.__data.length

    def is_empty(self) -> bool:
        return all(self.__data[i] is None for i in range(self.__data.length))
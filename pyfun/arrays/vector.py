from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')

class array:
    """dum arrays!"""
    def __init__(self, cls: type[T], length: int) -> None:
        self.__data: list[T] = [cls()] * length
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
    def __init__(self) -> None:
        pass

    def size(self) -> int:
        return 0
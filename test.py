from py_bitmask26 import Bitmask26 as PyBitmask26
from bitmask26 import Bitmask26

from sys import getsizeof

def _check_le(cls, w1: str, w2: str):
    b1 = cls(w1)
    b2 = cls(w2)
    ret = b1 <= b2
    print()
    print(f"{w1:10} <= {w2:>10}")
    print(f"{repr(b1):10} {repr(b2):10} {ret}")
    return ret

def _check_ge(cls, w1: str, w2: str):
    b1 = cls(w1)
    b2 = cls(w2)
    ret = b1 >= b2
    print()
    print(f"{w1:10} >= {w2:>10}")
    print(f"{repr(b1):10} {repr(b2):10} {ret}")
    return ret


def check(cls):
    print()
    print()
    print('Testing', cls)

    assert _check_le(cls, 'flee', 'eefl') == True
    assert _check_le(cls, 'elf', 'eefl')  == True
    assert _check_le(cls, 'left', 'eefl') == False
    assert _check_le(cls, 'cap', 'eefl')  == False
    assert _check_le(cls, 'fell', 'eefl') == True

    assert _check_ge(cls, 'eefl', 'flee') == True
    assert _check_ge(cls, 'eefl', 'elf')  == True
    assert _check_ge(cls, 'eefl', 'left') == False
    assert _check_ge(cls, 'eefl', 'cap')  == False
    assert _check_ge(cls, 'eefl', 'fell') == True

    print()
    for w in ['apple', 'orange', 'grape', 'banana']:
        b1 = cls(w)
        b2 = cls(w)
        s = frozenset(w)
        print(f"{repr(b1):10} {repr(b2):10} {''.join(sorted(s)):10}")
        print(f"{getsizeof(b1):10} {getsizeof(b2):10} {getsizeof(s):10}")

check(PyBitmask26)
check(Bitmask26)

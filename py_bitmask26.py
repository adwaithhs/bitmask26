from ctypes import c_uint32

_ORD_A = ord('a')

class Bitmask26:
    def __init__(self, word: str):
        ords = (ord(c) - _ORD_A for c in word.lower())
        mask = c_uint32(0)
        for i in ords:
            if 0 <= i < 26:
                mask |= 1 << i
        self.mask = mask
        self.nmask = None

    def __eq__(self, bitmask: 'Bitmask26'):
        return self.mask == bitmask.mask
    
    def __hash__(self):
        return self.mask

    def __ge__(self, mask: 'Bitmask26'):
        if self.nmask is None: self.nmask = ~self.mask
        return not (self.nmask & mask.mask)

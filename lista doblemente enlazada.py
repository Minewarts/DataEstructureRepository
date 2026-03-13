class DoblyNode:

    __slots__ = ['value', 'next', 'prev']
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    @property
    def has_next(self):
        return self.next is not None
    
    @property
    def has_prev(self):
        return self.prev is not None
    
    @property
    def value(self):
        return self._value

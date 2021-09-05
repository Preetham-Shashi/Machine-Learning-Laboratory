# 221910301050

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []  # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:  # Found a match:
                item._value = v  # reassign value
                return  # and quit
        # did not find match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:  # Found a match:
                self._table.pop(j)  # remove item
                return  # and quit
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key  # yield the KEY

if __name__ == '__main__':
    utm=UnsortedTableMap()
    keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}
    for key, value in keys.items():
        utm.__setitem__(key, value)
    
    print("Unsorted Map Length =",utm.__len__())
    print("Keys and Values")
    for i in utm.__iter__():
        print(i,utm.__getitem__(i))
    
    utm.__delitem__(5)
    print("After Deletion Unsorted Map Length =",utm.__len__())
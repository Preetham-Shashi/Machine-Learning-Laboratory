#221910301050

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        return bucket[k]  # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:  # key was new to the table
            self._n += 1  # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        del bucket[k]  # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:  # a nonempty slot
                for key in bucket:
                    yield key

if __name__ == '__main__':
    # Create initial hash table
    hash_table = ChainHashMap()
    keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}

    # Set items to buckets in hash table

    for key, value in keys.items():
        buckets = []
        print('Key:', key)
        bucket = hash_table._hash_function(key) # perform hash function on all keys creating bucket destination
        buckets.append(bucket)
        for bucket in buckets: # Set key and values to bucket destination 
            hash_table._bucket_setitem(bucket, key, value)
            print('Bucket:', bucket)
            print('Value:', value, '\n')
    
    print("Hash Table Length =",hash_table.__len__())
    print("Keys and Values")
    for key in hash_table.__iter__():
        print(key,hash_table.__getitem__(key))
    
    hash_table.__delitem__(5)
    print("After Deletion Hash Table Length =",hash_table.__len__())
#221910301050

class SplayTreeMap(TreeMap):
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                # zig case
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # zig-zig case
                self._rotate(parent)
                self._rotate(p)
            else:
                # zig-zag case
                self._rotate(p)
                self._rotate(p)
                
    #---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        self._splay(p)
        
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)  
            
    def _rebalance_access(self, p):
        self._splay(p)

tree = SplayTreeMap()
keys={6: 1, 9: 3, 3: 2, 13: 5, 10: 7, 5: 4, 4: 6}

for key, value in keys.items():
    tree.__setitem__(key,value)

print('Number of elements: ', len(tree), '\n')

tree._splay(tree.root())
print("Root Node =",tree.root().key())
print("Left Child of Root =",tree.left(tree.root()).key())
print("Right Child of Root =",tree.right(tree.root()).key())
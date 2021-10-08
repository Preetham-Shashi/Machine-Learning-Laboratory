#221910301050

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        
        __slots__ = '_height'
        
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0
            
        def left_height(self):
            return self._left._height if self._left is not None else 0
        
        def right_height(self):
            return self._right._height if self._right is not None else 0
    
    #------------------------- positional-based utility methods -------------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())
    
    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1
    
    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)
    
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
        
    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))                
                self._recompute_height(self.right(p))                           
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)
    #---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)
    def _rebalance_delete(self, p):
        self._rebalance(p)
        
"""
             6
           /   \
          3     9
           \     \
            5    13
           /    /
          4    10

"""

tree = AVLTreeMap()
keys={6: 1, 9: 3, 3: 2, 13: 5, 10: 7, 5: 4, 4: 6}

for key, value in keys.items():
    tree.__setitem__(key,value)

print('Number of elements: ', len(tree), '\n')

for i in tree.__iter__():
    print((i,tree.__getitem__(i)))
    

print("\nRoot Node=",tree.root().key())    
print("Is Tree balanced?",tree._isbalanced(tree.root()))
print("Tall child =",tree._tall_child(tree.root()).key())
print("Tall grandchild =",tree._tall_grandchild(tree.root()).key())
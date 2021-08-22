#221910301050

# Set of Map Operations

#221910301050
M={}
len(M)
# Return Value - 0
# Map: {}

M['K']=2
# Map: {'K':2}

M['B']=4 
# Map: {'K':2, 'B':4}

M['U']=2
# Map: {'K':2, 'B':4, 'U':2}

M['V']=8
# Map: {'K':2, 'B':4, 'U':2, 'V':8}

M['K']=9
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

M['B']
# Return Value - 4
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

M['X']
# Return Value - KeyError
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

M.get('F')
# Return Value - None
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

M.get('F',5)
# Return Value - 5
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

M.get('K',5)
# Return Value - 9
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

len(M)
# Return Value - 4
# Map: {'K':9, 'B':4, 'U':2, 'V':8}

del M['V']
# Map: {'K':9, 'B':4, 'U':2}

M.pop('K')
# Return Value - 9
# Map: {'B':4, 'U':2}

M.keys()
# Return Value - 'B', 'U'
# Map: {'B':4, 'U':2}

M.values()
# Return Value - 4, 2
# Map: {'B':4, 'U':2}

M.items()
# Return Value - ('B', 4), ('U', 2)
# Map: {'B':4, 'U':2}

M.setdefault('B',1)
# Return Value - 4
# Map: {'B':4, 'U':2}

M.setdefault('A',1)
# Return Value - 1
# Map: {'A':1, 'B':4, 'U':2}

M.popitem()
# Return Value - ('B', 4)
# Map: {'A':1, 'U':2}
import itertools

"""
# Generate list from iter object
# itertools.islice(x,N)
>>> x = xrange(20)
>>> print(list(itertools.islice(x,3)))
[0, 1, 2]

# itertools.takewhile
>>> print(list(itertools.takewhile((3).__cmp__,x)))
[0,1,2]

# iter()
>>> print(iter(iter(x).next,3))
[0,1,2]

# groupby
>>> [(name,len(list(grp))) for name,grp in itertools.groupby(['a','a','b','b','c'])]
[('a', 2), ('b', 2), ('c', 1)]
"""


from collections import namedtuple
NamedTuple = namedtuple('NamedTuple', ['name', 'phone'])
nTuple = NamedTuple('jerry', '123')
print(nTuple)
print(nTuple.name, nTuple.phone)

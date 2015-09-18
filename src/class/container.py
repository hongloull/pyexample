import collections


class Container(collections.Iterable):

    def __iter__(self):
        return iter(self)


a=Container(['a','b','c'])
print(a)

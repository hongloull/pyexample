class ReversedIter(object):

    """docstring for ReversedIter"""

    def __init__(self, start):
        super(ReversedIter, self).__init__()
        self.start = start

    def __iter__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1

    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


for i in reversed(ReversedIter(5)):
    print(i)
# 5
# 4
# 3
# 2
# 1

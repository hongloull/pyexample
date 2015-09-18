"""
The itertools.islice() function is perfectly suited for taking slices of iterators and generators.
"""
import itertools


def gen(num):
    n = 1
    while n < num:
        yield n
        n += 1


for i in itertools.islice(gen(10), 3, 6):
    print(i)
# 4
# 5
# 6

"""
Problem:
    You'd like to define a read-only attribute as a property that only gets computed on access. However, once accessed, you'd like the value to be cached and not recomputed on each access.

Solution:
    An efficient way to define a lazy attribute is through the use of a descriptor class, such as the following.

Discussion:
    when a descriptor is placed into a class definition, its __get__(), __set__(), and __delete__() methods get triggered on attribute access. However, if a descriptor only defines a __get__() method, it has a much
    weaker binding than usual. In particular, the __get__() method only fires if the attribute being accessed is not in the underlying instance dictionary. You can observe this by digging a little deeper into the example:
    >>>c=Circle(4.0)
    >>># Get instance variables
    >>>vars(c)
    {'radius': 4.0}
    >>># Compute area and observe variables afterward
    >>>c.area
    Computing area
    50.26548245743669
    >>>vars(c)
    {'area': 50.26548245743669, 'radius': 4.0}
    >>># Notice access doesn't invoke property anymore
    >>>c.area
    50.26548245743669
    >>># Delete the variable and see property trigger again
    >>>del c.area
    >>>vars(c)
    {'radius': 4.0}
    >>>c.area
    Computing area
    50.26548245743669
"""


class LazyProperty(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(4.0)
c.radius
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)

"""
Computing area
50.2654824574
50.2654824574
Computing perimeter
25.1327412287
25.1327412287
"""

"""
A central feature of an abstract base class is that it cannot be instantiated directly. To define an abstract base class, use the abc module.
"""

from abc import ABCMeta, abstractmethod, abstractproperty


class AbcBaseClass(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._name = name

    @abstractproperty
    def name(self):
        return self._name

    @abstractmethod
    def getName(self):
        pass


class SubClass(AbcBaseClass):

    @property
    def name(self):
        return self._name

    def getName(self):
        return self._name

b = SubClass('test')

# if you try to do below, you will get an error
# a = AbcBaseClass('test')
# TypeError: Can't instantiate abstract class AbcBaseClass with abstract
# methods getName


class AbcClass(object):
    __metaclass__ = ABCMeta

AbcClass.register(tuple)
print(issubclass(tuple, AbcClass))

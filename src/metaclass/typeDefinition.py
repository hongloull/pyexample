"""
Metaclasses give the ability to interact when a class object is created in memory
through its factory. They act like
__new__
but at the class level. The built-in type
type
is the built-in base factory. It is used to generate instances of any kind of class
given its name, its base classes, and a mapping containing its attributes:
>>> def method(self):
... return 1
...
>>> klass = type('MyClass', (object,), {'method': method})
>>> instance = klass()
>>> instance.method()
1
This is similar to an explicit definition of the class:
>>> class MyClass(object):
... def method(self):
... return 1
...
>>> instance = MyClass()
>>> instance.method()
1
"""


def method(self):
    return 1

classA = type('ClassA', (object,), {'method': method})
classA().method()


class ClassA(object):

    def method(self):
        return 1

ClassA().method()

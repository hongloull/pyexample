"""
An interesting feature that is almost never used by developers is
slots. They allow you to set a static attribute list for a given class with the
__slots__ attribute, and skip the creation of the __dict__ list in each instance of the class.

class Frozen(object):
    __slots__ = ['attrA', 'attrB']


ins=Frozen()
ins.attrA = 'a'
ins.attrC = 'c'

Traceback (most recent call last):
  File "src/class/slots.py", line 7, in <module>
    ins.attrC = 'c'
AttributeError: 'Frozen' object has no attribute 'attrC'
"""

from functools import wraps
import types

class myDecorator(object):

    """
    The only constraint upon the object returned by the decorator is that it
    can be used as a function which basically means it must be callable.
    Thus, any classes we use as decorators must implement __call__.
    """

    def __init__(self, func):
        print('inside myDecorator.__init__()')
        self._func = func
        @wraps(self._func)
        def _wraps(*args, **kwargs):
            return func(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('inside myDecorator.__call__()')
        return self._func(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@myDecorator
def _decoratorExecOrder():
    print('inside _decoratorExecOrder()')

_decoratorExecOrder()
# inside myDecorator.__init__()
# inside _decoratorExecOrder()
# inside myDecorator.__call__()


class Test(object):

    @myDecorator
    def callInClass(self):
        print('Call in class')

Test().callInClass()

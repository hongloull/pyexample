from functools import wraps


def myDecorator(opt):
    def _wrap(func):
        def __wrap(*args, **kwargs):
            print(opt)
            return func(*args, **kwargs)
        return __wrap
    return _wrap


@myDecorator('dec')
def test(word=''):
    """
    test docstring
    """
    print(word)

t = test(word='word')
# print(test.__name__)

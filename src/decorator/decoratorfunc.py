"""
"""
from functools import wraps


def wrapFunc(func):
    def wrapArgs(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapArgs

def wrapFuncByFunctools(func):
    @wraps(func)
    def _wrap(*args,**kwargs):
        return func(*args,**kwargs)
    return _wrap

@wrapFunc
def test1():
    print('test1')

"""
"""
@wrapFuncByFunctools
def test4():
    print('test4')

@wrapFunc
def test2(input):
    print(input)


def wrapFuncWithArg(opt):
    print(opt)

    def wrapFunc(func):
        def wrapArgs(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapArgs
    return wrapFunc


def wrapprint(opt):
    print(opt * 2)

    def wrapFunc(func):
        def wrapArgs(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapArgs
    return wrapFunc


@wrapFuncWithArg('opt')
def test3(input):
    print(input)


@wrapprint('opt1')
@wrapFuncWithArg('opt2')
def test3(input):
    print(input)

#test1()
#test4()
print(test1.__name__)
print(dir(test4))
print(test4.__name__)
# test2('test2')
# test3('true')

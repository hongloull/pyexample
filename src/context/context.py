"""
The with statement is used to wrap the execution of a block with methods defined by a context manager (see section With Statement Context Managers). This allows common try...except...finally usage patterns to be encapsulated for convenient reuse.

The execution of the with statement with one “item” proceeds as follows:

    The context expression (the expression given in the with_item) is evaluated to obtain a context manager.

    The context manager’s __exit__() is loaded for later use.

    The context manager’s __enter__() method is invoked.

    If a target was included in the with statement, the return value from __enter__() is assigned to it.

    Note

    The with statement guarantees that if the __enter__() method returns without an error, then __exit__() will always be called. Thus, if an error occurs during the assignment to the target list, it will be treated the same as an error occurring within the suite would be. See step 6 below.

    The suite is executed.

    The context manager’s __exit__() method is invoked. If an exception caused the suite to be exited, its type, value, and traceback are passed as arguments to __exit__(). Otherwise, three None arguments are supplied.

    If the suite was exited due to an exception, and the return value from the __exit__() method was false, the exception is reraised. If the return value was true, the exception is suppressed, and execution continues with the statement following the with statement.

    If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored, and execution proceeds at the normal location for the kind of exit that was taken.

"""


class Context(object):

    """
    A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement (described in section The with statement), but can also be used by directly invoking their methods.
    implement two methods: __enter__ and __exit__
    """

    def __enter__(self):
        print('enter context')

    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        print('exit context')
        if exceptionType is None:
            print('There is no error')
        else:
            print('Error:{0}'.format(exceptionValue))


with Context():
    print('context test')


from contextlib import contextmanager

"""
This function is a decorator that can be used to define a factory function for with statement context managers, without needing to create a class or separate __enter__() and __exit__() methods.
"""
@contextmanager
def tag(name):
    print "<%s>" % name
    yield
    print "</%s>" % name

"""
>>> with tag("h1"):
...    print "foo"
...
<h1>
foo
</h1>
"""

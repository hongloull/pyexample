"""
Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords.
"""

from functools import partial


def printImport(imports=''):
    print(imports)

printOverride = partial(printImport, imports='override')
printOverride()  # print override
printOverride(imports='test')  # print test

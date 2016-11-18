"""
Modules or packages can customize how tests are loaded from them during
normal test runs or test discovery by implementing a function called load_tests.

If a test module defines load_tests it will be called by
TestLoader.loadTestsFromModule() with the following arguments:

load_tests(loader, standard_tests, None)


If the package __init__.py defines load_tests then it will be called and
discovery not continued into the package. load_tests is called with the
following arguments:

load_tests(loader, standard_tests, pattern)

This should return a TestSuite representing all the tests from the package. (
standard_tests will only contain tests collected from __init__.py.)

Because the pattern is passed into load_tests the package is free to continue
(and potentially modify) test discovery. A ‘do nothing’ load_tests function
for a test package would look like:

def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests

"""

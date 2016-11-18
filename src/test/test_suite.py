import unittest


class FooTest(unittest.TestCase):
    def setUp(self):
        print('set up')

    def testA(self):
        print('test A')

    def testB(self):
        print('test B')


def addTestsToSuite():
    suite = unittest.TestSuite()
    for test in ('testA', 'testB'):
        suite.addTest(FooTest(test))
    return suite


if __name__ == '__main__':
    """
    """
    unittest.TextTestRunner(verbosity=1).run(addTestsToSuite())
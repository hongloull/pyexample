import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('set up')

    def tearDown(self):
        """
        If setUp() succeeded, the tearDown() method will be run whether
        runTest() succeeded or not.
        """
        print('tear down')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            'hello world'.split(2)

    def testRun(self):
        print('test run')


if __name__ == '__main__':
    unittest.main()

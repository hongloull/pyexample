import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            'hello world'.split(2)

    def runTest(self):
        print('run test')

if __name__ == '__main__':
    unittest.main()

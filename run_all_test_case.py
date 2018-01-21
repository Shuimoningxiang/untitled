import unittest


if __name__=='__main__':
    test_cases = unittest.defaultTestLoader.discover(".", pattern='*test.py')
    unittest.TextTestRunner().run(test_cases)
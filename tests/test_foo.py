import unittest
from my_modules.foo import Foo

class MyTest(unittest.TestCase):
    def test_my_func(self):
        x = 10
        foo = Foo(x)
        y = foo.my_func(10)
        self.assertEqual(y, 20)

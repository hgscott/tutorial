import unittest

from hello import hello

class TestHello(unittest.TestCase):
    def test_hello_name(self):
        self.assertEqual(hello.hello('John'), 'Hello, John!')

    def test_integer(self):
        with self.assertRaises(TypeError):
            hello.hello(123)

if __name__ == '__main__':
    unittest.main()     

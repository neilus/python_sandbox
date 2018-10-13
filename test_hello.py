import unittest
from hello import Hello

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_hello_object(self):
        hi = Hello()
        self.assertIsNotNone(hi, "This should be something")


if __name__ == '__main__':
    unittest.main()

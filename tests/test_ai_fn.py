import unittest
from brahma_functions import ai_fn


class TestAiFn(unittest.TestCase):
    def test_decorator(self):
        @ai_fn(model="text-davinci-003", backup=False)
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_partial(self):
        partial_add = ai_fn(model="text-davinci-003", backup=False)

        @partial_add
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_no_config(self):
        @ai_fn
        def add(a, b):
            return a + b

        self.assertRaises(TypeError, lambda: add(2, 3))


if __name__ == "__main__":
    unittest.main()

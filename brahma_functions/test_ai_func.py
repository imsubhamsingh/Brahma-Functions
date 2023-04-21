import unittest

# Import the module that contains the functions to be tested
import brahma_functions


class TestBrahmaFunctions(unittest.TestCase):
    def test_ai_func_add_nums(self):
        # Define arguments for the function
        num1 = 2
        num2 = 3

        # Define expected output of function
        expected_output = "return num1 + num2"

        # Call the function with the arguments and verify its output
        self.assertEqual(
            brahma_functions.ai_func(brahma_functions.add_nums), expected_output
        )

    def test_ai_func_merge_two_linkedlists(self):
        # Define arguments for the function
        l1 = [1, 2]
        l2 = [3, 4]

        # Define expected output of function
        expected_output = "return l1 + l2"

        # Call the function with the arguments and verify its output
        self.assertEqual(
            brahma_functions.ai_func(brahma_functions.merge_two_linkedlists),
            expected_output,
        )


if __name__ == "__main__":
    unittest.main()

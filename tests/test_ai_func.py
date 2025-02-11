import os
import sys

# Add the directory containing the brahma_functions module to the sys.path list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module that contains the functions to be tested
from brahma_functions import ai_func, get_func_obj_from_str, ai_fn


# Sample Tests for the get_func_obj_from_str
func_str = """
def add_nums(a, b, c):
    return a + b
"""
func_str1 = """
def merge_two_linkedlists_v1(l1, l2):

"""


# Sample Tests for the ai_func function
def add_nums(num1, num2):
    """This function adds two numbers togetherr"""


def merge_two_linkedlists_v1(l1, l2):
    """This function merges two linked lists together"""


def merge_two_linkedlists_v2(l1, l2):
    """This function merges two linked lists together
    args:
        l1: the first linked list
        l2: the second linked list
    returns:
        the merged linked list
    """


# Test the class generation
class Car:
    """
    "Write a Python class named 'Car' with attributes 'make', 'model', and 'year',
    and a method named 'description' that returns a string in the format 'year make model'."
    """


class Vehicle:
    """
    Suppose you are working on a project that requires a class to represent
    a vehicle. You have been asked to create a class named Vehicle with the
    following methods:
    Write the code for the Vehicle class with these methods implemented.
    You can assume that the make, model, year, and color parameters are strings,
    and the speed parameter is a float. You do not need to implement any validation
    for the parameters at this time.
    """

    def __init__(self, make, model, year, color):
        # TODO: Implement the __init__ method
        pass

    def start(self):
        # TODO: Implement the start method
        pass

    def stop(self):
        # TODO: Implement the stop method
        pass

    def accelerate(self, speed):
        pass

    def decelerate(self, speed):
        # TODO: Implement the decelerate method
        pass


# Test the @ai_fn decorator
@ai_fn(generate_tests=True)
def product_of_two_array(arr1, arr2):
    """This function returns the product of two arrays"""


test_ai_fn1 = product_of_two_array([1, 2, 3], [4, 5, 6])
test_ai_fn2 = product_of_two_array([], [4, 5, 6])


if __name__ == "__main__":
    # ai_func(add_nums)
    # ai_func(merge_two_linkedlists_v1)
    # ai_func(merge_two_linkedlists_v2)
    # ai_func(Car)
    # ai_func(Vehicle)
    # ai_func(
    #     merge_two_linkedlists_v1,
    #     generate_tests=True,
    #     backup=False,
    #     mode="text-davinci-003",
    # )
    # ai_func(
    #     merge_two_linkedlists_v1,
    #     generate_tests=True,
    #     backup=False,
    #     mode="gpt-3.5-turbo",
    # )
    # ai_func(merge_two_linkedlists_v1, generate_tests=True, backup=False, mode="gpt-4")
    # ai_func(merge_two_linkedlists_v1, generate_tests=True)
    # ai_func(Vehicle, generate_tests=True, backup=False, mode="gpt-4")
    # ai_func(
    #     add_nums,
    #     generate_tests=True,
    #     backup=True,
    #     language="python",
    #     model="gpt-3.5-turbo",
    # )
    # ai_func(
    #     add_nums,
    #     generate_tests=True,
    #     backup=True,
    #     language="java",
    #     model="gpt-3.5-turbo",
    # )
    # ai_func(add_nums, generate_tests=True, backup=True, model="text-davinci-003", language="python")
    # ai_func(add_nums, generate_tests=True, backup=False, language="python", model="gpt-4")
    # ai_func(add_nums)

    # print(get_func_obj_from_str(func_str))
    # print(get_func_obj_from_str(func_str1))

    print(test_ai_fn1)
    print(test_ai_fn2)

###########################################
#                                         #
#           Brahma Functions              #
#             Version 0.1                 #
#                                         #
#  This file contains the functions that  #
#    are used in the Brahma project.      #
#                                         #
###########################################


import os
import inspect
import functools
import openai
from formatters import _format_python_code

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "text-davinci-003"
DEBUG = True


@functools.lru_cache(maxsize=None)
def ai_func(func, prompt=None, *args, **kwargs):
    """
    This function uses GPT to generate code for the given function signature.
    args:
        func: the function to generate code for
        language: the language to use for the code generation
    returns:
        the generated code
    """
    language = kwargs.get("language", "python")
    backup = kwargs.get("backup", True)

    # get the function arguments and comments
    argspec = inspect.getfullargspec(func)
    comments = inspect.getdoc(func)

    # build the prompt
    if prompt is None:
        prompt = (
            f"Write a function {func.__name__} that"
            f" takes {len(argspec.args)} arguments: {', '.join(argspec.args)}\n"
            + "\n".join([f"- {arg}" for arg in argspec.args])
            + "\n\n"
            + (f"Here are the comments:\n{comments}\n\n" if comments else "")
        )

    if DEBUG:
        print(prompt)

    CACHE_DIR = "generated_code"
    CACHE_FILE = f"{func.__name__}.py"
    CACHE_FILE_PATH = f"{CACHE_DIR}/{CACHE_FILE}"

    # check if the code has already been generated
    if os.path.exists(CACHE_FILE_PATH):
        # Ask the user if they want to use the cached code
        regenerate = input(
            f"Code for '{CACHE_FILE}' already exists. Regenerate (y/n)?: "
        )
        if regenerate.lower() == "n":
            with open(CACHE_FILE_PATH, "r") as f:
                return f.read()

    # generate the code using GPT
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
        stop=None,
    )

    # extract and return the genetrated code
    generated_code = response.choices[0].text.strip()

    if backup:
        # write the generated code to a file
        if not os.path.exists(CACHE_DIR):
            os.mkdir(CACHE_DIR)
        with open(f"{CACHE_FILE_PATH}", "w") as f:
            print(f"Writing generated code to {CACHE_FILE_PATH}")
            f.write(generated_code)

    # format the generated code
    generated_code = _format_python_code(generated_code)

    return generated_code


# Running some samples to test the functions
# TODO: Remove this code and create a separate file for testing


def add_nums(num1, num2):
    """This function adds two numbers together"""


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


if __name__ == "__main__":
    ai_func(add_nums)
    # ai_func(merge_two_linkedlists_v1)
    # ai_func(merge_two_linkedlists_v2)

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
from .formatters import _format_python_code

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "text-davinci-003"
DEBUG = True


@functools.lru_cache(maxsize=None)
def ai_func(obj, prompt=None, *args, **kwargs):
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

    if inspect.isfunction(obj):
        # get the function arguments and comments
        argspec = inspect.getfullargspec(obj)
        comments = inspect.getdoc(obj)

        # build the prompt
        if prompt is None:
            prompt = (
                f"Write a function {obj.__name__} that"
                f" takes {len(argspec.args)} arguments: {', '.join(argspec.args)}\n"
                + "\n".join([f"- {arg}" for arg in argspec.args])
                + "\n\n"
                + (f"Here are the comments:\n{comments}\n\n" if comments else "")
            )
    elif inspect.isclass(obj):
        # get the class attributes and comments
        class_members = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))

        attributes = [a for a in class_members if not a[0].startswith("_")]

        attributes_names = [a[0] for a in attributes]
        attributes_values = [a[1] for a in attributes]

        class_methods = inspect.getmembers(obj, predicate=inspect.isfunction)
        class_methods_names = [a[0] for a in class_methods]

        comments = inspect.getdoc(obj)

        # build the prompt
        if prompt is None:
            prompt = (
                f"Write a class {obj.__name__} that has the following attributes:\n"
                + "\n".join([f"- {arg}" for arg in attributes_names])
                + "\n\n"
                + (f"Here are the comments:\n{comments}\n\n" if comments else "")
            )

            for method in class_methods:
                method_name = method[0]
                method_comments = inspect.getdoc(method[1])
                method_argspec = inspect.getfullargspec(method[1])
                prompt += f"Write a method {method_name} that" f" takes {len(method_argspec.args)} arguments: {', '.join(method_argspec.args)}\n" + "\n".join(
                    [f"- {arg}" for arg in method_argspec.args]
                ) + "\n\n" + (
                    f"Here are the comments:\n{method_comments}\n\n"
                    if method_comments
                    else ""
                )

    if DEBUG:
        print(prompt)

    CACHE_DIR = "generated_code"
    CACHE_FILE = f"{obj.__name__}.py"
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

    # format the generated code
    generated_code = _format_python_code(generated_code)

    if backup:
        # write the generated code to a file
        if not os.path.exists(CACHE_DIR):
            os.mkdir(CACHE_DIR)
        with open(f"{CACHE_FILE_PATH}", "w") as f:
            print(f"Writing generated code to {CACHE_FILE_PATH}")
            f.write(generated_code)

    return generated_code

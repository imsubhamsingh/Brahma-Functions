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


@functools.lru_cache(maxsize=128)
def ai_func(obj, prompt=None, generate_tests=False, *args, **kwargs):
    """
    This function uses GPT to generate code for the given function signature.
    args:
        func: the function to generate code for
        language: the language to use for the code generation
        backup: whether to backup the generated code
        generate_tests: whether to generate tests for the function
    returns:
        the generated code
    """
    language = kwargs.get("language", "python")
    backup = kwargs.get("backup", True)

    if inspect.isfunction(obj):
        # get the function arguments and comments
        argspec = inspect.getfullargspec(obj)
        comments = inspect.getdoc(obj)
        print(generate_tests)

        # build the prompt
        if prompt is None:
            prompt = (
                f"Write a function {obj.__name__} that"
                f" takes {len(argspec.args)} arguments: {', '.join(argspec.args)}\n"
                + "\n".join([f"- {arg}" for arg in argspec.args])
                + "\n\n"
                + (f"Here are the comments:\n{comments}\n\n" if comments else "")
            )

            if generate_tests:
                print(f"Generating tests for function {obj.__name__}...")
                prompt += "Also Write few test for this above function in the end of the file:\n"

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
        if generate_tests:
            print(f"Generating tests for class {obj.__name__}...")
            prompt += "\n\n"
            prompt += (
                "Also Write few test for this above class in the end of the file:\n"
            )
    else:
        raise ValueError("The given object is not a function or class.")

    if DEBUG:
        print(prompt)

    BACKUP_DIR = "generated_code"
    SOURCE_CODE_FILE = f"{obj.__name__}.py"
    SOURCE_CODE_FILE_PATH = f"{BACKUP_DIR}/{SOURCE_CODE_FILE}"

    # check if the source code has already been generated
    if os.path.exists(SOURCE_CODE_FILE_PATH):
        # Ask the user if they want to use the cached code
        regenerate = input(
            f"Code for '{SOURCE_CODE_FILE}' already exists. Regenerate (y/n)?: "
        )
        if regenerate.lower() == "n":
            with open(SOURCE_CODE_FILE_PATH, "r") as f:
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
    print(generated_code)

    # format the generated code
    generated_code = _format_python_code(generated_code)

    if backup:
        # write the generated source code to a file
        if not os.path.exists(SOURCE_CODE_FILE_PATH):
            os.mkdir(BACKUP_DIR)
        with open(f"{SOURCE_CODE_FILE_PATH}", "w") as f:
            print(f"Writing generated code to {SOURCE_CODE_FILE_PATH}")
            f.write(generated_code)

    return generated_code

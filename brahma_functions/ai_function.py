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
from .generators import PythonPromptGenerator, JavaPromptGenerator
from brahma_functions import settings
from .models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4


@functools.lru_cache(maxsize=128)
def ai_func(
    obj, prompt=None, generate_tests=False, model="gpt-3.5-turbo", *args, **kwargs
):
    """
    This function uses GPT to generate code for the given function signature.
    args:
        func: the function to generate code for
        language: the language to use for the code generation
        backup: whether to backup the generated code
        generate_tests: whether to generate tests for the function
        model: the GPT model to use for the code generation
    returns:
        the generated code
    """

    language = kwargs.get("language", "python")
    backup = kwargs.get("backup", True)
    optimize = kwargs.get("optimize", False)

    kwargs = {
        "language": language,
        "model": model,
        "backup": backup,
        "generate_tests": generate_tests,
        "optimize": optimize,
    }
    if settings.DEBUG:
        print(kwargs)

    # create the appropriate code generator based on the language argument
    if language == "python":
        generator = PythonPromptGenerator()
    elif language == "java":
        generator = JavaPromptGenerator()
    else:
        raise ValueError("The given language is not supported.")

    # generate the code
    prompt = generator.generate_prompt(obj, prompt, *args, **kwargs)

    if settings.DEBUG:
        print(f"Prompt: {prompt}")

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

    # generate the code using GPT Model
    if model == "text-davinci-003":
        gpt_response = talk_to_gpt3(prompt)
        response = gpt_response.choices[0].text.strip()
    elif model == "gpt-3.5-turbo":
        gpt_response = talk_to_gpt3_turbo(prompt)
        response = gpt_response.choices[0].message["content"].strip()
    elif model == "gpt-4":
        gpt_response = talk_to_gpt4(prompt)
        response = gpt_response.choices[0].message["content"].strip()
    else:
        raise ValueError("The given model is not supported.")

    # extract and return the genetrated code
    generated_code = response

    if optimize:
        # format the generated code
        generated_code = _format_python_code(generated_code)

    if backup:
        # write the generated source code to a file
        print(SOURCE_CODE_FILE_PATH)
        try:
            # create the backup directory if it doesn't exist
            os.makedirs(BACKUP_DIR, exist_ok=True)
            # write the generated source code to the file
            with open(SOURCE_CODE_FILE_PATH, mode="w") as source_file:
                source_file.write(generated_code)
                print(f"Writing generated code to {SOURCE_CODE_FILE_PATH}")

        except Exception as e:
            print(f"ERROR: unable to backup generated code: {e}")
    return generated_code


def get_func_obj_from_str(func_str):
    """
    handle the case where the user passes a string instead of a function object
    """

    if "(" not in func_str:
        raise ValueError("Function signature not found in input text")

    # get the function name
    func_name = func_str.split("(")[0].strip()
    # split the function string by the first "(" and get the first part after "def"
    func_name = func_name.split("def")[1].strip()

    # get the function arguments
    func_args_list = func_str.split("(")[1]
    if len(func_args_list) == 0:
        func_args = []
    else:
        func_args = func_args_list.split(")")[0].split(",")
        func_args = [arg.strip() for arg in func_args]

    # get the function body
    func_body = func_str.split("):")[1].strip()

    # get the function signature
    func_signature = f"def {func_name}({', '.join(func_args)}):"

    # get the function source code
    func_source_code = f"{func_signature}\n    {func_body}"

    # create a temporary file to store the function source code
    with open("temp.py", "w") as f:
        f.write(func_source_code)

    try:
        # import the function from the temporary file
        import importlib.util

        spec = importlib.util.spec_from_file_location("temp", "temp.py")
        temp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(temp)
        obj = getattr(temp, func_name)
    except Exception as e:
        print(f"ERROR: Unable to import function from string: {e}")
        obj = None
    finally:
        if "temp" in locals():
            del temp
        if "spec" in locals():
            del spec
        if "f" in locals():
            f.close()
        os.remove("temp.py")

    return obj

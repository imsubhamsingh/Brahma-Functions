import ast
import inspect


def get_function_signature(func):
    """Get the function signature of a function."""
    return inspect.signature(func)


def get_function_source(func):
    """Get the source code of a function."""
    return inspect.getsource(func)


def get_function_ast(func):
    """Get the AST of a function."""
    return ast.parse(get_function_source(func))


def get_function_docstring(func):
    """Get the docstring of a function."""
    return inspect.getdoc(func)


def get_function_name(func):
    """Get the name of a function."""
    return func.__name__


def get_function_args(func):
    """Get the arguments of a function."""
    return get_function_signature(func).parameters


def get_function_arg_names(func):
    """Get the argument names of a function."""
    return get_function_args(func).keys()


def get_function_arg_defaults(func):
    """Get the argument defaults of a function."""
    return get_function_args(func).values()


def get_function_arg_default_values(func):
    """Get the argument default values of a function."""
    return [arg.default for arg in get_function_arg_defaults(func)]


def sanitize_code(code):
    """
    Sanitize the code to remove the ```python and ``` from the code.
    Also remove any char comes after ``` in first line.
    Eg:
    ```python
    def my_function():
        #This function takes no arguments and returns None.
        return None
    ```

    will be converted to:
    def my_function():
        #This function takes no arguments and returns None.
        return None
    """
    if code.startswith("```"):
        code = code[code.find("\n") + 1 :].strip()
    if code.endswith("```"):
        code = code[: code.rfind("\n")].strip()
    return code

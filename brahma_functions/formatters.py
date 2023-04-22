import black


def _format_python_code(code):
    """
    Format the generated Python code to make it more readable and consistent.
    """
    return black.format_str(code, mode=black.FileMode())

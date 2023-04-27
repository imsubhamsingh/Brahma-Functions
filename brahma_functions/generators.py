import inspect
from abc import ABC, abstractmethod


class CodePromptGenerator(ABC):
    """
    This is an abstract class that is used to generate code.
    """

    @abstractmethod
    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError


class PythonPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate Python prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        """
        This function generates a prompt for the user to write code.

        Parameters
        ----------
        obj : function or class
            The function or class for which the prompt is to be generated.
        prompt : str, optional
            The prompt to be generated. If not provided, a prompt is generated
            automatically. The default is None.
        **kwargs : dict
            Additional arguments to be passed to the function.

        Returns
        -------
        str
            The prompt to be displayed to the user.
        """
        generate_tests = kwargs.get("generate_tests")
        print(f"generate_tests_gen: {generate_tests}")
        print(f"kwargs_gen: {kwargs}")
        print(type(obj))
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

                if generate_tests:
                    print(f"Generating tests for function {obj.__name__}...")
                    prompt += "Also Write few test for this above function in the end of the file:\n"

        elif inspect.isclass(obj):
            # get the class attributes and comments
            class_members = inspect.getmembers(
                obj, lambda a: not (inspect.isroutine(a))
            )

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
            raise TypeError("obj must be a function or a class")

        return prompt


class JavaPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate Java prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError


class JavaScriptPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate JavaScript prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError


class CppPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate C++ prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError


class CSharpPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate C# prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError


class GoPromptGenerator(CodePromptGenerator):
    """
    This class is used to generate Go prompt code.
    """

    def generate_prompt(self, obj, prompt=None, **kwargs):
        raise NotImplementedError

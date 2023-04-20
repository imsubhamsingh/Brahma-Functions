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

    # get the function arguments and comments
    argspec = inspect.getfullargspec(func)
    comments = inspect.getdoc(func)

    # build the prompt
    if prompt is None:
        prompt = f"Write a function {func.__name__} that"
        prompt += f" takes {len(argspec.args)} arguments: {', '.join(argspec.args)}"

        for arg in argspec.args:
            prompt += f"\n- {arg}"
        prompt += "\n\n"

        if comments is not None:
            prompt += f"Here are the comments:\n{comments}\n\n"

        prompt += f"The function should return:\n\n"
        if DEBUG:
            print(prompt)

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
    return generated_code


def add_nums(num1, num2):
    """This function adds two numbers together"""


if __name__ == "__main__":
    print(ai_func(add_nums))

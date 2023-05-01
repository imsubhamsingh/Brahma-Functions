import streamlit as st
from brahma_functions import settings
from brahma_functions import ai_func


def app():
    st.title("Brahma Factory")
    st.subheader(
        "Generate code for your functions and classes using OpenAI's GPT-3 API"
    )

    # add an input for the OpenAI API key and make it hidden
    api_key = st.text_input(
        "Setup OpenAI API Key:", value=settings.OPENAI_API_KEY, type="password"
    )
    if api_key:
        settings.set_openai_key(api_key)

    # define input options
    func_type = st.radio(
        "What type of function would you like to generate?",
        ("Function", "Class"),
    )

    # take code input
    st.subheader("Code Input")
    # determine if the user wants to generate code for a function or a class
    if func_type == "Function":
        code_input = st.text_area("Write the function name below:")
        if code_input:
            from brahma_functions import get_func_obj_from_str

            obj = get_func_obj_from_str(code_input)

    elif func_type == "Class":
        code_input = st.text_area("Write the class name below:")

    # get arguments
    num_args = st.number_input("Number of arguments:", min_value=0, step=1)
    args = []
    for i in range(num_args):
        args.append(st.text_input(f"Argument {i+1}:"))

    # get comments
    comments = st.text_area("Comments (optional):")

    generate_tests = st.checkbox("Generate tests?")

    # select model and optimization
    model = st.selectbox(
        "Select a model:", ["gpt-3.5-turbo", "text-davinci-003", "gpt-4"]
    )
    optimize = st.checkbox("Optimize output code?")

    # generate code
    if st.button("Generate Code"):
        if func_type == "Function":
            try:
                code = ai_func(
                    obj=obj,
                    # prompt=f"Write a function {name} that takes {num_args} arguments: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                    generate_tests=generate_tests,
                    model=model,
                    optimize=optimize,
                )
            except NameError:
                raise ValueError("Function name not found in input text")
        elif func_type == "Class":
            code = ai_func(
                obj=obj,
                # prompt=f"Write a class {name} that has the following attributes: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                generate_tests=generate_tests,
                model=model,
                optimize=optimize,
            )
        if settings.DEBUG:
            print(f"obj: {obj}") if obj else None

        st.write("Generated Code:")
        st.code(code, language="python")
        st.stop()


if __name__ == "__main__":
    app()

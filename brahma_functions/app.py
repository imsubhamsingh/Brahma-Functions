import streamlit as st
from brahma_functions import ai_func


def app():
    st.title("Brahma Functions")

    # define input options
    func_type = st.radio(
        "What type of function would you like to generate?",
        ("Function", "Class"),
    )
    generate_tests = st.checkbox("Generate tests?")

    # get function/class name
    name = st.text_input("Enter the name of your function/class:")

    # get arguments
    num_args = st.number_input("Number of arguments:", min_value=0, step=1)
    args = []
    for i in range(num_args):
        args.append(st.text_input(f"Argument {i+1}:"))

    # get comments
    comments = st.text_area("Comments (optional):")

    # generate code
    if st.button("Generate Code"):
        if func_type == "Function":
            code = ai_func(
                obj=lambda x: None,
                prompt=f"Write a function {name} that takes {num_args} arguments: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                generate_tests=generate_tests,
            )
        elif func_type == "Class":
            code = ai_func(
                obj=lambda x: None,
                prompt=f"Write a class {name} that has the following attributes: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                generate_tests=generate_tests,
            )
        st.code(code)


if __name__ == "__main__":
    app()

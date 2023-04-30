import streamlit as st
from brahma_functions import ai_func


def app():
    st.title("Brahma Factory")

    # define input options
    func_type = st.radio(
        "What type of function would you like to generate?",
        ("Function", "Class"),
    )
    generate_tests = st.checkbox("Generate tests?")

    # take code input
    st.subheader("Code Input")
    # determine if the user wants to generate code for a function or a class
    if func_type == "Function":
        code_input = st.text_area("Write the function name below:")
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

    # select model and optimization
    model = st.selectbox(
        "Select a model:", ["gpt-3.5-turbo", "text-davinci-003", "gpt-4"]
    )
    optimize = st.checkbox("Optimize output code?")

    # generate code
    if st.button("Generate Code"):
        if func_type == "Function":
            code = ai_func(
                obj=obj,
                # prompt=f"Write a function {name} that takes {num_args} arguments: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                generate_tests=generate_tests,
                model=model,
                optimize=optimize,
            )
        elif func_type == "Class":
            code = ai_func(
                obj=obj,
                # prompt=f"Write a class {name} that has the following attributes: {', '.join(args)}\n\nHere are the comments:\n{comments}\n\n",
                generate_tests=generate_tests,
                model=model,
                optimize=optimize,
            )

        # display the generated code
        st.code(code)


if __name__ == "__main__":
    app()

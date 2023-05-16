import logging
import streamlit as st
from brahma_functions import settings
from brahma_functions import ai_func


# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

##########################################
##  Title, Tabs, and Sidebar            ##
##########################################


def load_sidebar():
    st.title("𝞫(𝔁) Brahma Functions")
    st.markdown(
        "This mini-app generates codes from from function/class signature at runtime using OpenAI's GPT-3 model. [OpenAI](https://beta.openai.com/docs/models/overview)."
    )
    col1, col2, col3 = st.sidebar.columns([1, 8, 1])
    with col1:
        st.write("")
    with col2:
        st.image("images/brahma-func.jpg", use_column_width=True, width=200)
    with col3:
        st.write("")

    st.sidebar.markdown(" ## About Brahma Functions")
    st.sidebar.markdown(
        "Brahma Functions is an advanced AI function that leverages the power of GPT-3 to generate code from function signature at runtime. Right now, it supports only Python but support for other languages is coming soon."
    )
    st.sidebar.info(
        "Read more about how the function works and see the code on my [GitHub](https://github.com/imsubhamsingh/Brahma-Functions).",
        icon="ℹ️",
    )

    st.sidebar.markdown(" ## About the Author")
    st.sidebar.markdown("Subham Singh Rajput")
    st.sidebar.markdown(
        "Engineer @ [HackerEarth](https://www.hackerearth.com/) | [Twitter](https://twitter.com/imsubhamsingh) | [LinkedIn](https://www.linkedin.com/in/imsubhamsingh/) | [GitHub](https://github.com/imsubhamsingh) | [LeetCode](https://leetcode.com/iamsirius/)"
    )


##########################################
##      Brahma Functions logic          ##
##########################################
def app():
    # add an input for the OpenAI API key and make it hidden
    api_key = st.text_input(
        "Setup OpenAI API Key:", placeholder="sk-<OPENAI API KEY>", type="password"
    )
    if api_key:
        settings.set_openai_key(api_key)
    else:
        st.stop()
    # define input options

    language = st.selectbox(
        "Select a language:",
        ["Python", "JavaScript", "Java", "C++", "C#", "Go", "PHP", "Ruby", "Swift"],
    )
    if language:
        st.write(f"You selected {language}.")
    else:
        st.stop()
    # Based on the language selected, show the appropriate input options
    if language == "Python":
        pass
    elif language == "JavaScript":
        pass
    elif language == "Java":
        pass
    elif language == "C++":
        pass
    elif language == "C#":
        pass
    elif language == "Go":
        pass
    elif language == "PHP":
        pass
    elif language == "Ruby":
        pass
    elif language == "Swift":
        pass

    # determine if the user wants to generate code for a function or a class
    func_type = st.radio(
        "What type of function would you like to generate?",
        ("Function", "Class"),
    )

    # take code input
    st.subheader("Code Input")
    # determine if the user wants to generate code for a function or a class
    if func_type == "Function":
        code_input = st.text_area(
            "Write the function name below:", placeholder="def find_duplicate(nums):"
        )
        if code_input:
            from brahma_functions import get_func_obj_from_str

            obj = get_func_obj_from_str(code_input)

    elif func_type == "Class":
        code_input = st.text_area(
            "Write the class name below:", placeholder="class Person:"
        )

    # get arguments
    num_args = st.number_input(
        "Number of arguments(optional):",
        min_value=0,
        step=1,
    )
    args = []
    for i in range(num_args):
        args.append(st.text_input(f"Argument {i+1}:"))

    # get comments
    comments = st.text_area(
        "Comments (optional):",
        placeholder="Find the duplicate number in a list of numbers",
    )

    generate_tests = st.checkbox("Generate tests?")

    # select model and optimization
    model = st.selectbox(
        "Select a model:", ["gpt-3.5-turbo", "text-davinci-003", "gpt-4"]
    )
    optimize = st.checkbox("Optimize output code?")

    # generate code
    if st.button("Generate Code", type="primary"):
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
            logging.info(f"obj: {obj}")

        st.write("Generated Code:")
        st.code(code, language="python")
        st.stop()


if __name__ == "__main__":
    load_sidebar()
    app()

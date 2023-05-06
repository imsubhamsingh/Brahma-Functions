import logging
import streamlit as st
from brahma_functions import settings
from brahma_functions import ai_func
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4

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
        "<h5 style='text-align: center; color: black;'>Empower your code with the divine functions of Brahma</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.sidebar.columns([1, 8, 1])
    with col1:
        st.write("")
    with col2:
        st.image("images/brahma-func.jpg", use_column_width=True, width=200)
    with col3:
        st.write("")

    st.sidebar.markdown(" ## Brahma Functions v2.0")
    st.sidebar.markdown(
        "Brahma Functions is an advanced AI function that leverages the power of GPT-3 to generate code from given functin config."
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


def setup_api_key():
    """
    Setup the OpenAI API key to the environment variable. This is required to use the OpenAI API.
    Also a refresh button to change the API key.
    """
    # if settings.is_openai_key_set():
    #     return

    api_key = st.text_input(
        "Setup OpenAI API Key:", placeholder="sk-<OPENAI API KEY>", type="password"
    )
    st.markdown(
        "Get your API Key from [OpenAI](https://platform.openai.com/account/api-keys/).",
        unsafe_allow_html=True,
    )
    if api_key and api_key.startswith("sk-") and len(api_key) > 32:
        settings.set_openai_key(api_key)
        if settings.is_openai_key_set():
            st.success("API Key set successfully.", icon="🔑")
    else:
        if api_key:
            st.warning("Invalid API Key.", icon="🔑")

    # Make a refresh button to reset the API key
    if api_key:
        if st.button("Reset API Key"):
            if settings.is_openai_key_set():
                settings.reset_openai_key()
                st.success("API Key reset successfully.", icon="🔑")
            else:
                st.warning("No API Key set.", icon="🔑")


def app():
    """
    Main function that runs the Brahma Functions app.
    """
    language = st.selectbox(
        "Select a language:",
        [
            "Python",
            "JavaScript",
            "Java",
            "C",
            "C++",
            "C#",
            "Go",
            "PHP",
            "Ruby",
            "Swift",
        ],
    )
    # list versions of the language
    if language == "Python":
        version = st.selectbox(
            "Select a version:",
            ["3", "2"],
        )
    elif language == "JavaScript":
        version = st.selectbox(
            "Select a version:",
            ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
        )
    elif language == "Java":
        version = st.selectbox(
            "Select a version:",
            ["14", "11", "8"],
        )
    elif language == "C":
        version = st.selectbox(
            "Select a version:",
            ["GCC 10.3", "GCC 9.3", "GCC 8.4"],
        )
    elif language == "C++":
        version = st.selectbox(
            "Select a version:",
            ["C++17", "C++14", "C++11"],
        )
    elif language == "C#":
        version = st.selectbox(
            "Select a version:",
            ["C# 9", "C# 8", "C# 7"],
        )
    elif language == "Go":
        version = st.selectbox(
            "Select a version:",
            ["1.15", "1.14", "1.13"],
        )
    elif language == "PHP":
        version = st.selectbox(
            "Select a version:",
            ["7.4", "7.3", "7.2"],
        )
    elif language == "Ruby":
        version = st.selectbox(
            "Select a version:",
            ["3.0", "2.7", "2.6", "2.5"],
        )
    elif language == "Swift":
        version = st.selectbox(
            "Select a version:",
            ["5.3", "5.2", "5.1", "4.2", "4.1"],
        )
    else:
        st.error("Please select a language.")
        return

    # Determine if the user wants to generate code for a function or a class
    # TODO: Add support for class and method

    options = [
        "Function",
        "Code Stub",
        "Class",
        "Method",
    ]
    disabled_options = ["Class", "Method"]

    code_type = st.selectbox(
        "What type of code would you like to generate?",
        options,
        index=0,
        format_func=lambda x: x if x not in disabled_options else f"{x} (coming soon)",
    )

    if code_type != "Function" and code_type != "Code Stub":
        st.stop()

    prompt = ""

    # determine if the user wants to generate code for a function or a class
    if code_type in ["Function", "Code Stub"]:
        # take language config input eg. function_name, function_docstring, function_params, return_type, return_statement
        function_name = st.text_input("Function Name", placeholder="find_duplicate")
        function_docstring = st.text_input(
            "Function Docstring",
            placeholder="Find the duplicate number in a list of numbers",
        )
        # get parameters
        params = []
        num_params = st.number_input("Number of Parameters", min_value=0, step=1)
        for i in range(num_params):
            params.append(st.text_input(f"Parameter {i+1}"))

        return_type = st.text_input("Return Type", placeholder="list")
        # return_statement = st.text_input("Return Statement", placeholder="return duplicate")

        prompt = (
            f"Act as {language} language specialist with version {version}.\n"
            f"Write a function {function_name} that takes {num_params} arguments: {', '.join(params)}"
            + f" and returns {return_type}.\n"
            f"Here is a docstring for the function: {function_docstring}\n\n"
            + "Do not include any other explanatory text in your response.\n\n"
        )

    if code_type == "Code Stub":
        prompt = (
            f"Act as {language} language specialist with version {version}.\n"
            f"Generate code stub for function {function_name} that takes {num_params} arguments: {', '.join(params)}"
            + f" and returns {return_type} with proper docstrings.\n"
            + "Don't write the implementation of the function. Also write the main function to test the function.\n\n"
            + "Do not include any other explanatory text in your response.\n\n"
        )

    generate_tests = st.checkbox("Generate tests?")

    if generate_tests:
        num_tests = st.number_input("Number of Tests", min_value=0, step=1)

        prompt += f"Also write {num_tests} tests cases for the function:\n\n"

    st.write(prompt)
    # select model and optimization
    model = st.selectbox(
        "Select a model:", ["gpt-3.5-turbo", "text-davinci-003", "gpt-4"]
    )
    # TODO: Add support for optimization
    # Optimize = st.checkbox("Optimize output code?")

    # generate code
    if st.button("Generate Code", type="primary"):
        if code_type in ["Function", "Code Stub"]:
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
            # generate code
            generated_code = response
            st.write("Generated Code:")
            st.code(generated_code)
        else:
            st.error("Please select a code type.")
            return


if __name__ == "__main__":
    load_sidebar()
    setup_api_key()
    app()

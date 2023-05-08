import logging
import streamlit as st
from brahma_functions import settings
from brahma_functions import ai_func
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4
from brahma_functions.constants import LANG_TO_FILE_EXTENSION
from Brahma_Functions import load_sidebar

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


##########################################
##      Brahma Functions logic          ##
##########################################


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
            + f" and return {return_type} type.\n"
            f"Here is a docstring for the function: {function_docstring}\n\n"
            + "Do not include any other explanatory text in your response and generate as code file without any (```)delimiters.\n\n"
        )

    if code_type == "Code Stub":
        prompt = (
            f"Act as {language} language specialist with version {version}.\n"
            f"Generate code stub for function {function_name} that takes {num_params} arguments: {', '.join(params)}"
            + f" and return {return_type} type with docstrings.\n\n"
            + "Don't write the implementation of the function. Also write the main function to test the function.\n\n"
            + "Do not include any other explanatory text in your response and generate as code file without any (```)delimiters.\n\n"
        )

    generate_tests = st.checkbox("Generate tests?")

    if generate_tests:
        num_tests = st.number_input("Number of Tests", min_value=0, step=1)

        if num_tests > 0:
            prompt += (
                f"Generate {num_tests} tests for the function {function_name}.\n\n"
            )

    # select model and optimization
    model = st.selectbox("Select a model:", ["gpt-3.5-turbo", "text-davinci-003"])
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

            if language == "Python":
                if version == "2":
                    extension = "py"
                else:
                    extension = "py3"
            elif language == "JavaScript":
                if version == "Nodejs v18.15.0":
                    extension = "njs"
                else:
                    extension = "js"
            elif language == "Java":
                if version == "8":
                    extension = "java8"
                elif version == "11":
                    extension = "java11"
                else:
                    extension = "java14"
            elif language == "C++":
                if version == "17":
                    extension = "cpp17"
                elif version == "14":
                    extension = "cpp14"
                else:
                    extension = "cpp11"
            else:
                extension = LANG_TO_FILE_EXTENSION.get(language, "txt")

            # Write code to file and download
            # TODO: Add support for USER DEFINED FILE PATH
            # with open(f"{function_name}.{extension}", "w") as f:
            btn = st.download_button(
                label="Download File",
                data=generated_code,
                file_name=f"{function_name}.{extension}",
                mime="text/plain",
            )
            if btn:
                st.write("Downloaded")
        else:
            st.error("Please select a code type.")
            return


if __name__ == "__main__":
    st.title("Automated Code Generation Tool")
    load_sidebar()
    app()

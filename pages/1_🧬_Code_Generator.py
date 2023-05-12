import logging
import streamlit as st
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4
from brahma_functions.constants import (
    LANG_TO_FILE_EXTENSION,
    CODE_TYPE_FUN,
    CODE_TYPE_CLASS,
    CODE_TYPE_METHOD,
    CODE_TYPE_STUB,
    MODEL_OPT_1,
    MODEL_OPT_2,
    MODEL_OPT_3,
    CLASS_OPT_1,
    CLASS_OPT_2,
    CLASS_PLACEHOLDER,
    FUN_PLACEHOLDER,
    STUB_PLACEHOLDER,
    FUN_OPT_1,
    FUN_OPT_2,
    STUB_OPT_1,
    STUB_OPT_2,
)
from Brahma_Functions import load_sidebar, is_api_key_set

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
    options = [
        CODE_TYPE_FUN,
        CODE_TYPE_CLASS,
        CODE_TYPE_STUB,
        CODE_TYPE_METHOD,
    ]
    disabled_options = [CODE_TYPE_METHOD]

    code_type = st.selectbox(
        "What type of code would you like to generate?",
        options,
        index=0,
        format_func=lambda x: x if x not in disabled_options else f"{x} (coming soon)",
    )

    if code_type not in [CODE_TYPE_FUN, CODE_TYPE_CLASS, CODE_TYPE_STUB]:
        st.stop()

    prompt = ""
    function_name = None
    # determine if the user wants to generate code for a function or a class
    if code_type == CODE_TYPE_FUN:
        # add radio button to select option
        option = st.radio(
            "Select an option:",
            [FUN_OPT_1, FUN_OPT_2],
        )
        if option == FUN_OPT_1:
            prompt = st.text_area(
                "Prompt", height=100, max_chars=600, placeholder=FUN_PLACEHOLDER
            )
            prompt = prompt.strip()
            if prompt == "":
                st.error("Please enter a prompt.")
                return

        else:
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
                f"Act as {language} language programmer with version {version}.\n"
                f"Write a function {function_name} that takes {num_params} arguments: {', '.join(params)}"
                + f" and return {return_type} type.\n"
                f"Here is a docstring for the function: {function_docstring}\n\n"
                + "Do not include any other explanatory text like (```)delimiters in your response.\n\n"
            )

    if code_type == CODE_TYPE_STUB:
        option = st.radio(
            "Select an option:",
            [STUB_OPT_1, STUB_OPT_2],
        )
        if option == STUB_OPT_1:
            prompt = st.text_area(
                "Prompt", height=100, max_chars=600, placeholder=STUB_PLACEHOLDER
            )
            prompt = prompt.strip()
            if prompt == "":
                st.error("Please enter a prompt.")
                return

        else:
            # TODO: REMOVE REDUNDANT CODE
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
                f"Generate code stub for a function {function_name} that takes {num_params} arguments: {', '.join(params)}"
                + f" and return {return_type} type with docstrings.\n\n"
                + "Don't write the implementation of the function. Also write the main function to test the function.\n\n"
                + "Do not include any other explanatory text like (```)delimiters in your response.\n\n"
            )

    if code_type == CODE_TYPE_CLASS:
        # add radio button to select option
        option = st.radio(
            "Select an option:",
            [CLASS_OPT_1, CLASS_OPT_2],
        )

        prompt = ""
        if option == CLASS_OPT_1:
            prompt = st.text_area(
                "Prompt", height=100, max_chars=600, placeholder=CLASS_PLACEHOLDER
            )
            prompt = prompt.strip()
            if prompt == "":
                st.error("Please enter a prompt.")
                return

        if option == CLASS_OPT_2:
            st.warning("This feature is under development, please check back later.")
            return

    if code_type in [CODE_TYPE_FUN, CODE_TYPE_STUB]:
        generate_tests = st.checkbox("Generate tests?")
        if generate_tests:
            num_tests = st.number_input("Number of Tests", min_value=0, step=1)
            if num_tests > 0:
                prompt += (
                    f"Generate {num_tests} tests for the function {function_name}.\n\n"
                )

    logging.info(f"Prompt: {prompt}")
    # select model and optimization
    model = st.selectbox(
        "Select a Model:", [MODEL_OPT_1, MODEL_OPT_2, MODEL_OPT_3], index=0
    )
    # TODO: Add support for optimization
    # Optimize = st.checkbox("Optimize output code?")

    # generate code
    if st.button("Generate Code", type="primary"):
        if code_type in [CODE_TYPE_FUN, CODE_TYPE_STUB, CODE_TYPE_CLASS]:
            if model == MODEL_OPT_1:
                gpt_response = talk_to_gpt3_turbo(prompt)
                response = gpt_response.choices[0].message["content"].strip()
            elif model == MODEL_OPT_2:
                gpt_response = talk_to_gpt3(prompt)
                response = gpt_response.choices[0].text.strip()
            elif model == MODEL_OPT_3:
                st.warning("GPT-4 is coming soon. Please check back later.")
                st.stop()
            else:
                st.error("Please select a model.")
                st.stop()

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
                extension = LANG_TO_FILE_EXTENSION.get(language.upper(), "txt")
            print("File Extension:", extension)

            # Write code to file and download
            # TODO: Add support for USER DEFINED FILE PATH
            # with open(f"{function_name}.{extension}", "w") as f:
            btn = st.download_button(
                label="Download File",
                data=generated_code,
                file_name=f"{function_name}.{extension}"
                if function_name
                else f"code.{extension}",
                mime="text/plain",
            )
            if btn:
                st.write("Downloaded")
        else:
            st.error("Please select a code type.")
            return


if __name__ == "__main__":
    st.title("Automated Code Generation Tool")
    if not is_api_key_set():
        st.warning("Please set your OpenAI API key to continue.")
        st.stop()

    load_sidebar()
    app()

import logging
import streamlit as st
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4
from brahma_functions.utils import sanitize_code
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
    SQL_OLD_SCHEMA_PLACEHOLDER,
    SQL_OLD_QUERY_PLACEHOLDER,
    SQL_NEW_SCHEMA_PLACEHOLDER,
    SQL_NEW_QUERY_PLACEHOLDER,
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
        "Select a Language",
        [
            "Python",
            "Java",
            "JavaScript",
            "C",
            "C++",
            "C#",
            "Swift",
            "Go",
            "Bash",
            "PHP",
            "Perl",
            "Ruby",
            "R",
            "Rust",
            "Kotlin",
            "Scala",
            "Haskell",
            "Lua",
            "Clojure",
            "SQL",
        ],
    )
    # list versions of the language
    if language == "Python":
        version = st.selectbox(
            "Select a Version",
            ["3", "2"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["unittest", "pytest", "nose"],
        )
    elif language == "JavaScript":
        version = st.selectbox(
            "Select a Version",
            ["ES6", "ES5", "Rhino1.7", "Nodejs v18.15.0"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["jest", "mocha", "chai"],
        )
    elif language == "Java":
        version = st.selectbox(
            "Select a Version",
            ["14", "11", "8"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["junit", "testng"],
        )
    elif language == "C":
        version = st.selectbox(
            "Select a Version",
            ["GCC 10.3", "GCC 9.3", "GCC 8.4"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["cunit", "cmocka"],
        )
    elif language == "C++":
        version = st.selectbox(
            "Select a Version",
            ["C++17", "C++14", "C++11"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["gtest", "catch2"],
        )
    elif language == "C#":
        version = st.selectbox(
            "Select a Version",
            ["C# 9", "C# 8", "C# 7"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["nunit", "xunit"],
        )
    elif language == "Go":
        version = st.selectbox(
            "Select a Version",
            ["1.15", "1.14", "1.13"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["testing", "testify"],
        )
    elif language == "PHP":
        version = st.selectbox(
            "Select a Version",
            ["7.4", "7.3", "7.2"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["phpunit", "codeception"],
        )
    elif language == "Ruby":
        version = st.selectbox(
            "Select a Version",
            ["3.0", "2.7", "2.6", "2.5"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["rspec", "minitest"],
        )
    elif language == "Swift":
        version = st.selectbox(
            "Select a Version",
            ["5.3", "5.2", "5.1", "4.2", "4.1"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["xctest", "quick"],
        )
    elif language == "TypeScript":
        version = st.selectbox(
            "Select a Version",
            ["4.1", "4.0", "3.9", "3.8"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["jest", "mocha"],
        )
    elif language == "SQL":
        db_type = st.selectbox(
            "Select a database type",
            ["MYSQL", "PostgreSQL", "SQL Server", "Oracle", "SQLite"],
        )
        query_language = "SQL"
        test_framework = None

    elif language == "R":
        version = st.selectbox(
            "Select a Version",
            ["4.0", "3.6", "3.5", "3.4"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["testthat", "RUnit"],
        )
    elif language == "Scala":
        version = st.selectbox(
            "Select a Version",
            ["2.13", "2.12", "2.11", "2.10"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["scalatest", "specs2"],
        )
    elif language == "Kotlin":
        version = st.selectbox(
            "Select a Version",
            ["1.4", "1.3", "1.2", "1.1"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["junit", "kotlintest"],
        )
    elif language == "Rust":
        version = st.selectbox(
            "Select a Version",
            ["1.49", "1.48", "1.47", "1.46"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["rusttest", "rustspec"],
        )
    elif language == "Haskell":
        version = st.selectbox(
            "Select a Version",
            ["8.10", "8.8", "8.6", "8.4"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["hspec", "hunit"],
        )
    elif language == "Bash":
        version = st.selectbox(
            "Select a Version",
            ["5.1", "5.0", "4.4", "4.3"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["bats", "shunit2"],
        )
    elif language == "Lua":
        version = st.selectbox(
            "Select a Version",
            ["5.4", "5.3", "5.2", "5.1"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["busted", "luassert"],
        )
    elif language == "Perl":
        version = st.selectbox(
            "Select a Version",
            ["5.32", "5.30", "5.28", "5.26"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["test", "test2"],
        )
    elif language == "Clojure":
        version = st.selectbox(
            "Select a Version",
            ["1.10", "1.9", "1.8", "1.7"],
        )
        test_framework = st.selectbox(
            "Select a Test Framework",
            ["clojure.test", "speclj"],
        )
    else:
        st.error("Please select a language.")
        return

    code_type = None
    function_name = None

    if language == "SQL":
        schema = st.text_area(
            "Enter your Schema",
            height=150,
            max_chars=4000,
            placeholder=SQL_NEW_SCHEMA_PLACEHOLDER,
        )
        query_prompt = st.text_area(
            "Enter your Prompt",
            height=100,
            max_chars=2000,
            placeholder=SQL_NEW_QUERY_PLACEHOLDER,
        )

        prompt = (
            f"Act as {query_language} language programmer. Consider the following schema for {db_type}:\n"
            f"{schema}\n" + "Write the following query:\n\n"
            f"{query_prompt}\n\n"
        )
        logging.info(f"Query Language: {query_language}")
        logging.info(f"DB Type: {db_type}")
        logging.info(f"Query Prompt: {query_prompt}")

    # If the user has selected a language other than SQL
    else:
        # Determine if the user wants to generate code for a function, class, stub or method
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
            format_func=lambda x: x
            if x not in disabled_options
            else f"{x} (coming soon)",
        )

        if code_type not in [CODE_TYPE_FUN, CODE_TYPE_CLASS, CODE_TYPE_STUB]:
            st.stop()

        prompt = ""
        function_name = None
        # determine if the user wants to generate code for a function or a class
        if code_type == CODE_TYPE_FUN:
            # add radio button to select option
            option = st.radio(
                "Select an option",
                [FUN_OPT_1, FUN_OPT_2],
            )
            if option == FUN_OPT_2:
                prompt = st.text_area(
                    "Prompt", height=100, max_chars=2000, placeholder=FUN_PLACEHOLDER
                )
                prompt = prompt.strip()
                if prompt == "":
                    st.error("Please enter a prompt.")
                    return

            else:
                # take language config input eg. function_name, function_docstring, function_params, return_type, return_statement
                function_name = st.text_input(
                    "Function Name", placeholder="find_duplicate"
                )
                function_docstring = st.text_area(
                    "Function Description",
                    placeholder="Find the duplicate number in a list of numbers",
                    max_chars=4000,
                    height=100,
                )
                function_docstring = function_docstring.strip()
                # get parameters
                params = []
                num_params = st.number_input(
                    "Number of Parameters", min_value=0, step=1
                )
                for i in range(num_params):
                    params.append(st.text_input(f"Parameter {i+1}"))

                return_type = st.text_input("Return Type", placeholder="list")
                # return_statement = st.text_input("Return Statement", placeholder="return duplicate")

                prompt = (
                    f"Act as {language} language programmer with version {version}.\n"
                    f"Write a function {function_name} that takes {num_params} arguments: {', '.join(params)}"
                    + f" and return {return_type} type.\n"
                    f"Here is a docstring for the function: {function_docstring}\n\n"
                    + "Do not include any other explanatory text like ``` delimiters in your response.\n\n"
                )

        if code_type == CODE_TYPE_STUB:
            option = st.radio(
                "Select an option",
                [STUB_OPT_1, STUB_OPT_2],
            )
            if option == STUB_OPT_2:
                prompt = st.text_area(
                    "Prompt", height=100, max_chars=2000, placeholder=STUB_PLACEHOLDER
                )
                prompt = prompt.strip()
                if prompt == "":
                    st.error("Please enter a prompt.")
                    return

            else:
                # TODO: REMOVE REDUNDANT CODE
                # take language config input eg. function_name, function_docstring, function_params, return_type, return_statement
                function_name = st.text_input(
                    "Function Name", placeholder="find_duplicate"
                )
                function_docstring = st.text_area(
                    "Function Description",
                    placeholder="Find the duplicate number in a list of numbers",
                    max_chars=4000,
                    height=100,
                )
                function_docstring = function_docstring.strip()
                # get parameters
                params = []
                num_params = st.number_input(
                    "Number of Parameters", min_value=0, step=1
                )
                for i in range(num_params):
                    params.append(st.text_input(f"Parameter {i+1}"))

                return_type = st.text_input("Return Type", placeholder="list")
                # return_statement = st.text_input("Return Statement", placeholder="return duplicate")

                prompt = (
                    f"Act as {language} language specialist with version {version}.\n"
                    f"Generate code stub for a function {function_name} that takes {num_params} arguments: {', '.join(params)}"
                    + f" and return {return_type} type with docstrings.\n\n"
                    + "Don't write the implementation of the function. Also write the main function to test the function.\n\n"
                )

        if code_type == CODE_TYPE_CLASS:
            # add radio button to select option
            if language == "Bash":
                st.warning("Bash does not support Object Oriented Programming.")
                return

            option = st.radio(
                "Select an option",
                [CLASS_OPT_2, CLASS_OPT_1],
            )

            prompt = ""
            if option == CLASS_OPT_2:
                prompt = st.text_area(
                    "Prompt", height=100, max_chars=2000, placeholder=CLASS_PLACEHOLDER
                )
                prompt = prompt.strip()
                if prompt == "":
                    st.error("Please enter a prompt.")
                    return

            else:
                st.warning(
                    "This feature is under development, please check back later."
                )
                return

        if code_type in [CODE_TYPE_FUN, CODE_TYPE_STUB]:
            generate_tests = st.checkbox("Generate tests?")
            if generate_tests:
                # testing framework selection logic here
                num_tests = st.number_input("Number of Tests", min_value=0, step=1)
                if num_tests > 0:
                    prompt += f"Also Generate {num_tests} tests for the {code_type.lower()} {function_name} using {test_framework} framework.\n\n"
        prompt += "Please do not write any self explanatory text like ``` delimiters in your response.\n\n"

        logging.info(f"Code Type: {code_type}")

    prompt = prompt.strip()

    logging.info(f"Language: {language}")
    logging.info(f"Prompt: {prompt}")

    # select model and optimization
    model = st.selectbox(
        "Select a Model", [MODEL_OPT_1, MODEL_OPT_2, MODEL_OPT_3], index=0
    )
    # TODO: Add support for optimization
    # Optimize = st.checkbox("Optimize output code?")

    # generate code

    if st.button("Generate Code", type="primary"):
        with st.spinner("Generating Code..."):
            if code_type or db_type:
                if code_type in [
                    CODE_TYPE_FUN,
                    CODE_TYPE_STUB,
                    CODE_TYPE_CLASS,
                ] or db_type in [
                    "MYSQL",
                    "PostgreSQL",
                    "SQL Server",
                    "Oracle",
                    "SQLite",
                ]:
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
                    logging.info(f"Generated Code: {generated_code}")
                    generated_code = sanitize_code(generated_code)
                    logging.info(f"Sanitized Code: {generated_code}")
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
                    logging.info(f"File Extension: {extension}")

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
                    st.error("Please select a valid option.")
            else:
                st.error("Please select a valid option.")


if __name__ == "__main__":
    st.title("Automated Code Generation Tool")
    if not is_api_key_set():
        st.error("⚠️ Error: Access Denied!!")
        st.info(
            "🔐 Please set your API key [here](https://brahma.streamlit.app/#getting-started) to unlock its full functionality"
        )
        st.markdown(
            """
            <iframe src="https://giphy.com/embed/8m4QVdIshz8ckvSBOl" width="400" height="350" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            """,
            unsafe_allow_html=True,
        )
        st.stop()

    load_sidebar()
    app()

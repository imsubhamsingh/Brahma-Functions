import logging
import streamlit as st
from brahma_functions import settings
from brahma_functions import ai_func
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo, talk_to_gpt4

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

# Set page configuration
st.set_page_config(
    page_title="Brahma Functions",
    page_icon="images/brahma-func.jpg",
)


##########################################
##  Title, Tabs, and Sidebar            ##
##########################################


def load_sidebar():

    st.title("𝞫(𝔁) Brahma Functions")

    col1, col2, col3 = st.sidebar.columns([1, 8, 1])
    with col1:
        st.write("")
    with col2:
        st.image("images/brahma-func.jpg", use_column_width=True, width=200)
    with col3:
        st.write("")

    st.sidebar.markdown(" ## Brahma Functions v2.0")
    st.sidebar.markdown(
        "Brahma Functions is an advanced AI function that leverages the power of OpenAI's GPT-3 to generate code from any required configurations."
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
    """
    Main function that runs the Brahma Functions app.
    """

    st.markdown(
        "<h5 style='text-align: center; color: black;'>Empower your code with the divine functions of Brahma</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Brahma Functions is a web framework that quickly generates code for a function in multiple programming languages. Users can choose the programming language, function name, docstring, parameters, and return type. The AI-powered tool produces accurate code that can be easily copied and pasted into a project. Users can also create test cases and select from various AI models for code generation, making coding easier for both experienced coders and novices."
    )

    st.markdown("## Features")
    st.markdown(
        "##### 🚀 AI-powered code generation\n"
        "##### 🚀 Support for multiple programming languages\n"
        "##### 🚀 Support for multiple language versions\n"
        "##### 🚀 Code generation for functions, classes, and methods\n"
        "##### 🚀 Code stubs and docstrings generation for functions\n"
        "##### 🚀 Customizable code templates\n"
        "##### 🚀 Tests generation\n"
        "##### 🚀 Support for multiple AI models\n"
        "##### 🚀 Download generated code as a file\n"
    )
    st.markdown("## Roadmap (coming soon)")
    st.markdown(
        "###### 📌 Support for uploading configuration files for generating code.\n"
        "###### 📌 Support for code stubs for class and docstrings generation\n"
        "###### 📌 Support for adding custom test frameworks\n"
        "###### 📌 Support for generating code for multiple functions at once.\n"
        "###### 📌 Support for generating code for more programming languages and frameworks.\n"
        "###### 📌 Support for generating documentation and comments for the generated code automatically.\n"
        "###### 📌 Support for generating entire projects, not just individual functions, with appropriate file structures and configurations.\n"
        "###### 📌 Support for advanced customization options for generated code, including the ability to fine-tune the generated code based on specific project requirements.\n"
    )

    st.markdown("## How to use Brahma Functions?")
    st.markdown(
        "###### 0. Setup the OpenAI API key.\n"
        "###### 1. Select the programming language and version.\n"
        "###### 2. Select the AI model.\n"
        "###### 3. Enter the function name, docstring, parameters, and return type.\n"
        "###### 4. Click on the **Generate** button.\n"
        "###### 5. Copy the generated code and paste it into your project.\n"
    )

    st.markdown("## Supported Programming Languages")

    st.markdown(
        "##### 1. Python [3, 2]\n"
        "##### 2. C [10.3, 9.3, 8.4]\n"
        "##### 3. C++ [17, 14, 11]\n"
        "##### 4. C# [9, 8, 7]\n"
        "##### 4. Java [14, 11, 8]\n"
        "##### 5. JavaScript [ES6, ES5, Rhino1.7, Nodejs v18.15.0]\n"
        "##### 6. Go [1.15, 1.14, 1.13]\n"
        "##### 7. PHP [7.4, 7.3, 7.2]\n"
        "##### 8. Ruby [3.0, 2.7, 2.6, 2.5]\n"
        "##### 9. Swift [5.3, 5.2, 5.1, 4.2, 4.1]\n"
    )

    st.markdown("## Supported AI Models")

    st.markdown(
        "##### 1. GPT-3.5 \n" "##### 2. GPT-3.5 Turbo \n" "##### 3. GPT-4 (coming soon)"
    )


if __name__ == "__main__":
    load_sidebar()
    app()

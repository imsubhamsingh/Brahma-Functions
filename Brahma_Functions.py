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
    layout="wide",
    initial_sidebar_state="expanded",
)


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
    # st.markdown(
    #     "Get your API Key from [OpenAI](https://platform.openai.com/account/api-keys/).",
    #     unsafe_allow_html=True,
    # )
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


##########################################
##  Title, Tabs, and Sidebar            ##
##########################################


def load_sidebar():

    col1, col2, col3 = st.sidebar.columns([1, 4, 1])

    with col2:
        st.image("images/brahma-func.jpg", use_column_width=True, width=150)

    st.sidebar.markdown(
        "## 🚀 Brahma Functions v1.0"
        "\n\n Brahma Functions is an advanced AI function that leverages the power of OpenAI's GPT-3 to generate code from any required configurations."
    )

    st.sidebar.markdown("\n\n## 👨‍💻 About the Author")

    # st.sidebar.image("images/author.jpeg", use_column_width=True, width=75, caption="Author's Photo")
    st.sidebar.markdown("Subham Singh Rajput")
    st.sidebar.markdown(
        "Engineer @ [HackerEarth](https://www.hackerearth.com/) | [Twitter](https://twitter.com/imsubhamsingh) "
        "| [LinkedIn](https://www.linkedin.com/in/imsubhamsingh/) | [GitHub](https://github.com/imsubhamsingh)"
        " | [LeetCode](https://leetcode.com/iamsirius/)"
    )


##########################################
##      Brahma Functions logic          ##
##########################################


def app():
    """
    Main function that runs the Brahma Functions app.
    """
    st.title("𝞫(𝔁) Brahma Functions")

    st.markdown(
        "<h5 style='text-align: left; color: black;'>Empower your code with the divine functions of Brahma</h5>",
        unsafe_allow_html=True,
    )

    st.write(
        "Brahma Functions is a web framework that quickly generates code for a function in multiple programming languages. Users can choose the programming language, function name, docstring, parameters, and return type. The AI-powered tool produces accurate code that can be easily copied and pasted into a project. Users can also create test cases and select from various AI models for code generation, making coding easier for both experienced coders and novices."
    )

    st.markdown("### Features")
    lines = [
        "🚀 AI-powered code generation",
        "🚀 Support for multiple programming languages",
        "🚀 Support for multiple language versions",
        "🚀 Code generation for functions, classes, and methods",
        "🚀 Code stubs and docstrings generation for functions",
        "🚀 Tests generation",
        "🚀 Support for multiple AI models",
        "🚀 Download generated code as a file",
    ]
    st.markdown("###### " + "\n###### ".join(lines))

    st.markdown(
        "### Supported Programming Languages"
        "\n- 🐍 Python"
        "\n- 🔢 C"
        "\n- 🗡️ C++ "
        "\n- 💎 C#"
        "\n- ☕ Java"
        "\n- 🌐 JavaScript"
        "\n- 🏃‍♂️💨 Go"
        "\n- 🐘 PHP"
        "\n- 💎 Ruby"
        "\n- 🕊️ Swift"
    )

    st.markdown("### Supported AI Models")

    st.markdown(
        "###### 1. GPT-3.5 \n"
        "###### 2. GPT-3.5 Turbo \n"
        "###### 3. GPT-4 (coming soon) \n"
    )

    st.markdown("### Privacy Policy")
    st.markdown(
        "Brahma Functions app takes user privacy very seriously. We understand the importance of keeping your data safe and confidential. We only collect necessary information that is required to provide our service, and we do not share or sell this information to any third parties. Your OpenAI API key is securely stored and used only for generating code at your request. We may collect anonymous usage statistics to improve our app, but this data is not personally identifiable. We take appropriate measures to protect your data, including using industry-standard encryption and security protocols. By using our app, you agree to our privacy policy. If you have any concerns or questions about our privacy practices, please contact us at imsks007@gmail.com."
    )

    st.markdown(
        "<style>div.markdown-text-container { background-color: #ADD8E6 }</style>",
        unsafe_allow_html=True,
    )
    st.markdown("### Getting Started")
    st.markdown(
        "To get started, simply enter your OpenAI API key below. If you don't have an OpenAI API key, you can sign up for one [here](https://platform.openai.com/accounts/api-keys)."
    )

    # Get OpenAI API key
    setup_api_key()


if __name__ == "__main__":
    load_sidebar()
    app()

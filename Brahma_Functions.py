import logging
import streamlit as st
from brahma_functions import settings
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
    Setup the OpenAI API key to the session state. This is required to use the OpenAI API.
    Also a refresh button to change the API key.
    """
    api_key = st.text_input(
        "Setup OpenAI API Key:", placeholder="sk-<OPENAI API KEY>", type="password"
    )
    if not api_key:
        return

    if api_key and api_key.startswith("sk-") and len(api_key) > 32:
        # Set the API key to the session state
        st.session_state.openai_api_key = api_key
        # Set the API key to the settings
        settings.set_openai_key(api_key)
        st.success("API Key set successfully.", icon="🔑")
    else:
        st.warning("Invalid API Key.", icon="🔑")

    # Make a refresh button to reset the API key
    if st.button("Reset API Key"):
        if "openai_api_key" in st.session_state:
            # Delete the API key from the settings
            settings.reset_openai_key()
            # Delete the API key from the session state
            del st.session_state["openai_api_key"]
            st.warning("API Key reset successfully.", icon="🔑")
        else:
            st.warning("No API Key set.", icon="🔑")


def is_api_key_set():
    """
    Check if the API key is set in the session state.
    """

    if "openai_api_key" in st.session_state:
        return True
    else:
        return False


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

    st.caption("<Empower your code with the divine functions of Brahma>")

    st.divider()

    st.write(
        "Welcome to Brahma Functions, the ultimate solution for generating high-quality accurate code quickly and easily. Our intuitive web app supports a range of programming languages and lets you customize function name, docstring, parameters, and return type with ease. With cutting-edge AI technology and a range of models, our tool streamlines the coding process and makes creating test cases a breeze. Whether you're a seasoned pro or a beginner, Brahma Functions simplifies the task of crafting top-notch code for your projects. Give it a go today and feel the difference!"
    )
    st.divider()
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

    st.divider()
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
    st.divider()
    st.markdown("### Supported AI Models")

    st.markdown(
        "###### 1. GPT-3.5 \n"
        "###### 2. GPT-3.5 Turbo \n"
        "###### 3. GPT-4 (coming soon) \n"
    )

    st.divider()

    st.markdown("### Privacy Policy")
    st.markdown(
        "Brahma Functions app takes user privacy very seriously. We understand the importance of keeping your data safe and confidential. We only collect necessary information that is required to provide our service, and we do not share or sell this information to any third parties. Your OpenAI API key is securely stored and used only for generating code at your request. We may collect anonymous usage statistics to improve our app, but this data is not personally identifiable. We take appropriate measures to protect your data, including using industry-standard encryption and security protocols. By using our app, you agree to our privacy policy. If you have any concerns or questions about our privacy practices, please contact us at imsks007@gmail.com."
    )

    st.markdown(
        "<style>div.markdown-text-container { background-color: #ADD8E6 }</style>",
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Getting Started")
    st.markdown(
        "To get started, simply enter your OpenAI API key below. If you don't have an OpenAI API key, you can sign up for one [here](https://platform.openai.com/accounts/api-keys)."
    )

    # Get OpenAI API key
    setup_api_key()

    # add a proceed button to proceed to the code generation page


if __name__ == "__main__":
    load_sidebar()
    app()

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
        "Setup OpenAI API Secret", placeholder="sk-<OPENAI API KEY>", type="password"
    )
    if not api_key:
        return

    if api_key and api_key.startswith("sk-") and len(api_key) > 32:
        # Set the API key to the session state
        st.session_state.openai_api_key = api_key
        # Set the API key to the settings
        settings.set_openai_key(api_key)
        st.success("Access Granted: API Key set successfully.", icon="🔑")
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
        "\n\n Brahma Functions harnesses the cutting-edge capabilities of OpenAI's GPT model to deliver an unparalleled AI-driven code generation experience."
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
    st.markdown(
        """
        <div style="text-align: center; color: black;">
            <h1> ⚡️Brahma Functions⚡️</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div style="text-align: center; color: black;"> <h4> <i> Next-Level Code Generation with AI </i> </h4> </div>""",
        unsafe_allow_html=True,
    )
    # st.caption("<Experience Next-Level Code Generation with Brahma Functions>")

    st.divider()

    st.write(
        "Welcome to Brahma Functions, the ultimate solution for generating high-quality accurate code quickly and easily. Our intuitive web app supports a range of programming languages and lets you customize function name, docstring, parameters, and return type with ease. With cutting-edge AI technology and a range of models, our tool streamlines the coding process and makes creating test cases a breeze. Whether you're a seasoned pro or a beginner, Brahma Functions simplifies the task of crafting top-notch code for your projects. Give it a go today and feel the difference!"
    )
    st.divider()
    st.markdown("### Features")
    lines = [
        "🚀 Advanced NLP capabilities for lightning-fast results",
        "🌍 Support for 20+ programming languages, tailored to your preferences",
        "🌟 Seamlessly compatible with multiple language versions for versatile projects",
        "💡 Effortlessly generate code for functions, classes, and methods",
        "📚 Automatic code stubs and docstrings creation for thorough documentation",
        "✅ Reliable code quality ensured with 40+ testing frameworks",
        "🎧 Harness the AI magic for seamless code translation",
        "⚡  Accelerate database development with simplified SQL query generation",
        "🚀 Tailor code generation to your needs with multiple AI models ",
        "🔧 Customize code generation with cutting-edge AI models",
        "💾 Download your generated code files with ease for seamless integration",
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
        "\n- 🗃️ SQL"
        "\n- 🐹 Haskell"
        "\n- 🐚 Bash"
        "\n- 🐪 Perl"
        "\n- 🅡 R"
        "\n- 🐦 TypeScript"
        "\n- 🐬 Kotlin"
        "\n- 🐍 Lua"
        "\n- 🐙 Rust"
        "\n- 🦑 Scala"
        "\n- 🐍 Clojure"
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
        "Brahma Functions app takes user privacy very seriously. We understand the importance of keeping your data safe and confidential. We only collect necessary information that is required to provide our service, and we do not share or sell this information to any third parties. Your OpenAI API key is securely stored and used only for generating code at your request. To run your own queries here, you have to provide your OpenAI API key. The key will only be stored in your browser's [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage). By using our app, you agree to our privacy policy. If you have any concerns or questions about our privacy practices, please contact us at imsks007@gmail.com."
    )

    st.markdown(
        "<style>div.markdown-text-container { background-color: #ADD8E6 }</style>",
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Getting Started")
    st.markdown(
        "To get started, simply enter your OpenAI API key below. If you don't have an OpenAI API key, You can find your API key in the [OpenAI dashboard](https://platform.openai.com/account/api-keys)."
    )
    st.info(
        "Note: Brahma Functions will use your API key to execute completion requests on your behalf. This will result in charges on your OpenAI account. Please make sure you understand the [OpenAI pricing model](https://platform.openai.com/pricing) before using it. Brahma Functions does not take responsibility for any charges incurred by executing queries on this site."
    )
    # st.markdown("Brahma functions will use your API key to execute completion requests on your behalf. This will result in charges on your OpenAI account. Please make sure you understand the [OpenAI pricing model](https://platform.openai.com/pricing) before using it. Brahma Functions does not take responsibility for any charges incurred by executing queries on this site.")
    # Get OpenAI API key
    setup_api_key()

    # add a proceed button to proceed to the code generation page


if __name__ == "__main__":
    load_sidebar()
    app()

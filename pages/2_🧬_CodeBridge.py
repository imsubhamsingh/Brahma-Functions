import logging
import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
from Brahma_Functions import load_sidebar, is_api_key_set
from brahma_functions.constants import MODEL_OPT_1, MODEL_OPT_2, MODEL_OPT_3
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo
from brahma_functions.utils import sanitize_code

# init logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def app():
    """
    Main function that runs the AI Code Translator app.
    """

    # language selection
    input_language = st.selectbox(
        "Select Input Language",
        (
            "Python",
            "JavaScript",
            "C",
            "C++",
            "Java",
            "CSharp",
            "PHP",
            "Go",
            "Ruby",
            "TypeScript",
            "Swift",
            "Kotlin",
            "Rust",
            "Scala",
            "R",
            "Haskell",
            "Perl",
            "Lua",
            "Clojure",
            "Bash",
        ),
        key="input_language",
    )

    if input_language == "Python":
        input_version = st.selectbox(
            "Select a Version",
            ["3", "2"],
        )
    elif input_language == "JavaScript":
        input_version = st.selectbox(
            "Select a Version",
            ["ES6", "ES5"],
        )
    elif input_language == "C":
        input_version = st.selectbox(
            "Select a Version",
            ["C11", "C99"],
        )
    elif input_language == "C++":
        input_version = st.selectbox(
            "Select a Version",
            ["C++17", "C++14", "C++11", "C++98"],
        )
    elif input_language == "Java":
        input_version = st.selectbox(
            "Select a Version",
            ["14", "13", "12", "11", "10", "8"],
        )
    elif input_language == "CSharp":
        input_version = st.selectbox(
            "Select a Version",
            ["9", "8", "7.3", "7.2", "7.1", "7", "6", "5"],
        )
    elif input_language == "PHP":
        input_version = st.selectbox(
            "Select a Version",
            ["8", "7.4", "7.3", "7.2", "7.1", "7.0", "5.6"],
        )
    elif input_language == "Go":
        input_version = st.selectbox(
            "Select a Version",
            ["1.15", "1.14", "1.13", "1.12", "1.11", "1.10", "1.9"],
        )
    elif input_language == "Ruby":
        input_version = st.selectbox(
            "Select a Version",
            ["3.0", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2"],
        )
    elif input_language == "TypeScript":
        input_version = st.selectbox(
            "Select a Version",
            ["4.1", "4.0", "3.9", "3.8", "3.7", "3.6", "3.5"],
        )
    elif input_language == "Swift":
        input_version = st.selectbox(
            "Select a Version",
            ["5.3", "5.2", "5.1", "5.0", "4.2"],
        )
    elif input_language == "Kotlin":
        input_version = st.selectbox(
            "Select a Version",
            ["1.4", "1.3", "1.2", "1.1", "1.0"],
        )
    elif input_language == "Rust":
        input_version = st.selectbox(
            "Select a Version",
            ["1.49", "1.48", "1.47", "1.46", "1.45", "1.44", "1.43"],
        )
    elif input_language == "Scala":
        input_version = st.selectbox(
            "Select a Version",
            ["2.13", "2.12", "2.11", "2.10"],
        )
    elif input_language == "R":
        input_version = st.selectbox(
            "Select a Version",
            ["4.0", "3.6", "3.5", "3.4", "3.3"],
        )
    elif input_language == "Haskell":
        input_version = st.selectbox(
            "Select a Version",
            ["8.10", "8.8", "8.6", "8.4", "8.2", "8.0"],
        )
    elif input_language == "Perl":
        input_version = st.selectbox(
            "Select a Version",
            ["5.32", "5.30", "5.28", "5.26", "5.24", "5.22"],
        )
    elif input_language == "Lua":
        input_version = st.selectbox(
            "Select a Version",
            ["5.4", "5.3", "5.2", "5.1"],
        )
    elif input_language == "Clojure":
        input_version = st.selectbox(
            "Select a Version",
            ["1.10", "1.9", "1.8", "1.7", "1.6"],
        )
    elif input_language == "Bash":
        input_version = st.selectbox(
            "Select a Version",
            ["5.1", "5.0", "4.4", "4.3", "4.2", "4.1", "4.0"],
        )

    c1, c2 = st.columns([3, 1])
    with c1:
        code = st_ace(
            # language=input_language.lower(),
            language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
            theme=c2.selectbox("Theme", options=THEMES, index=2),
            keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
            font_size=c2.slider("Font size", 5, 24, 14),
            min_lines=20,
            key="ace",
            auto_update=True,
        )

    # Select the language you want to translate to
    output_language = st.selectbox(
        "Select Output Language",
        (
            "JavaScript",
            "Python",
            "C",
            "C++",
            "Java",
            "CSharp",
            "PHP",
            "Go",
            "Ruby",
            "TypeScript",
            "Swift",
            "Kotlin",
            "Rust",
            "Scala",
            "R",
            "Haskell",
            "Perl",
            "Lua",
            "Clojure",
            "Bash",
        ),
        key="output_language",
    )

    if output_language == "Python":
        output_version = st.selectbox(
            "Select a Version",
            ["3", "2"],
            key="output_version",
        )
    elif output_language == "JavaScript":
        output_version = st.selectbox(
            "Select a Version",
            ["ES6", "ES5"],
            key="output_version",
        )
    elif output_language == "C":
        output_version = st.selectbox(
            "Select a Version",
            ["C11", "C99"],
            key="output_version",
        )
    elif output_language == "C++":
        output_version = st.selectbox(
            "Select a Version",
            ["C++17", "C++14", "C++11", "C++98"],
            key="output_version",
        )
    elif output_language == "Java":
        output_version = st.selectbox(
            "Select a Version",
            ["14", "13", "12", "11", "10", "8"],
            key="output_version",
        )
    elif output_language == "CSharp":
        output_version = st.selectbox(
            "Select a Version",
            ["9", "8", "7.3", "7.2", "7.1", "7", "6", "5"],
            key="output_version",
        )
    elif output_language == "PHP":
        output_version = st.selectbox(
            "Select a Version",
            ["8", "7.4", "7.3", "7.2", "7.1", "7.0", "5.6"],
            key="output_version",
        )
    elif output_language == "Go":
        output_version = st.selectbox(
            "Select a Version",
            ["1.15", "1.14", "1.13", "1.12", "1.11", "1.10", "1.9"],
            key="output_version",
        )
    elif output_language == "Ruby":
        output_version = st.selectbox(
            "Select a Version",
            ["3.0", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2"],
            key="output_version",
        )
    elif output_language == "TypeScript":
        output_version = st.selectbox(
            "Select a Version",
            ["4.1", "4.0", "3.9", "3.8", "3.7", "3.6", "3.5"],
            key="output_version",
        )
    elif output_language == "Swift":
        output_version = st.selectbox(
            "Select a Version",
            ["5.3", "5.2", "5.1", "5.0", "4.2"],
            key="output_version",
        )
    elif output_language == "Kotlin":
        output_version = st.selectbox(
            "Select a Version",
            ["1.4", "1.3", "1.2", "1.1", "1.0"],
            key="output_version",
        )
    elif output_language == "Rust":
        output_version = st.selectbox(
            "Select a Version",
            ["1.49", "1.48", "1.47", "1.46", "1.45", "1.44", "1.43"],
            key="output_version",
        )
    elif output_language == "Scala":
        output_version = st.selectbox(
            "Select a Version",
            ["2.13", "2.12", "2.11", "2.10"],
            key="output_version",
        )
    elif output_language == "R":
        output_version = st.selectbox(
            "Select a Version",
            ["4.0", "3.6", "3.5", "3.4", "3.3"],
            key="output_version",
        )
    elif output_language == "Haskell":
        output_version = st.selectbox(
            "Select a Version",
            ["8.10", "8.8", "8.6", "8.4", "8.2", "8.0"],
            key="output_version",
        )
    elif output_language == "Perl":
        output_version = st.selectbox(
            "Select a Version",
            ["5.32", "5.30", "5.28", "5.26", "5.24", "5.22"],
            key="output_version",
        )
    elif output_language == "Lua":
        output_version = st.selectbox(
            "Select a Version",
            ["5.4", "5.3", "5.2", "5.1"],
            key="output_version",
        )
    elif output_language == "Clojure":
        output_version = st.selectbox(
            "Select a Version",
            ["1.10", "1.9", "1.8", "1.7", "1.6"],
            key="output_version",
        )
    elif output_language == "Bash":
        output_version = st.selectbox(
            "Select a Version",
            ["5.1", "5.0", "4.4", "4.3", "4.2", "4.1", "4.0"],
            key="output_version",
        )

    if input_language == output_language and input_version == output_version:
        st.error(
            "Hey! You can't translate to the same language and version! 😅 Please select a different language or version."
        )
        st.stop()

    comments = st.checkbox("Generate comments for the code", key="comments")

    # fetch code from ace editor
    code = code.strip()

    # prompt
    prompt = f"You are an expert programmer in all programming languages. Translate the following {input_language} {input_version} code to {output_language} {output_version} code:\n\n{code}"
    prompt += "\n\n"
    prompt += "Also write the necessary comments for the code:\n\n" if comments else ""
    prompt += "Please do not write any self explanatory text like ``` delimiters in your response.\n\n"

    prompt = prompt.strip()

    logging.info(f"Prompt: {prompt}")

    # select model and optimization
    model = st.selectbox(
        "Select a Model", [MODEL_OPT_1, MODEL_OPT_2, MODEL_OPT_3], index=0
    )

    # translate button
    translate_button = st.button(
        "Translate", key="translate", help="Translate code", type="primary"
    )

    st.markdown(
        "<h3 style='text-align: center; color: black;'>Translated code</h3>",
        unsafe_allow_html=True,
    )
    # st.divider()

    # translate code
    if translate_button:
        st.divider()
        with st.spinner("Translating code..."):
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

            # display translated code
            translated_code = response

            # sanitize code
            sanitize_code(translated_code)
            logging.info(f"Translated code: {translated_code}")

            # display translated code in ace editor
            st_ace(
                translated_code,
                language=output_language.lower(),
                theme="chrome",
                keybinding="vscode",
                font_size=14,
                min_lines=20,
                key="ace2",
                auto_update=True,
            )


if __name__ == "__main__":
    st.markdown(
        """
        <div style="text-align: center; color: black;">
            <h1>CodeBridge</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div style="text-align: center; color: black;"> <h4> <i>Effortless code translation for developers</i> </h4> </div>""",
        unsafe_allow_html=True,
    )

    # st.divider()
    if not is_api_key_set():
        st.error("⚠️ Error: Access Denied!!")
        st.info(
            "🔐 Please set your API key [here](https://brahma.streamlit.app/#getting-started) to unlock its full functionality"
        )
        st.stop()

    load_sidebar()
    app()

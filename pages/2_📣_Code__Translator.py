import logging
import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
from Brahma_Functions import load_sidebar, is_api_key_set
from brahma_functions.constants import MODEL_OPT_1, MODEL_OPT_2, MODEL_OPT_3
from brahma_functions.models import talk_to_gpt3, talk_to_gpt3_turbo

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

    # fetch code from ace editor
    code = code.strip()

    # prompt
    prompt = f"You are an expert programmer in all programming languages. Translate the following {input_language} code to {output_language} code:\n\n{code}"
    prompt += "\n\n"
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
    st.title("AI Code Translator")
    st.caption("Effortless code translation for developers")
    st.divider()
    if not is_api_key_set():
        st.error("⚠️ Error: Access Denied!!")
        st.info(
            "🔐 Please set your API key [here](https://brahma.streamlit.app/#getting-started) to unlock its full functionality"
        )
        st.stop()

    load_sidebar()
    app()

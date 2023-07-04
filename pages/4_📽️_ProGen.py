import streamlit as st
from Brahma_Functions import load_sidebar


def app():
    """
    Main function that runs the Brahma Functions app.
    """
    st.markdown(
        """
        <div align='center'>
            <iframe src="https://giphy.com/embed/LqmXowsvx0yqn3RnfK" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    load_sidebar()
    app()

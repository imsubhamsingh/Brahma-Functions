import streamlit as st
from Home import load_sidebar


def app():
    """
    Main function that runs the Brahma Functions app.
    """
    st.markdown(
        """
        <div align='center'>
            <img src='https://media.giphy.com/media/3o7aDcz3u24RLHjGGI/giphy.gif' width='300' height='300' />
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Coming Soon!</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center; color: black;'>Brahma is working on this feature. Please check back later.</h3>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    load_sidebar()
    app()

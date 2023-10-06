import streamlit as st

def maintenance_mode():
    """
    Function to display a maintenance message.
    """
    st.warning(
        f"🚧 Sorry, We're down for scheduled maintenance. Please check back later.🚧 \n\n"
        f"You can visit [status page](https://ultronlabs.statuspage.io/) to check the status. "
    )


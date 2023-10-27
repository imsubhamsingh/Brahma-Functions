import streamlit as st

# Title and header
st.title("Product Updates Page")
st.header("Check out the latest product updates here!")

# Product updates
updates = [
    {
        "title": "Version 1.0 Released",
        "date": "October 1, 2023",
        "description": "We are excited to announce the release of version 1.0 of our product. This release includes many new features and improvements."
    },
    {
        "title": "Improved User Interface",
        "date": "September 15, 2023",
        "description": "We have updated the user interface to provide a more user-friendly experience. Let us know what you think!"
    },
    {
        "title": "Bug Fixes",
        "date": "September 5, 2023",
        "description": "We've addressed several bugs reported by our users to make the product more stable and reliable."
    }
]

# Display updates
for update in updates:
    st.subheader(update["title"])
    st.write(f"Date: {update['date']}")
    st.write(update["description"])
    st.markdown("---")  # Horizontal line to separate updates


# Add a feedback section
st.header("Provide Feedback")
feedback = st.text_area("Share your thoughts or suggestions here:", height=200)
if st.button("Submit Feedback"):
    # You can add code here to process and store the feedback
    st.success("Feedback submitted successfully!")

# Sidebar with additional information
st.sidebar.header("About")
st.sidebar.write("This page displays the latest product updates.")
st.sidebar.write("Created with Streamlit.")


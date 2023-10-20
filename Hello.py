import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon="👋",
)

st.write("# Welcome to Bhinneka App! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Bhinneka App is an open-source app framework built specifically for
    Exploring and Contributing Indonesia Local Languages.
    **👈 Select a demo from the sidebar** to see some examples
    of what Bhinneka App can do!
    ### Want to learn more?
    - Check out [bhinneka.io](#)
    - Jump into our [documentation](#)
    - Ask a question in our [community
        forums](#)
    ### See parallel corpus 
    - Explore a [Indonesian Local Languages dataset](https://github.com/joanitolopo/bhinneka-korpus)
""")

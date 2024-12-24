import streamlit as st


def multi_page():
    with st.sidebar:
        st.page_link("streamlit_app.py", label="ホーム", icon="🏠")
        st.page_link("pages/multi_page1.py", label="マルチページ1", icon="1️⃣")
        st.page_link("pages/multi_page2.py", label="マルチページ2", icon="2️⃣")

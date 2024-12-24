"""例2-17 コールバック"""

import streamlit as st

st.title("コールバックの使用")


def test_callback():
    st.write(
        "コールバックが実行されました。入力テキストはこちら-> ",
        st.session_state["text_input"],
    )


st.text_input("テキスト入力", key="text_input", on_change=test_callback)

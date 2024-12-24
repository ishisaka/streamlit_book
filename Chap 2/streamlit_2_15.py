"""例2-15"""

import streamlit as st

st.title("session_stateを使う場合")

# ボタンをクリックしていない状態の場合には、session_stateのcountを0に設定
if "count" not in st.session_state:
    st.session_state["count"] = 0


test = st.button("Test")

if test:
    st.session_state["count"] += 1

st.write("session_state使用 -> ", st.session_state["count"])

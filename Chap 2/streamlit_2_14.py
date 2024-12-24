import streamlit as st

st.title("session_stateを使わない場合")
count = 0

test = st.button("Test")

if test:
    count += 1

st.write("session_state未使用 -> ", count)

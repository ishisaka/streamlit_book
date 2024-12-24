import streamlit as st
from functions.multi_pages import multi_page

multi_page()

# タイトルとテキストを追加
st.title("初めてのStreamlit!")
st.write("Streamlitでアプリを作成しよう！")

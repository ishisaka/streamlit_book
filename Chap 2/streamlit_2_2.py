import streamlit as st

# ページの設定
st.set_page_config(
    page_title="Streamlitアプリケーション",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config",
        "Report a bug": "https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config",
        "About": "Streamlitでアプリを作成しよう",
    },
)

# タイトルとテキストを追加
st.title("初めてのStreamlit!")
st.write("Streamlitでアプリを作成しよう！")

# 画像を表示
st.image("./static/images/polar_bear.png")

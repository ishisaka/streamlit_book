import base64

import streamlit as st


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


image = "./static/images/polar_bear.jpg"
encoded_image = get_base64_image(image)
css = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-color:rgba(255,255,255,0.4);
    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# タイトルとテキストを追加
st.title("初めてのStreamlit!")
st.write("Streamlitでアプリを作成しよう！")
st.write(
    "背景としてシロクマを表示しているので、文字の後ろにシロクマが表示されています。"
)

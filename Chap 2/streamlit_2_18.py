"""例2-18 st:fragmentを使用したアプリケーション"""

import numpy as np
import pandas as pd
import streamlit as st

st.title("Fragmentの使用例")


# Fragment内での処理を定義
@st.fragment
def fragment_graph():
    trigger = True
    # Fragmentを実行
    if trigger:
        data = pd.DataFrame({"x": range(10), "y": np.random.randn(10)})
        st.line_chart(data)
    trigger = st.button("グラフを更新する")


# Fragmentを使用している場所として二つのカラムを作成
col1, col2 = st.columns(2)

with col1:
    # Fragmentを使用している箇所
    st.header("Fragment使用")
    fragment_graph()

with col2:
    # Fragmentを使用していない箇所
    st.header("Fragment未使用")
    data = pd.DataFrame({"x": range(10), "y": np.random.randn(10)})
    st.line_chart(data)

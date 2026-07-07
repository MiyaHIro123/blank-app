import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="TUS Archery",
    layout="wide"
)

# 左上タイトル
st.markdown("""
<style>
div[data-testid="stAppViewContainer"]::before{
    content:"TUS Archery";
    position:fixed;
    top:15px;
    left:20px;
    font-size:26px;
    font-weight:bold;
    z-index:9999;
}

/* タイトルと重ならないように */
.block-container{
    padding-top:4rem;
}
</style>
""", unsafe_allow_html=True)

# ナビゲーション
page = st_navbar(
    ["射数管理", "ホーム", "カレンダー"],
    selected="ホーム",
)

# ページ表示
st.title(page)
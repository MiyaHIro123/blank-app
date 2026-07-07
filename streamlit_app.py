import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="TUS Archery",
    layout="wide"
)

# CSS
st.markdown("""
<style>
/* 左上タイトル */
.logo{
    position: fixed;
    top: 12px;
    left: 20px;
    font-size: 28px;
    font-weight: bold;
    z-index: 999;
}

/* 本文との余白 */
.block-container{
    padding-top: 4rem;
}
</style>
""", unsafe_allow_html=True)

# 左上タイトル
st.markdown('<div class="logo">TUS Archery</div>', unsafe_allow_html=True)

# ナビゲーション
page = option_menu(
    menu_title=None,
    options=["射数管理", "ホーム", "カレンダー"],
    icons=["bullseye", "house", "calendar"],
    orientation="horizontal",
    default_index=1,
)

# ページ表示
st.title(page)
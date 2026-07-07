import streamlit as st

st.set_page_config(
    page_title="TUS Archery",
    layout="wide",
    initial_sidebar_state="collapsed"  # 最初は閉じた状態
)

# 初期ページ
if "page" not in st.session_state:
    st.session_state.page = "ホーム"

# 左上タイトル
st.markdown(
    "<h1 style='margin-top:0;'>TUS Archery</h1>",
    unsafe_allow_html=True
)

# サイドバー
with st.sidebar:
    st.title("メニュー")

    if st.button("🏠 ホーム", use_container_width=True):
        st.session_state.page = "ホーム"

    if st.button("🎯 射数管理", use_container_width=True):
        st.session_state.page = "射数管理"

    if st.button("📅 カレンダー", use_container_width=True):
        st.session_state.page = "カレンダー"

# ページ表示
st.header(st.session_state.page)
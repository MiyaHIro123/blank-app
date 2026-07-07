import streamlit as st

st.set_page_config(
    page_title="TUS Archery",
    layout="wide"
)

# 初期ページ
if "page" not in st.session_state:
    st.session_state.page = "ホーム"

# CSS
st.markdown("""
<style>
.title{
    font-size:32px;
    font-weight:bold;
    margin-bottom:20px;
}

div.stButton > button{
    width:100%;
    height:45px;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# タイトル
st.markdown('<div class="title">TUS Archery</div>', unsafe_allow_html=True)

# ナビゲーション
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("射数管理"):
        st.session_state.page = "射数管理"

with col2:
    if st.button("ホーム"):
        st.session_state.page = "ホーム"

with col3:
    if st.button("カレンダー"):
        st.session_state.page = "カレンダー"

st.divider()

# ページ表示
st.header(st.session_state.page)
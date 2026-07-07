import streamlit as st

# 初期状態
if "page" not in st.session_state:
    st.session_state.page = "射数管理"

# タイトル表示
st.title(st.session_state.page)

# ページごとの内容（今回は空）
st.write("")

# 下部に余白を作る
st.markdown("<br>" * 15, unsafe_allow_html=True)

# 下部ナビゲーション
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("射数管理", use_container_width=True):
        st.session_state.page = "射数管理"
        st.rerun()

with col2:
    if st.button("タイマー", use_container_width=True):
        st.session_state.page = "タイマー"
        st.rerun()

with col3:
    if st.button("カレンダー", use_container_width=True):
        st.session_state.page = "カレンダー"
        st.rerun()
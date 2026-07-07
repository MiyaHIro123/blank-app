import streamlit as st
import time

st.set_page_config(
    page_title="TUS Archery",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 初期ページ
if "page" not in st.session_state:
    st.session_state.page = "ホーム"

# タイマー用
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

# タイトル
st.title("TUS Archery")

# サイドバー
with st.sidebar:
    st.title("メニュー")

    if st.button("🏠 ホーム", use_container_width=True):
        st.session_state.page = "ホーム"

    if st.button("🎯 射数管理", use_container_width=True):
        st.session_state.page = "射数管理"

    if st.button("⏱️ タイマー", use_container_width=True):
        st.session_state.page = "タイマー"

    if st.button("📅 カレンダー", use_container_width=True):
        st.session_state.page = "カレンダー"

# ページ表示
st.header(st.session_state.page)

# ------------------------
# ホーム
# ------------------------
if st.session_state.page == "ホーム":
    st.write("ホーム画面")

# ------------------------
# 射数管理
# ------------------------
elif st.session_state.page == "射数管理":
    st.write("射数管理画面")

# ------------------------
# タイマー
# ------------------------
elif st.session_state.page == "タイマー":

    minutes = st.number_input(
        "時間（分）",
        min_value=1,
        max_value=60,
        value=2
    )

    if st.button("開始"):
        total = minutes * 60
        placeholder = st.empty()

        for sec in range(total, -1, -1):
            m = sec // 60
            s = sec % 60
            placeholder.metric("残り時間", f"{m:02}:{s:02}")
            time.sleep(1)

        st.success("終了")

# ------------------------
# カレンダー
# ------------------------
elif st.session_state.page == "カレンダー":
    st.write("カレンダー画面")
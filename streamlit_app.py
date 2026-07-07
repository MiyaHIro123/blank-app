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

    # 初期値
    if "today_shots" not in st.session_state:
        st.session_state.today_shots = 0

    if "editing_shots" not in st.session_state:
        st.session_state.editing_shots = False

    st.subheader("今日の射数")

    col1, col2 = st.columns([3, 1])

    with col1:
        if st.session_state.editing_shots:
            new_value = st.number_input(
                "今日の射数",
                min_value=0,
                value=st.session_state.today_shots,
                step=1
            )

            if st.button("保存"):
                st.session_state.today_shots = new_value
                st.session_state.editing_shots = False
                st.rerun()

        else:
            st.markdown(
                f"<h2>{st.session_state.today_shots} 射</h2>",
                unsafe_allow_html=True
            )

    with col2:
        if not st.session_state.editing_shots:
            if st.button("✏️ 編集"):
                st.session_state.editing_shots = True
                st.rerun()

# ------------------------
# タイマー
# ------------------------
elif st.session_state.page == "タイマー":

    # 初期化
    if "remaining" not in st.session_state:
        st.session_state.remaining = 120

    if "running" not in st.session_state:
        st.session_state.running = False

    if "duration" not in st.session_state:
        st.session_state.duration = 120

    st.subheader("タイマー")

    # 時間設定
    minutes = st.selectbox(
        "時間",
        [1, 2, 3, 4, 5],
        index=1
    )

    if st.button("設定"):
        st.session_state.duration = minutes * 60
        st.session_state.remaining = minutes * 60
        st.session_state.running = False

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("▶ Start"):
            st.session_state.running = True

    with col2:
        if st.button("⏸ Stop"):
            st.session_state.running = False

    with col3:
        if st.button("↺ Reset"):
            st.session_state.remaining = st.session_state.duration
            st.session_state.running = False

    progress = st.session_state.remaining / st.session_state.duration
    st.progress(progress)

    m = st.session_state.remaining // 60
    s = st.session_state.remaining % 60

    st.markdown(
        f"<h1 style='text-align:center'>{m:02}:{s:02}</h1>",
        unsafe_allow_html=True
    )

    if st.session_state.running:
        time.sleep(1)
        st.session_state.remaining -= 1

        if st.session_state.remaining <= 0:
            st.session_state.remaining = 0
            st.session_state.running = False
            st.success("終了！")

        st.rerun()
# ------------------------
# カレンダー
# ------------------------
elif st.session_state.page == "カレンダー":
    st.write("カレンダー画面")
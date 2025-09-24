import streamlit as st

# 페이지 설정 (더 넓은 레이아웃 사용)
st.set_page_config(layout="wide")

st.title("📋 나만의 클립보드 앱")
st.write("자주 사용하는 텍스트나 이모티콘을 저장하고 쉽게 복사하세요.")

# st.session_state를 사용하여 앱 재실행 시에도 데이터 유지
if 'my_clips' not in st.session_state:
    st.session_state.my_clips = ["안녕하세요! 👋", "반갑습니다. 😊", "streamlit은 정말 편리해요! ✨"]

# --- 입력 부분 ---
st.header("새로운 내용 추가하기")
new_item = st.text_input("자주 사용하는 이모티콘이나 텍스트를 입력하세요:", label_visibility="collapsed", placeholder="여기에 내용을 입력하고 '추가하기'를 누르세요.")

if st.button("추가하기"):
    if new_item and new_item not in st.session_state.my_clips:
        # 새로운 항목을 리스트의 맨 앞에 추가
        st.session_state.my_clips.insert(0, new_item)
        st.success("새로운 항목이 추가되었습니다!")
    elif not new_item:
        st.warning("추가할 내용을 입력해주세요.")
    else:
        st.info("이미 목록에 있는 항목입니다.")

st.divider() # 구분선 추가

# --- 저장된 목록 보여주기 ---
st.header("저장된 목록")

if not st.session_state.my_clips:
    st.info("아직 저장된 항목이 없습니다. 새로운 내용을 추가해보세요!")
else:
    # 3개의 컬럼으로 나누어 표시
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    # enumerate를 사용하여 각 항목의 인덱스(번호)를 가져옴
    for i, item in enumerate(st.session_state.my_clips):
        # 현재 항목을 표시할 컬럼 선택 (순환)
        current_col = columns[i % 3]
        
        with current_col:
            st.code(item, language="")
            # 각 항목마다 고유한 key를 가진 삭제 버튼 생성
            if st.button("삭제", key=f"delete_{i}"):
                # 해당 인덱스의 항목을 리스트에서 제거
                st.session_state.my_clips.pop(i)
                # 삭제 후 앱을 즉시 새로고침하여 목록을 업데이트
                st.rerun()
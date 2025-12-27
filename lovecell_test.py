import streamlit as st
import time
from PIL import Image

# --------------------------------------------------------------------------
# [설정 구역]
# --------------------------------------------------------------------------
page_title = "연애 세포 생존 테스트 v2"
main_title = "💘 2025년 나의 연애 세포 진단"
# 👇 사장님 제휴 링크
link_cpa = "https://www.google.com" 
link_coupang = "https://www.naver.com"
# --------------------------------------------------------------------------

# 1. 기본 디자인 및 배너 설정
st.set_page_config(page_title=page_title, page_icon="💘", layout="centered")

# 메인 배너 (jpg -> png 변경)
try:
    banner_img = Image.open("images/main_banner.png")
    st.image(banner_img, use_container_width=True)
except:
    st.warning("images 폴더에 main_banner.png 파일이 없습니다.")

st.title(main_title)
st.write("무뎌진 감각을 깨워드립니다. 솔직하게 답해주세요.")
st.write("---")

# 2. 점수 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0

# 3. 질문 리스트 (Subheader 삭제 + png 변경)
with st.form("my_form"):
    score = 0 
    
    # 질문 1
    # st.subheader 삭제됨
    try: 
        st.image(Image.open("images/q1.png"), caption="Q1. 금요일 밤 퇴근길", use_container_width=True)
    except: pass
    
    q1 = st.radio("당신의 선택은?", 
                  ("A. '아 기 빨려... 집 가서 씻고 맥주나 한 캔 해야지'", 
                   "B. '오늘 좀 꾸몄는데 아까운데? 친구들한테 연락해볼까?'"),
                  key="q1")
    if q1.startswith("B"):
        score += 30

    st.write("---") 

    # 질문 2
    # st.subheader 삭제됨
    try: 
        st.image(Image.open("images/q2.png"), caption="Q2. 답장 없는 카톡", use_container_width=True)
    except: pass
    
    q2 = st.radio("당신의 행동은?", 
                  ("A. '바쁜가 보네' 하고 폰 덮고 내 할 일 한다.", 
                   "B. '뭐지? 내가 말실수했나?' 대화 내용을 곱씹어 본다."),
                  key="q2")
    if q2.startswith("B"):
        score += 40

    st.write("---")

    # 질문 3
    # st.subheader 삭제됨
    try: 
        st.image(Image.open("images/q3.png"), caption="Q3. 이상형 발견", use_container_width=True)
    except: pass
    
    q3 = st.radio("당신의 반응은?", 
                  ("A. '죄송합니다' 하고 갈 길 간다. (속으로만 아쉬워함)", 
                   "B. 괜찮으시냐고 물어보며 눈을 맞춘다. (혹시 모를 기회 포착!)"),
                  key="q3")
    if q3.startswith("B"):
        score += 30

    st.write("")
    st.write("---")
    
    # 결과 확인 버튼
    submitted = st.form_submit_button("진단 결과 확인하기 (클릭)", type="primary", use_container_width=True)

# 4. 결과 화면 보여주기
if submitted:
    with st.spinner('당신의 무의식을 스캔 중입니다...'):
        time.sleep(1.5) 
        
    st.header("🔍 분석 결과")
    
    # 결과 이미지도 png로 변경
    if score >= 80:
        try: st.image(Image.open("images/result_high.png"), use_container_width=True)
        except: pass
        st.success("🔥 활활 타오르는 '용광로 세포'")
        st.write("당신은 준비됐습니다! 작은 불씨만 있어도 바로 사랑에 빠질 상태입니다.")
        st.write("지금 당신에게 필요한 건 '만남의 기회' 뿐입니다.")
        
    elif score >= 40:
        try: st.image(Image.open("images/result_mid.png"), use_container_width=True)
        except: pass
        st.warning("🛌 이불 밖은 위험해 '동면 세포'")
        st.write("연애의 설렘은 그립지만, 새로운 시작이 귀찮은 상태입니다.")
        st.write("억지로 깨우지 않으면 영영 잠들 수도 있습니다.")
        
    else:
        try: st.image(Image.open("images/result_low.png"), use_container_width=True)
        except: pass
        st.error("🧊 꽁꽁 얼어붙은 '빙하기 세포'")
        st.write("혼자가 너무 편해지셨군요. 연애 세포가 생존 본능을 잃었습니다.")
        st.write("이대로 방치하면 영구 동토층이 됩니다. 긴급 처방이 필요합니다.")

    st.write("---")
    
    # 💰 [수익화 버튼 구역]
    st.subheader("👇 당신을 위한 맞춤 처방전")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("💎 내 미래 배우자 얼굴보기", link_cpa, use_container_width=True)
        st.caption("▲ 전문 매니저의 분석")
        
    with col2:
        st.link_button("📚 죽은 세포 살리는 추천책", link_coupang, use_container_width=True)
        st.caption("▲ 베스트셀러 바로가기")
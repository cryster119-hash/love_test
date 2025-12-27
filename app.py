import streamlit as st
import time
import hashlib
import datetime

# --------------------------------------------------------------------------
# [설정 구역]
# --------------------------------------------------------------------------
page_title = "2026년 신년 연애운"
main_title = "2026년(병오년) 나의 연애운세"
sub_title = "이름과 생년월일로 보는 나의 내년 로맨스"

# 👇 사장님 수익화 링크
link_lucky_item = "https://iryan.kr/t74qtfvomr" 
link_dating_app = "https://iryan.kr/t74qtfwyxi"
# 🎁 카카오페이 복채 링크 (추가됨)
link_kakaopay = "https://qr.kakaopay.com/Ej80O3SQW" 
# --------------------------------------------------------------------------

st.set_page_config(page_title=page_title, page_icon="🔮", layout="centered")

st.title(main_title)
st.write(sub_title)
st.write("---")

# 1. 사용자 입력 받기
with st.form("fortune_form"):
    st.write("### 📜 사주 정보를 입력하세요")
    name = st.text_input("이름 (실명)", placeholder="예: 홍길동")
    
    min_date = datetime.date(1950, 1, 1)
    max_date = datetime.date.today()
    default_date = datetime.date(1995, 1, 1)
    
    birth_date = st.date_input(
        "생년월일", 
        value=default_date,
        min_value=min_date,
        max_value=max_date
    )
    
    gender = st.radio("성별", ("남성", "여성"))
    
    st.write("")
    submitted = st.form_submit_button("2026년 운세 확인하기 (클릭)", type="primary", use_container_width=True)

# 2. 운세 로직
def get_fortune_index(name, date):
    unique_string = name + str(date)
    hash_obj = hashlib.md5(unique_string.encode())
    hash_int = int(hash_obj.hexdigest(), 16)
    return hash_int

# 3. 결과 리스트
fortune_results = [
    {
        "type": "💖 도화살 폭발형",
        "title": "가만히 있어도 이성이 꼬인다!",
        "desc": "2026년은 당신의 매력이 정점을 찍는 해입니다. 어딜 가나 시선이 집중되고, 연락처를 묻는 사람이 줄을 섭니다. 다만, 똥파리도 꼬일 수 있으니 옥석을 잘 가려야 합니다.",
        "lucky_color": "핑크색",
        "advice": "자신감을 가지세요. 당신은 충분히 고를 자격이 있습니다.",
        "img": "🔥"
    },
    {
        "type": "💍 운명적 만남형",
        "title": "드디어 결혼할 인연이 나타난다",
        "desc": "오랫동안 기다려온 '그 사람'이 나타납니다. 처음 본 순간 찌릿한 느낌이 올 거예요. 기존에 알던 사이보다는 새로운 모임이나 여행지에서 만날 확률이 높습니다.",
        "lucky_color": "화이트",
        "advice": "집에만 있지 말고 무조건 밖으로 나가세요!",
        "img": "💒"
    },
    {
        "type": "🌧️ 짝사랑 주의보형",
        "title": "감정 소모가 심할 수 있어요",
        "desc": "누군가를 좋아하게 되지만, 상대방의 마음이 애매합니다. 썸만 타다가 끝날 수도 있습니다. 너무 빨리 마음을 주지 말고 천천히 지켜보는 게 좋습니다.",
        "lucky_color": "노란색",
        "advice": "밀당이 필요합니다. 너무 다 퍼주지 마세요.",
        "img": "☂️"
    },
    {
        "type": "💼 일과 사랑 성공형",
        "title": "사내 연애나 일 관련된 만남",
        "desc": "일하는 모습에서 매력을 느끼는 사람이 다가옵니다. 혹은 당신이 존경할 수 있는 능력 있는 사람을 만나게 됩니다. 연애와 커리어 두 마리 토끼를 다 잡을 운세!",
        "lucky_color": "네이비",
        "advice": "프로페셔널한 모습을 보여주세요.",
        "img": "👩‍💻"
    },
    {
        "type": "🧘‍♀️ 나를 사랑하는 해",
        "title": "연애보다는 자기계발이 대박",
        "desc": "솔직히 연애 운은 평범하지만, 금전운과 성취운이 최강입니다. 억지로 연애하려 하기보다 운동하고 돈 버는 데 집중하면, 연말쯤 자연스럽게 수준 높은 인연이 따라옵니다.",
        "lucky_color": "초록색",
        "advice": "지금은 당신의 가치를 높일 타이밍!",
        "img": "💰"
    }
]

# 4. 결과 보여주기
if submitted:
    if name == "":
        st.error("이름을 입력해주세요!")
    else:
        with st.spinner('신령님께 여쭤보는 중입니다...🙏'):
            time.sleep(2) 
        
        idx = get_fortune_index(name, birth_date) % 5 
        result = fortune_results[idx]
        
        st.header(f"🔮 {name}님의 2026년 연애운")
        st.write("---")
        
        st.subheader(f"{result['img']} {result['type']}")
        st.success(f"**{result['title']}**")
        st.write(result['desc'])
        
        st.info(f"🍀 행운의 컬러: **{result['lucky_color']}**")
        st.write(f"💡 **조언:** {result['advice']}")
        
        st.write("---")
        
        st.subheader("👇 당신의 운세를 더 좋게 만들려면?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.link_button("내 MBTI와 딱 맞는 사람은 어디있을까?", link_lucky_item, use_container_width=True)
            st.caption("▲ 평생 나의 짝꿍 찾기")
            
        with col2:
            st.link_button("에겐 vs 테토, 내 연애 스타일은?", link_dating_app, use_container_width=True)
            st.caption("▲ 나도 모르는 내 연애성향 확인하기")

        # ------------------------------------------------------------------
        # 💰 [새로 추가된 복채 구역]
        # ------------------------------------------------------------------
        st.write("")
        st.write("")
        st.write("---")
        st.markdown("<h3 style='text-align: center;'>🧧 신령님께 드리는 소액 복채</h3>", unsafe_allow_status=True)
        st.markdown("<p style='text-align: center; color: gray;'>운세가 맘에 드셨나요? <br> 주말 반납하고 앱 만든 직장인에게 카페인을 선물해주세요! ☕</p>", unsafe_allow_status=True)
        
        # 중앙 정렬을 위한 컬럼 배치
        _, btn_col, _ = st.columns([1, 2, 1])
        with btn_col:
            st.link_button("🍬 복채 500원 보내기 (카카오페이)", link_kakaopay, use_container_width=True)
            st.caption("<p style='text-align: center;'>복채를 내면 2026년 운이 +100% 상승합니다 (아마도..)</p>", unsafe_allow_status=True)
"""
예제 2: 캐릭터 챗봇
====================================
실행: streamlit run example_2_character.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="캐릭터 챗봇", page_icon="🎭")
st.title("🎭 캐릭터 챗봇")
st.caption("다양한 캐릭터와 대화해보세요!")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.9)

# 캐릭터 정의
characters = {
    "친구 (반말)": {
        "system": "너는 친근한 친구야. 반말로 편하게 대답해. 이모티콘도 많이 써! 😊",
        "icon": "👋"
    },
    "해적": {
        "system": "너는 거친 바다를 누비는 해적 선장이야. '~다'나 '~이다' 같은 해적 말투를 써. 항상 모험과 보물 이야기를 좋아해.",
        "icon": "🏴‍☠️"
    },
    "로봇": {
        "system": "당신은 정중한 AI 로봇입니다. '~입니다', '~것으로 분석됩니다' 같은 로봇 말투를 사용합니다. 논리적이고 정확한 답변을 제공합니다.",
        "icon": "🤖"
    },
    "요리사": {
        "system": "당신은 열정적인 셰프입니다. 음식과 요리에 대한 이야기를 좋아하고, 맛있는 요리 팁을 자주 줍니다. '맛있는', '훌륭한' 같은 표현을 자주 씁니다.",
        "icon": "👨‍🍳"
    }
}

# 사이드바
with st.sidebar:
    st.header("🎭 캐릭터 선택")
    selected_character = st.selectbox(
        "누구와 대화할까요?",
        list(characters.keys())
    )
    
    st.info(f"{characters[selected_character]['icon']} {selected_character}를 선택했습니다!")
    
    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("💡 Model I/O + Prompt Template + Memory를 활용한 예제입니다!")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
if user_input := st.chat_input("메시지를 입력하세요..."):
    # 사용자 메시지 저장 및 표시
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # AI 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("답변 중..."):
            # 메시지 변환
            messages = [HumanMessage(content=characters[selected_character]["system"])]
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                else:
                    messages.append(AIMessage(content=msg["content"]))
            
            response = model.invoke(messages)
            st.write(response.content)
    
    # AI 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": response.content})


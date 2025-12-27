"""
나만의 챗봇 만들기 템플릿
====================================
아래 코드를 수정해서 나만의 챗봇을 만들어보세요!

실행 방법:
streamlit run my_chatbot_template.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ============================================
# 1. 페이지 설정 (제목, 아이콘 등)
# ============================================
st.set_page_config(
    page_title="나만의 챗봇",  # 👈 여기를 수정하세요!
    page_icon="🤖",  # 👈 원하는 이모지로 바꾸세요!
)

st.title("🤖 나만의 AI 챗봇")  # 👈 제목을 수정하세요!
st.caption("LangChain으로 만든 나만의 챗봇입니다")  # 👈 설명을 수정하세요!


# ============================================
# 2. AI 모델 설정
# ============================================
model = ChatOpenAI(
    model="gpt-4.1-mini",  # 변경하지 마세요.
    temperature=0.7,  # 0~1 (높을수록 창의적)
)


# ============================================
# 3. 프롬프트 템플릿 설정 (챗봇의 성격)
# ============================================
# 👇 챗봇의 성격과 역할을 정의하세요!
system_prompt = """
당신은 친절한 AI 어시스턴트입니다.
사용자의 질문에 정확하고 도움이 되는 답변을 제공합니다.
"""

# 👆 이 부분을 수정해서 챗봇의 성격을 바꿔보세요!
# 예시:
# - "당신은 재미있는 농담을 하는 코미디언입니다."
# - "당신은 친구처럼 반말로 대답하는 AI입니다."
# - "당신은 영어 선생님입니다. 항상 영어로 답변하세요."


# ============================================
# 4. 세션 상태 초기화 (메모리)
# ============================================
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 시스템 프롬프트를 첫 메시지로 저장
    st.session_state.messages.append(
        {"role": "system", "content": system_prompt}
    )


# ============================================
# 5. 사이드바 (추가 기능)
# ============================================
with st.sidebar:
    st.header("⚙️ 설정")
    
    # 대화 초기화 버튼
    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = [
            {"role": "system", "content": system_prompt}
        ]
        st.rerun()
    
    st.divider()
    
    # 통계
    message_count = len([m for m in st.session_state.messages if m["role"] != "system"])
    st.metric("총 대화 수", message_count)
    
    st.divider()
    
    st.caption("💡 팁: 챗봇의 성격을 바꾸려면 코드에서 system_prompt를 수정하세요!")


# ============================================
# 6. 대화 내역 표시
# ============================================
for message in st.session_state.messages:
    if message["role"] == "system":
        continue  # 시스템 메시지는 표시하지 않음
    
    with st.chat_message(message["role"]):
        st.write(message["content"])


# ============================================
# 7. 사용자 입력 처리
# ============================================
if user_input := st.chat_input("메시지를 입력하세요..."):  # 👈 placeholder 수정 가능
    
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.write(user_input)
    
    # AI 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):  # 👈 로딩 메시지 수정 가능
            
            # LangChain 메시지 형식으로 변환
            messages = []
            for msg in st.session_state.messages:
                if msg["role"] == "system":
                    continue
                elif msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(AIMessage(content=msg["content"]))
            
            # 시스템 프롬프트와 함께 전달
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                *[(m.type, m.content) for m in messages]
            ])
            
            chain = prompt | model
            response = chain.invoke({})
            
            # 응답 표시
            st.write(response.content)
    
    # AI 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": response.content})


# ============================================
# 8. 하단 정보
# ============================================
st.divider()
st.caption("이 템플릿을 수정해서 나만의 챗봇을 만들어보세요.")


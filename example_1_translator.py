"""
예제 1: 번역기 챗봇
====================================
실행: streamlit run example_1_translator.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="AI 번역기", page_icon="🌍")
st.title("🌍 AI 번역기")
st.caption("어떤 언어든 번역해드립니다!")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)

# 번역 프롬프트 템플릿
translation_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 전문 번역가입니다. 정확하고 자연스러운 번역을 제공합니다."),
    ("human", "다음 문장을 {target_language}로 번역해주세요:\n\n{text}")
])

chain = translation_template | model

# 사이드바
with st.sidebar:
    st.header("⚙️ 번역 설정")
    target_language = st.selectbox(
        "번역할 언어 선택",
        ["영어", "일본어", "중국어", "스페인어", "프랑스어", "독일어"]
    )
    
    st.divider()
    st.caption("💡 Prompt Template을 활용한 예제입니다!")

# 메인
text_input = st.text_area("번역할 문장을 입력하세요:", height=150)

if st.button("🔄 번역하기", type="primary"):
    if text_input:
        with st.spinner(f"{target_language}로 번역 중..."):
            response = chain.invoke({
                "text": text_input,
                "target_language": target_language
            })
            
            st.success("번역 완료!")
            st.write("### 번역 결과:")
            st.info(response.content)
    else:
        st.warning("번역할 문장을 입력해주세요!")


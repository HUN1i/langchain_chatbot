"""
예제 3: 문서 기반 Q&A 챗봇 (RAG)
====================================
실행: streamlit run example_3_qna.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

st.set_page_config(page_title="문서 Q&A", page_icon="📚")
st.title("📚 문서 기반 Q&A 챗봇")
st.caption("문서 내용을 기반으로 질문에 답변합니다!")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)

# 예제 문서 (실제로는 PDF, TXT 등에서 불러올 수 있음)
sample_documents = [
    """
    Python 기초
    - Python은 1991년 귀도 반 로섬이 개발한 프로그래밍 언어입니다.
    - 배우기 쉽고 읽기 쉬운 문법이 특징입니다.
    - 웹 개발, 데이터 분석, 인공지능 등 다양한 분야에서 사용됩니다.
    - 변수 선언 시 타입을 명시하지 않아도 됩니다.
    """,
    """
    Python 자료구조
    - 리스트(List): 순서가 있는 변경 가능한 자료구조 [1, 2, 3]
    - 튜플(Tuple): 순서가 있는 변경 불가능한 자료구조 (1, 2, 3)
    - 딕셔너리(Dictionary): 키-값 쌍으로 이루어진 자료구조 {"key": "value"}
    - 세트(Set): 중복을 허용하지 않는 자료구조 {1, 2, 3}
    """,
    """
    Python 함수
    - def 키워드를 사용하여 함수를 정의합니다.
    - return 문으로 값을 반환할 수 있습니다.
    - 매개변수에 기본값을 설정할 수 있습니다.
    - 람다 함수로 간단한 함수를 한 줄로 작성할 수 있습니다.
    예시: lambda x: x + 1
    """
]

# 사이드바
with st.sidebar:
    st.header("⚙️ 설정")
    
    st.write("### 📄 현재 문서")
    st.info(f"총 {len(sample_documents)}개의 문서가 로드되었습니다.")
    
    st.divider()
    st.caption("💡 RAG (Retriever)를 활용한 예제입니다!")

# 벡터 데이터베이스 초기화
@st.cache_resource
def init_vectorstore():
    documents = [Document(page_content=doc) for doc in sample_documents]
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="\n")
    split_docs = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        collection_name="python_docs"
    )
    return vectorstore

# 초기화
with st.spinner("문서 준비 중..."):
    vectorstore = init_vectorstore()

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# RAG 체인
template = """다음 문서 내용을 참고해서 질문에 답변해주세요.
문서에 정보가 없으면 "문서에서 관련 정보를 찾을 수 없습니다"라고 답변하세요.

문서 내용:
{context}

질문: {question}

답변:"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# 메인
st.write("### 💬 질문하기")
st.caption("예시: Python은 언제 만들어졌어? / 리스트와 튜플의 차이는?")

question = st.text_input("질문을 입력하세요:")

if st.button("🔍 검색 및 답변", type="primary"):
    if question:
        with st.spinner("문서를 검색하고 답변을 생성하는 중..."):
            # 관련 문서 찾기
            relevant_docs = retriever.invoke(question)
            
            # 답변 생성
            answer = rag_chain.invoke(question)
            
            st.success("답변 완료!")
            st.write("### 📝 답변:")
            st.info(answer)
            
            # 참고 문서 표시
            with st.expander("📚 참고한 문서 보기"):
                for i, doc in enumerate(relevant_docs, 1):
                    st.write(f"**문서 {i}:**")
                    st.write(doc.page_content)
                    st.divider()
    else:
        st.warning("질문을 입력해주세요!")


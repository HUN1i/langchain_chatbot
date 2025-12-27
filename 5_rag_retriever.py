"""
5. RAG (Retriever) - 검색 증강 생성
RAG는 문서를 검색해서 AI가 그 내용을 기반으로 답변하는 것!
AI가 모르는 정보를 가르쳐줄 수 있다.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

print("=" * 50)
print("RAG - 학교 규칙 챗봇")
print("=" * 50)

# 학교 규칙 문서
school_documents = [
    """
    우리 학교 급식 규칙
    - 점심 급식 시간: 12시 30분 ~ 1시 30분
    - 급식실 위치: 3층 대강당 옆
    - 급식 신청은 전날까지 해야 함
    """,
    """
    우리 학교 도서관 이용 규칙
    - 운영 시간: 평일 오전 8시 ~ 오후 6시
    - 대출 가능 권수: 1인당 최대 3권
    - 대출 기간: 2주
    - 연체 시 하루당 100원의 연체료 부과
    """,
    """
    우리 학교 컴퓨터실 사용 규칙
    - 사용 가능 시간: 평일 오후 3시 ~ 5시
    - 게임 및 유해 사이트 접속 금지
    - 사용 후 자리 정리 필수
    """,
]

print("\n문서 준비 중...")
documents = [Document(page_content=doc) for doc in school_documents]

# 텍스트 분할
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="\n")
split_docs = text_splitter.split_documents(documents)

# 벡터 데이터베이스 생성
print("벡터 데이터베이스 생성 중...")
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    collection_name="school_rules"
)

# RAG 체인 생성
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 프롬프트 템플릿
template = """다음 문서 정보를 참고해서 질문에 답변해줘.
문서에 정보가 없으면 "문서에서 관련 정보를 찾을 수 없습니다"라고 답변해.

문서 내용:
{context}

질문: {question}

답변:"""

prompt = ChatPromptTemplate.from_template(template)

# RAG 체인: 검색 → 프롬프트 → 모델 → 파서
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print("준비 완료!\n")
print("학교 규칙에 대해 질문하세요 (종료: 'quit')")
print("예시: 급식 시간이 언제야? / 도서관에서 책을 몇 권까지 빌릴 수 있어?\n")

# 사용자 질문 받기
while True:
    question = input("질문: ")
    
    if question.lower() == 'quit':
        print("\n챗봇을 종료합니다.")
        break
    
    result = rag_chain.invoke(question)
    print(f"답변: {result}\n")

print("\n" + "=" * 50)
print("과정: 문서 준비 → 벡터화 → 검색 → 답변")
print("=" * 50)


"""
3. Chain & Parser - 체인과 파서
Chain: 작업을 레고처럼 연결 (prompt | model | parser)
Parser: 더러운 문자열을 깨끗한 데이터로 정제
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

print("=" * 50)
print("Chain & Parser - 리스트 파서 예제")
print("=" * 50)

# 사용자 입력
subject = input("\n어떤 주제의 목록을 받고 싶나요? (예: 프로그래밍 언어, 과일, 영화 등): ")

# 리스트 파서
list_parser = CommaSeparatedListOutputParser()

# 프롬프트 템플릿
prompt = ChatPromptTemplate.from_template(
    "{subject}의 종류를 5가지만 알려줘. {format_instructions}"
)

# Chain: 프롬프트 → 모델 → 파서 (파이프로 연결!)
chain = prompt | model | list_parser

# 실행
print("\n처리 중...")
result = chain.invoke({
    "subject": subject,
    "format_instructions": list_parser.get_format_instructions()
})

print("\n" + "-" * 50)
print(f"{subject} 목록:")
for i, item in enumerate(result, 1):
    print(f"  {i}. {item.strip()}")

print(f"\n데이터 타입: {type(result)}")

print("\n" + "=" * 50)
print("=" * 50)


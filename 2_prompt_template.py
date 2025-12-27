"""
2. Prompt Template - 프롬프트 템플릿
프롬프트 템플릿은 '설계도'! 값만 바꿔 끼우면 된다.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

print("=" * 50)
print("Prompt Template - 번역 템플릿")
print("=" * 50)

# 번역 템플릿 만들기
translation_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 전문 번역가입니다."),
    ("human", "다음 문장을 {target_language}로 번역해주세요: {text}")
])

# 사용자 입력
text = input("\n번역할 문장을 입력하세요: ")
language = input("어떤 언어로 번역할까요? ")

# 템플릿에 값 넣기
messages = translation_template.format_messages(
    text=text,
    target_language=language
)

# 번역 실행
response = model.invoke(messages)
print("\n" + "-" * 50)
print(f"번역 결과: {response.content}")

print("\n" + "=" * 50)
print("=" * 50)


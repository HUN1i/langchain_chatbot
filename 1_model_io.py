"""
1. Model I/O - 모델 입출력
모델을 바꾸면 API가 어떻게 달라지는지 확인해보자!
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

print("=" * 50)
print("Model I/O - 같은 질문, 다른 AI 모델")
print("=" * 50)

# OpenAI 모델
openai_model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

# Google 모델
google_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# 사용자 입력 받기
question = input("\n질문을 입력하세요: ")

print("\n" + "-" * 50)
openai_response = openai_model.invoke(question)
print(f"OpenAI 답변:\n{openai_response.content}")

print("\n" + "-" * 50)
google_response = google_model.invoke(question)
print(f"Google 답변:\n{google_response.content}")

print("\n" + "=" * 50)
print("=" * 50)


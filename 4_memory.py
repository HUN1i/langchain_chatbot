"""
4. Memory - 메모리 (대화 기억하기)
메모리를 사용하면 AI가 이전 대화를 기억한다!
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

print("=" * 50)
print("Memory - AI와 대화하기 (종료: 'quit')")
print("=" * 50)

# 대화 기록을 저장할 리스트
chat_history = []

print("\nAI와 대화를 시작하세요!")
print("예시: '내 이름은 철수야' → '내 이름이 뭐였지?'\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("\n대화를 종료합니다.")
        break
    
    # 이전 대화 기록을 포함해서 AI에게 전달
    messages = chat_history + [HumanMessage(content=user_input)]
    response = model.invoke(messages)
    
    # 대화 기록에 추가
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))
    
    print(f"AI: {response.content}\n")

# 저장된 대화 확인
print("\n" + "=" * 50)
print("저장된 대화 내역:")
print("-" * 50)
for msg in chat_history:
    if isinstance(msg, HumanMessage):
        print(f"You: {msg.content}")
    else:
        print(f"AI: {msg.content}")

print("\n" + "=" * 50)
print("=" * 50)


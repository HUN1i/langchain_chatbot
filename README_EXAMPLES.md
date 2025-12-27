# 🎯 나만의 챗봇 만들기

## 📚 학습한 내용 복습

5개의 실습을 통해 배운 내용:

1. **Model I/O** - AI 모델과 대화하기
2. **Prompt Template** - 프롬프트 설계도 만들기
3. **Chain & Parser** - 작업 연결하고 데이터 정제
4. **Memory** - 대화 기억하기
5. **RAG** - 문서 검색 후 답변하기

---

## 🚀 Streamlit으로 웹 챗봇 만들기

### 설치

```bash
pip install streamlit
```

### 실행 방법

```bash
streamlit run 파일명.py
```

---

## 📂 제공된 파일들

### 1. `my_chatbot_template.py` - 기본 템플릿

**가장 기본적인 챗봇 템플릿**

실행:

```bash
streamlit run my_chatbot_template.py
```

**수정할 부분:**

- 페이지 제목 & 아이콘
- 챗봇 성격 (system_prompt)
- 모델 설정 (temperature 등)

**활용 개념:** Model I/O, Prompt Template, Memory

---

### 2. `example_1_translator.py` - 번역기

**여러 언어로 번역해주는 챗봇**

실행:

```bash
streamlit run example_1_translator.py
```

**특징:**

- 사이드바에서 언어 선택
- Prompt Template 활용
- 깔끔한 번역 결과 표시

**활용 개념:** Prompt Template, Chain

---

### 3. `example_2_character.py` - 캐릭터 챗봇

**다양한 캐릭터와 대화하는 챗봇**

실행:

```bash
streamlit run example_2_character.py
```

**특징:**

- 친구, 해적, 로봇, 요리사 캐릭터
- 대화 기록 저장
- 캐릭터별 다른 말투

**활용 개념:** Model I/O, Prompt Template, Memory

---

### 4. `example_3_qna.py` - 문서 Q&A

**문서 내용을 기반으로 답변하는 챗봇**

실행:

```bash
streamlit run example_3_qna.py
```

**특징:**

- Python 문서 기반 질문 답변
- 참고한 문서 표시
- RAG 시스템 활용

**활용 개념:** RAG (Retriever), Chain, Parser

---

## 💡 나만의 챗봇 만들기 아이디어

### 초급

1. **감정 분석 챗봇**

   - 사용자의 메시지를 분석해서 감정을 알려줌
   - Parser로 JSON 형태로 결과 받기

2. **퀴즈 챗봇**

   - 문제를 내고 정답 체크
   - Memory로 점수 기록

3. **일기 작성 도우미**
   - 오늘 있었던 일을 입력하면 멋진 일기로 다듬어줌

### 중급

4. **학습 도우미**

   - 과목별 문제 풀이 설명
   - 학생 수준에 맞춰 설명

5. **영어 회화 연습**

   - 영어로 대화 연습
   - 틀린 문법 교정

6. **코딩 선생님**
   - 프로그래밍 질문에 답변
   - 코드 예제 제공

### 고급

7. **책 내용 Q&A**

   - PDF 책을 업로드하면 RAG로 질문 답변
   - 문서 기반 검색

8. **회의록 요약기**

   - 긴 텍스트를 입력하면 요약
   - 핵심 포인트 추출

9. **멀티 에이전트 챗봇**
   - 여러 AI가 협력해서 답변
   - 각자 다른 역할 수행

---

## 🎨 Streamlit 주요 기능

### 기본 요소

```python
st.title("제목")
st.header("헤더")
st.write("일반 텍스트")
st.caption("작은 글씨")
```

### 입력

```python
st.text_input("입력:")
st.text_area("여러 줄 입력:")
st.button("버튼")
st.selectbox("선택", ["옵션1", "옵션2"])
```

### 레이아웃

```python
st.sidebar.write("사이드바")
st.columns(2)  # 2개 컬럼
st.tabs(["탭1", "탭2"])  # 탭
```

### 채팅 UI

```python
st.chat_message("user").write("메시지")
st.chat_input("입력...")
```

### 알림

```python
st.success("성공!")
st.info("정보")
st.warning("경고")
st.error("오류")
```

---

## 📝 템플릿 수정 가이드

### 1단계: 기본 설정

```python
# 페이지 설정
st.set_page_config(
    page_title="내 챗봇",
    page_icon="🤖"
)
```

### 2단계: 챗봇 성격 정의

```python
system_prompt = """
당신은 ___입니다.
___한 말투로 대답합니다.
"""
```

### 3단계: 추가 기능

- 사이드바에 옵션 추가
- 통계 표시
- 파일 업로드 등

### 4단계: 스타일링

```python
st.markdown("""
<style>
/* CSS로 스타일 변경 */
</style>
""", unsafe_allow_html=True)
```

---

## 🎓 학습 흐름

1. **실습 코드 실행** (1~5번 파일)

   - 각 개념 이해하기

2. **템플릿 실행** (my_chatbot_template.py)

   - 기본 구조 파악하기

3. **예제 실행** (example\_\*.py)

   - 다양한 활용법 보기

4. **나만의 챗봇 만들기**
   - 템플릿 복사해서 수정하기
   - 원하는 기능 추가하기

---

## 💬 도움말

### 오류가 발생하면?

1. API 키 확인 (.env 파일)
2. 패키지 재설치
3. 터미널에서 오류 메시지 확인

### 더 배우고 싶다면?

- [Streamlit 문서](https://docs.streamlit.io/)
- [LangChain 문서](https://python.langchain.com/)

---

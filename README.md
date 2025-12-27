# 🤖 LangChain 실습 코드

LangChain의 핵심 개념을 배우는 5개의 실습 파일입니다.

## 📚 목차

1. **Model I/O** (`1_model_io.py`) - AI 모델 사용하기
2. **Prompt Template** (`2_prompt_template.py`) - 프롬프트 설계도 만들기
3. **Chain & Parser** (`3_chain_parser.py`) - 작업 연결하고 데이터 정제하기
4. **Memory** (`4_memory.py`) - 대화 기억하기
5. **RAG** (`5_rag_retriever.py`) - 문서 검색해서 답변하기

## 🚀 시작하기

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. API 키 설정

`.env` 파일을 만들고 API 키를 입력하세요:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. 실습 코드 실행

각 파일을 순서대로 실행해보세요:

```bash
python 1_model_io.py
python 2_prompt_template.py
python 3_chain_parser.py
python 4_memory.py
python 5_rag_retriever.py
```

## 📖 각 파일 설명

### 1️⃣ Model I/O (1_model_io.py)

- ChatOpenAI vs ChatGoogleGenerativeAI 비교
- API가 어떻게 다른지 확인
- temperature로 창의성 조절하기

### 2️⃣ Prompt Template (2_prompt_template.py)

- 프롬프트 템플릿 = 설계도
- 변수를 사용해서 값만 바꿔 끼우기
- 번역, 캐릭터 대화 등 실용 예제

### 3️⃣ Chain & Parser (3_chain_parser.py)

- Chain: 작업을 레고 블록처럼 연결
- Parser: 지저분한 문자열을 깔끔한 데이터로 정제
- StrOutputParser, JsonOutputParser, ListOutputParser 사용

### 4️⃣ Memory (4_memory.py)

- AI가 이전 대화를 기억하게 만들기
- ConversationBufferMemory: 전체 기억
- ConversationBufferWindowMemory: 최근 N개만 기억
- ConversationSummaryMemory: 요약해서 기억

### 5️⃣ RAG - Retriever (5_rag_retriever.py)

- AI가 모르는 정보를 가르쳐주기
- 문서 → 벡터화 → 검색 → 답변 생성
- 학교 규칙 챗봇 예제

## 🎯 학습 목표

- LangChain의 핵심 개념 5가지 이해하기
- 실제로 동작하는 AI 챗봇 만들어보기
- 프롬프트 엔지니어링 기초 다지기
- RAG로 AI에게 새로운 지식 가르치기

## 🔧 문제 해결

### API 키 오류

- `.env` 파일이 제대로 만들어졌는지 확인
- API 키가 올바르게 입력되었는지 확인

### 패키지 설치 오류

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 실행 오류

- Python 3.8 이상 버전인지 확인
- 필요한 패키지가 모두 설치되었는지 확인

## 📝 추가 학습 자료

- [LangChain 공식 문서](https://python.langchain.com/)
- [OpenAI API 문서](https://platform.openai.com/docs)
- [Google Generative AI 문서](https://ai.google.dev/)

---

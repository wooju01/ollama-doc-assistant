# 03. Python for AI — AI 서비스 개발을 위한 Python

## 개요

이 강의는 Python 문법을 외우는 과정이 아니다. **AI 서비스를 만들 때 데이터를 읽고, 변환하고, 검증하고, 함수와 객체로 책임을 나누고, 외부 시스템과 데이터를 주고받을 수 있는 Python 코드를 작성하는 능력**을 만드는 과정이다.

앞 과목의 [[React]]가 사용자의 입력과 화면 상태를 다뤘다면, Python은 Backend와 AI 기능의 내부에서 실제 데이터를 처리하는 언어로 사용한다. 다음 과목 [[FastAPI]]에서는 여기서 배운 함수, Type Hint, 객체, 예외, JSON, Decorator, 비동기 개념을 그대로 사용한다.

```text
사용자
  ↓
React
  ↓ HTTP / JSON
FastAPI
  ↓
Python 함수와 객체
  ├─ 입력 검증
  ├─ 데이터 변환
  ├─ 파일 처리
  ├─ AI Provider 호출
  └─ 결과 조립
```

따라서 이 강의의 목표는 "Python을 많이 아는 것"이 아니라 **FastAPI와 AI 서비스 코드를 읽고 직접 구현할 수 있을 정도로 Python을 이해하는 것**이다.

## 학습 목표

학습자는 이 과정을 마친 뒤 다음을 할 수 있어야 한다.

- Python 코드가 어떤 순서로 실행되는지 설명할 수 있다.
- 변수의 이름과 객체, 참조, Mutable/Immutable의 차이를 설명할 수 있다.
- List, Tuple, Dictionary, Set을 상황에 맞게 선택할 수 있다.
- 조건문, 반복문, Comprehension으로 데이터를 가공할 수 있다.
- 함수를 정의하고 매개변수·반환값·Type Hint를 사용할 수 있다.
- 예외를 구분하고 필요한 위치에서 처리할 수 있다.
- Module과 Package로 코드를 분리할 수 있다.
- 파일과 JSON 데이터를 읽고 쓸 수 있다.
- Class, Object, Inheritance, Composition의 역할을 구분할 수 있다.
- Decorator가 함수를 감싸는 구조와 FastAPI에서의 쓰임을 설명할 수 있다.
- `@dataclass`와 일반 Class, Pydantic Model의 역할 차이를 다음 과정과 연결해 이해할 수 있다.
- AI Backend에서 Python이 담당하는 위치를 설명할 수 있다.

## 전체 학습 지도

```text
왜 Python인가
  ↓
Python 실행 구조 / 개발환경
  ↓
이름 · 객체 · 참조 · 자료형
  ↓
조건 · 반복 · Collection
  ↓
함수 · Type Hint · 예외
  ↓
Module · Package
  ↓
File · JSON
  ↓
Class · Object
  ↓
Inheritance · Composition
  ↓
Decorator · Dataclass
  ↓
FastAPI에서 사용할 Python 준비 완료
```

> **학습 원칙**  
> 뒤에서 다시 등장하는 개념이 앞에서 조금 먼저 나와도 괜찮다. Python은 각각의 문법을 따로 암기하는 것보다 같은 개념을 여러 상황에서 반복해서 보는 것이 더 중요하다.

## 수업 환경 기준

- Python: **3.12 계열**
- 가상환경: 프로젝트별 독립 환경 사용
- Editor: VS Code 기준으로 설명하되 다른 Editor를 사용해도 무방
- Package 설치: `pip` 또는 `uv`를 사용하되 프로젝트별 Lock File을 재현 기준으로 관리

이 교육과정의 미니프로젝트와 메인프로젝트는 **Python 3.12 계열을 공통 기준**으로 사용한다. 최신 Python 자체보다 FastAPI·PyTorch·Transformers·Sentence Transformers·OpenAI SDK·LangChain 등 여러 라이브러리를 함께 사용할 때의 호환성과 재현성을 우선한다. 정확한 patch 버전과 패키지 버전은 프로젝트별 Lock File에 고정한다.

---

# Part 1. Python의 원리와 기본 문법

이 Part에서는 Python 코드를 "작성하는 법"뿐 아니라 **왜 그렇게 동작하는지**를 먼저 이해한다. 특히 이름과 객체, 참조, Mutable/Immutable은 이후 List, 함수, Class, FastAPI Request Model을 이해하는 기반이 된다.

## Unit 1. 왜 AI 개발자는 Python을 사용하는가?

---

### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Python은 무엇인가?
- 왜 AI 개발에서는 Python을 가장 많이 사용하는가?
- Python은 AI 서비스에서 어떤 역할을 하는가?
- React, FastAPI와는 어떤 관계인가?
- 앞으로 왜 Python을 먼저 배우는가?

---

### ① 문제 이해 (Why)

#### AI 서비스를 만들려면 무엇부터 필요한가?

앞으로 우리가 만들 AI 서비스에는 다음과 같은 기술이 활용됩니다.

- Transformer
- LLM
- Embedding
- Vector DB
- RAG
- Agent
- OCR
- AI 서비스 아키텍처

이 과정에서는 이러한 기술을 실제 서비스로 구현하기 위한

프로그래밍 기반부터 학습합니다.

이제부터

> **"직접 AI 서비스를 만드는 방법"**

을 배우기 시작합니다.

---

그런데 AI 서비스를 만들려면 가장 먼저 필요한 것이 있습니다.

바로

> **프로그래밍 언어**

입니다.

AI 모델은 스스로 실행되지 않습니다.

누군가가

- 모델을 호출하고
- 데이터를 읽고
- 파일을 저장하고
- 사용자의 요청을 처리해야 합니다.

이 모든 일을 하는 것이

> **프로그래밍 언어**

입니다.

---

#### 왜 Python을 배우는가?

AI 개발을 처음 시작하면 대부분 이런 질문을 합니다.

> Java도 있는데?

> C++도 있는데?

> JavaScript도 있는데?

왜 모두 Python을 사용할까?

---

사실 AI는

**Python으로 만들어진 것이 아닙니다.**

여기서 많은 사람들이 오해합니다.

예를 들어

ChatGPT의 핵심 연산은

GPU 위에서

- CUDA
- C++
- 최적화 라이브러리

등이 수행합니다.

그런데 개발자는 대부분 Python을 사용합니다.

왜일까요?

---

#### AI 개발자가 해야 하는 일

AI 모델을 직접 만드는 사람보다

AI 모델을 활용하는 사람이 훨씬 많습니다.

예를 들어

```
사용자 질문

↓

OpenAI API 호출

↓

응답 받기

↓

응답 저장

↓

웹 화면에 출력
```

여기에는

수학보다

프로그램을 연결하는 일이 훨씬 많습니다.

Python은

바로 이러한

> **연결(Connection)**

을 매우 쉽게 만들어 줍니다.

---

#### 이 과정의 AI 서비스 개발은 연결과 조합의 비중이 크다.

학습자는 AI 개발이라고 하면

이런 장면을 떠올립니다.

```
거대한 AI 모델을 직접 만든다.
```

이 과정은 AI 모델 자체를 연구하거나 학습시키는 역할보다,
기존 모델·API·데이터 처리 도구를 연결해 AI 서비스를 만드는 역할에
초점을 맞춥니다.

예를 들어

```
PDF 업로드

↓

텍스트 추출

↓

LLM 호출

↓

요약 생성

↓

DB 저장

↓

웹 출력
```

여기에는

수십 개의 라이브러리가 연결됩니다.

Python은

이 연결을 가장 쉽게 만드는 언어입니다.

---

#### 비유

Python은

레고를 조립하는 것과 비슷합니다.

레고 블록은 이미 만들어져 있습니다.

우리는

```
OCR

+

LLM

+

Database

+

API

+

Web
```

를 연결하면 됩니다.

Python은

이 레고를 가장 쉽게 조립할 수 있는 언어입니다.

---

### 기존 언어들의 문제

Python 이전에도 좋은 언어는 많았습니다.

예를 들어

```
C
```

장점

- 매우 빠르다.

단점

- 코드가 어렵다.
- 메모리를 직접 관리한다.

---

```
C++
```

장점

- 빠르다.
- 성능이 좋다.

단점

- 문법이 어렵다.
- 배우기 어렵다.

---

```
Java
```

장점

- 안정적이다.

단점

- 코드가 길다.
- AI 라이브러리가 상대적으로 적었다.

---

AI는

실험을 매우 많이 합니다.

```
데이터 변경

↓

모델 변경

↓

결과 확인

↓

다시 수정
```

이 과정을

하루에도 수십 번 반복합니다.

---

Python은

이 반복 작업을

가장 빠르게 할 수 있도록 설계되었습니다.

---

### Python이 등장한 이유

Python은

1991년 **귀도 반 로섬(Guido van Rossum)**이 만들었습니다.

당시에는

이런 생각이 있었습니다.

> "프로그래밍은 사람도 읽기 쉬워야 한다."

이 철학이 지금까지 이어지고 있습니다.

Python은

컴퓨터보다

사람을 위한 언어입니다.

---

#### Python의 철학

Python에는 유명한 철학이 있습니다.

```
Simple is better than complex.

복잡한 것보다
단순한 것이 좋다.
```

또 다른 철학은

```
Readability counts.

읽기 쉬운 코드가 중요하다.
```

입니다.

이 철학 때문에

AI 연구자들이 Python을 매우 좋아하게 됩니다.

---

### AI 분야에서 Python이 표준이 된 이유

AI 연구자들이 원하는 것은

```
빠르게 실험

↓

빠르게 수정

↓

빠르게 검증
```

입니다.

Python은

이 과정을 가장 잘 지원했습니다.

그래서

AI 관련 라이브러리들이

하나둘 Python으로 만들어지기 시작했습니다.

예를 들면

```
NumPy

↓

Pandas

↓

Matplotlib

↓

scikit-learn

↓

TensorFlow

↓

PyTorch

↓

Transformers

↓

LangChain

↓

OpenAI SDK
```

결국

라이브러리가 많아질수록

더 많은 개발자가 Python을 사용하게 되었고,

사용자가 늘어나자

더 많은 라이브러리가 만들어지는

선순환이 형성되었습니다.

---

### AI 서비스에서 Python의 역할

먼저 AI 서비스의 기본 구조를 살펴봅시다.

```
사용자

↓

웹 화면

↓

API 서버

↓

LLM

↓

Vector DB

↓

DB

↓

파일 저장소
```

여기서 Python은 어디에 있을까요?

대부분

API 서버와 AI 처리 계층에서 사용됩니다.

```
            React

              │

              │ HTTP

              ▼

        FastAPI(Python)

              │

      ┌───────┼────────┐

      │       │        │

      ▼       ▼        ▼

    OpenAI   OCR     Database

      │

      ▼

   AI 응답 생성

      │

      ▼

   React로 반환
```

즉,

Python은 **AI 서비스를 실제로 동작시키는 핵심 실행 언어**입니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 Python 문법을 배우지 않았습니다.

먼저

> **왜 Python을 배우는가?**

를 이해했습니다.

핵심은 다음과 같습니다.

- Python은 AI 모델 자체를 만드는 언어라기보다 AI 서비스를 연결하는 언어이다.
- AI 개발의 대부분은 여러 라이브러리와 서비스를 조합하는 작업이다.
- Python은 간결한 문법과 뛰어난 생산성으로 빠른 실험과 개발에 적합하다.
- AI 생태계의 주요 라이브러리들이 Python 중심으로 발전하면서 사실상의 표준 언어가 되었다.
- 앞으로 배우게 될 FastAPI, AI Integration, Document AI도 모두 Python을 기반으로 한다.

---

#### 다음 Unit에서 학습할 내용

다음 Unit에서는 **Python의 기본 문법이 아니라, Python 프로그램이 어떻게 실행되는지와 인터프리터(Interpreter)의 동작 원리, 스크립트 언어의 개념**부터 학습합니다. 이후 변수, 자료형, 함수, 객체 등 실제 AI 개발에 필요한 문법을 원리 중심으로 단계적으로 익혀 나갑니다.

---

## Unit 2. Python은 어떻게 실행되는가?

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 AI 개발자는 Python을 사용하는가? ✅
>
> **Unit 2. Python은 어떻게 실행되는가?** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- Python은 컴퓨터에서 어떻게 실행되는가?
- 컴파일 언어와 인터프리터 언어는 무엇이 다른가?
- Python은 정말 느린 언어인가?
- AI 개발에서는 왜 Python이 충분한가?
- Python 코드가 GPU를 사용하는 과정은 어떻게 되는가?

---

### ① 문제 이해 (Why)

#### 우리는 Python 코드를 작성한다.

예를 들어

```python
print("Hello AI")
```

이 코드를 실행하면

```
Hello AI
```

가 출력됩니다.

여기서 자연스럽게 질문이 하나 생깁니다.

> 컴퓨터는 영어를 이해할까?

답은

**아니오.**

컴퓨터는

오직

```
0과 1
```

만 이해합니다.

그렇다면

우리가 작성한 Python 코드는

어떻게 컴퓨터가 이해하는 언어로 변하는 것일까요?

---

### 사람이 사용하는 언어와 컴퓨터의 언어

사람

↓

Python

↓

???

↓

CPU

---

여기 가운데를 담당하는 것이 있습니다.

바로

> **Python Interpreter(인터프리터)**

입니다.

---

### 인터프리터란?

인터프리터는

한마디로

> **Python 코드를 컴퓨터가 이해할 수 있도록 번역하면서 실행하는 프로그램**

입니다.

즉

우리가 실행하는 것은

Python 코드가 아니라

Python Interpreter입니다.

Interpreter가

Python 파일을 읽어

하나씩 실행하는 것입니다.

---

비유하면

```
한국인

↓

통역사

↓

외국인
```

처럼

Python은

```
개발자

↓

Python Interpreter

↓

컴퓨터
```

구조입니다.

---

### 실행 과정

예를 들어

```python
a = 10
b = 20

print(a + b)
```

실제로는

이런 과정이 발생합니다.

```
Python 코드

↓

Python Interpreter 실행

↓

문법 검사

↓

Byte Code 생성

↓

Python Virtual Machine 실행

↓

CPU 명령 실행

↓

결과 출력
```

생각보다

중간 과정이 많습니다.

---

### Python은 한 줄씩 실행되는가?

많은 입문자가

이렇게 알고 있습니다.

> Python은 한 줄씩 바로 실행된다.

엄밀하게 말하면

조금 다릅니다.

여기서는 우리가 가장 일반적으로 사용하는

**CPython 구현을 기준으로** 설명하겠습니다.

실제로는

```
Python Source

↓

Bytecode

↓

CPython 실행 엔진

↓

CPU
```

과정을 거칩니다.

즉

CPython은

중간 코드(Bytecode)를 먼저 만든 후

실행 엔진이 이를 처리합니다.

가져온 모듈의 Bytecode는 필요에 따라

`__pycache__` 디렉터리에 `.pyc` 파일로 저장될 수 있습니다.

항상 `.pyc` 파일이 먼저 만들어져야 실행되는 것은 아닙니다.

---

### Bytecode란?

Bytecode는

컴퓨터의 기계어는 아닙니다.

또

Python 코드도 아닙니다.

중간 단계의 언어입니다.

예를 들어

```
Python

↓

Bytecode

↓

Machine Code
```

이런 구조입니다.

---

비유하면

```
한국어

↓

영어

↓

프랑스어
```

처럼

중간 언어를 거치는 것입니다.

---

### Python Virtual Machine(PVM)

입문 과정에서는 Bytecode를 처리하는

**CPython의 실행 부분**을

Python Virtual Machine(PVM)이라고 이해할 수 있습니다.

```
Python

↓

Bytecode

↓

PVM

↓

CPU
```

PVM을 별도로 설치하거나 실행하는 것은 아닙니다.

CPython Interpreter 내부에서

Bytecode를 읽고 명령을 수행하는 과정을 설명하기 위한 용어입니다.

---

### 컴파일 언어와 인터프리터 언어

이제 자주 듣는 용어를 이해해봅시다.

---

#### 컴파일 언어

대표적인 언어

```
C

C++

Rust
```

실행 과정

```
Source Code

↓

Compiler

↓

Machine Code

↓

실행
```

프로그램을

미리 모두 번역합니다.

---

장점

- 매우 빠르다.
- 최적화가 뛰어나다.

단점

- 수정할 때마다 다시 컴파일해야 한다.

---

#### 인터프리터 언어

대표적인 언어

```
Python

JavaScript

Ruby
```

실행 과정

```
Source

↓

Interpreter

↓

실행
```

장점

- 개발이 빠르다.
- 수정이 쉽다.
- 실험하기 좋다.

단점

- 일반적으로 컴파일 언어보다 느리다.

---

### 그런데 Python은 정말 느릴까?

정답은

> **Python 자체는 상대적으로 느립니다.**

하지만 AI 개발에서는 핵심 모델 연산이 최적화된 네이티브 코드나 GPU,
또는 외부 API에서 수행되는 경우가 많아 Python 인터프리터의 속도가
항상 가장 큰 병목이 되는 것은 아닙니다.

다만 전처리 코드의 긴 반복문, 대용량 파일 파싱, 동기 I/O처럼
Python에서 직접 처리하는 부분은 충분히 병목이 될 수 있습니다.

왜일까요?

---

### 많은 AI 핵심 연산은 Python 바깥의 최적화 코드가 수행한다.

예를 들어

```python
response = client.responses.create(...)
```

이 예제에서 모델 추론의 핵심 계산은 현재 Python Process가 아니라
외부 AI 서버에서 수행됩니다.

실제로는

```
Python

↓

OpenAI SDK

↓

API 요청

↓

OpenAI Server

↓

GPU

↓

결과 반환
```

입니다.

---

또 다른 예입니다.

```python
import torch
```

이후

```python
tensor.matmul()
```

을 실행하면

실제로 계산하는 것은

Python이 아닙니다.

```
Python

↓

PyTorch

↓

C++

↓

CUDA

↓

GPU
```

입니다.

Python은

명령만 전달합니다.

---

### 비유

Python은

현장 작업자가 아닙니다.

오히려

현장 감독입니다.

```
감독

↓

작업 지시

↓

전문 작업팀

↓

결과 보고
```

AI 개발도 같습니다.

```
Python

↓

NumPy

↓

PyTorch

↓

CUDA

↓

GPU
```

Python은

"이 계산을 수행해."

라고 지시할 뿐입니다.

실제 계산은

최적화된 라이브러리가 수행합니다.

---

### 그래서 Python이 AI에서 강력한 이유

Python은

직접 계산하지 않아도 됩니다.

대신

가장 잘하는 것은

```
라이브러리 연결

↓

데이터 전달

↓

결과 처리
```

입니다.

AI 서비스에서는

바로 이것이 가장 중요합니다.

---

### AI 서비스에서의 실행 흐름

이 구조를 Python의 실행 흐름과 연결해 보면

```
사용자

↓

React

↓

FastAPI(Python)

↓

OpenAI SDK

↓

OpenAI API

↓

LLM

↓

응답

↓

Python

↓

React
```

여기서 Python은

계산 엔진이 아니라

**전체 AI 서비스의 오케스트레이터(Orchestrator)** 역할을 합니다.

즉,

어떤 AI 모델을 호출할지, 어떤 데이터를 전달할지, 결과를 어떻게 후처리할지를 제어하는 중심 역할을 수행합니다.

---

### Python 파일은 어떻게 실행할까?

예를 들어

```python
hello.py
```

라는 파일이 있다면

터미널에서

```bash
python hello.py
```

를 입력합니다.

그러면

```
Python Interpreter 실행

↓

hello.py 읽기

↓

Bytecode 생성

↓

PVM 실행

↓

출력
```

순서로 동작합니다.

이 과정은 매우 빠르게 이루어지므로 우리는 거의 느끼지 못합니다.

---

### Python에는 여러 구현체가 있다.

대부분의 개발자는 하나의 Python만 있다고 생각합니다.

하지만 실제로는 여러 구현체가 존재합니다.

| 구현체     | 특징                                                        |
| ---------- | ----------------------------------------------------------- |
| CPython    | 가장 널리 사용되는 대표 구현체                              |
| PyPy       | JIT(Just-In-Time) 컴파일러를 사용하여 일부 작업에서 더 빠름 |
| Jython     | JVM(Java Virtual Machine) 위에서 실행                       |
| IronPython | .NET 환경에서 실행                                          |

실무에서 AI 개발은 거의 모두 **CPython**을 사용합니다.

따라서 앞으로 AIKOS에서도 특별한 언급이 없다면 Python은 **CPython**을 의미합니다.

---

### 학습자가 자주 혼동하는 부분

##### 오해 1

> 모든 AI 계산을 Python Interpreter가 직접 수행한다.

대규모 Tensor 연산과 모델 추론의 핵심 계산은 주로 GPU,
최적화된 Native Library 또는 외부 AI 서버가 수행합니다.
Python은 이를 호출하고 전체 흐름을 제어하며, 전처리·후처리와
서비스 로직의 일부는 Python에서 직접 실행될 수 있습니다.

---

##### 오해 2

> Python이 느려서 AI에는 적합하지 않다.

아닙니다.

핵심 Tensor 연산은 GPU와 최적화 라이브러리가 수행하는 경우가 많지만,
Python으로 작성한 반복문·파싱·전처리는 병목이 될 수 있습니다.

---

##### 오해 3

> Python은 한 줄씩 단순히 읽고 실행한다.

정확히는

CPython 기준으로 Bytecode 생성 → 실행 엔진의 처리 과정을 거칩니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 Python 코드가 실제로 어떻게 실행되는지를 이해했습니다.

핵심은 다음과 같습니다.

- Python 코드는 컴퓨터가 직접 실행하는 것이 아니라 **Python Interpreter**가 읽고 실행한다.
- 일반적으로 사용하는 **CPython 기준으로**, Python 코드는 **Bytecode**로 변환되고 CPython의 실행 엔진이 이를 처리한다.
- Python은 컴파일 언어보다 일반적으로 느리지만, 많은 AI 핵심 연산은 최적화된 라이브러리·GPU·외부 API가 수행한다.
- 실제 AI 연산은 **PyTorch, TensorFlow, NumPy, CUDA, GPU** 등 고성능 라이브러리와 하드웨어가 담당한다.
- Python은 AI 서비스에서 계산 엔진이 아니라 **서비스를 연결하고 제어하는 오케스트레이터** 역할을 수행한다.

---

이제 Python이 왜 AI 개발에서 널리 사용되는지뿐 아니라, **어떻게 실행되고 어떤 작업에서 Python 자체의 성능이 병목이 될 수 있는지**까지 이해했습니다. 다음 Unit부터는 이러한 실행 구조를 바탕으로 AI 개발에 필요한 Python 문법과 데이터 구조를 본격적으로 학습하게 됩니다.

---

## Unit 3. 개발환경 구축과 Python 프로젝트의 구조

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 AI 개발자는 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> **Unit 3. Python 개발환경 구축과 프로젝트 구조** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- Python을 설치하면 실제로 무엇이 설치되는가?
- IDE는 무엇이며 왜 필요한가?
- 터미널은 왜 사용하는가?
- AI 프로젝트는 어떤 구조로 관리하는가?
- 왜 프로젝트마다 독립적인 개발환경을 사용하는가?

---

### ① 문제 이해 (Why)

#### 지금까지는 Python만 배웠다.

우리는 지금까지

> Python이라는 언어

를 배웠습니다.

하지만

실제 개발자는

Python만 설치해서 개발하지 않습니다.

실제로는

```text
Python

+

IDE

+

Terminal

+

Git

+

Virtual Environment

+

Package Manager
```

를 함께 사용합니다.

즉,

Python은

개발 환경의 한 구성 요소일 뿐입니다.

---

#### AI 프로젝트는 라이브러리가 매우 많다.

예를 들어

AI 문서 요약 서비스를 만든다고 가정해 봅시다.

필요한 라이브러리만 적어도

```text
FastAPI

OpenAI

Pandas

NumPy

Pydantic

Uvicorn

python-dotenv

PyMuPDF

Pillow
```

등이 필요합니다.

이 모든 것을

직접 관리해야 합니다.

그래서

개발환경이 매우 중요합니다.

---

### 개발환경(Development Environment)이란?

개발환경이란

> **프로그램을 개발하기 위해 필요한 모든 도구들의 집합**

입니다.

즉

```text
컴퓨터

↓

운영체제

↓

Python

↓

IDE

↓

Terminal

↓

Library

↓

Project
```

전체를

개발환경이라고 부릅니다.

---

### 실제 개발자의 환경

실무에서는

보통 다음과 같은 구성을 사용합니다.

```text
Windows / macOS / Linux

        │

Python

        │

Visual Studio Code

        │

Git

        │

Virtual Environment

        │

Project
```

---

### 왜 VS Code를 사용하는가?

Python은

메모장으로도 작성할 수 있습니다.

예를 들어

```python
print("Hello")
```

이 정도는 메모장도 가능합니다.

그런데

실무 프로젝트는

수백 개의 파일이 존재합니다.

예를 들면

```text
app/

api/

models/

services/

utils/

config/

database/
```

메모장으로는

이 프로젝트를 관리할 수 없습니다.

---

그래서 사용하는 것이

> **IDE(Integrated Development Environment)**

입니다.

---

### IDE란?

IDE는

> **개발에 필요한 기능을 하나로 모아 놓은 프로그램**

입니다.

대표적으로

```text
VS Code

PyCharm

IntelliJ

Visual Studio
```

등이 있습니다.

AI 개발에서는

가장 많이 사용하는 IDE가

> **Visual Studio Code(VS Code)**

입니다.

---

### VS Code가 제공하는 기능

단순히 코드를 입력하는 프로그램이 아닙니다.

```text
코드 작성

↓

자동 완성

↓

오류 표시

↓

디버깅

↓

Git 연동

↓

Terminal 내장

↓

Extension 설치
```

즉

AI 개발에 필요한 거의 모든 기능이 포함되어 있습니다.

---

### VS Code를 추천하는 이유

AI·Python 생태계에서 널리 사용되며,
이 과정의 예제와 실습 환경을 통일하기 좋습니다.

예를 들어

OpenAI

LangChain

FastAPI

React

Python

Docker

Git

모두

VS Code를 중심으로

Extension이 제공됩니다.

---

### Terminal은 왜 사용하는가?

많은 입문자는

터미널을 어려워합니다.

하지만

AI 개발 과정에서 매우 자주 사용합니다.

예를 들어

```bash
python main.py
```

```bash
python -m pip install openai
```

```bash
git status
```

```bash
uvicorn main:app
```

모두

터미널에서 실행됩니다.

---

### 터미널은 무엇인가?

터미널은

> **컴퓨터에게 명령을 직접 전달하는 창**

입니다.

비유하면

마우스는

버튼을 누르는 방식이고

터미널은

컴퓨터와 대화하는 방식입니다.

```text
개발자

↓

Terminal

↓

Operating System

↓

Python
```

---

### Python 프로젝트는 어디에 저장할까?

학습자는

바탕화면에

파일을 하나씩 만들곤 합니다.

```text
hello.py

hello2.py

test.py

new.py

final.py

real_final.py
```

이런 방식은

프로젝트가 커질수록 관리가 불가능합니다.

---

실무에서는

프로젝트 단위로 관리합니다.

예를 들어

```text
AI_Project/

    main.py

    app/

    data/

    docs/

    tests/

    requirements.txt
```

이렇게

하나의 폴더가

하나의 프로젝트입니다.

---

### AIKOS에서 사용할 기본 프로젝트 구조

Phase 1에서는

소규모 AI API 프로젝트에서 시작하기 좋은
**실무 지향 기본 구조**를 사용합니다.

```text
ai-project/

│

├── app/

│      ├── main.py

│      ├── config.py

│      ├── services/

│      ├── models/

│      ├── utils/

│

├── data/

│

├── docs/

│

├── tests/

│

├── requirements.txt

│

└── README.md
```

현재는

구조만 이해하면 됩니다.

각 폴더의 역할은

FastAPI를 배우면서 자세히 설명합니다.

---

### 왜 프로젝트마다 독립적인 환경을 사용할까?

예를 들어

Project A는

```text
OpenAI 1.2
```

를 사용합니다.

Project B는

```text
OpenAI 2.0
```

를 사용합니다.

둘을

같은 컴퓨터에 설치하면

어떤 버전이 실행될까요?

충돌이 발생합니다.

---

그래서

프로젝트마다

독립적인 Python 환경을 만듭니다.

이것을

> **Virtual Environment(가상환경)**

라고 합니다.

---

### Virtual Environment란?

비유하면

하나의 집 안에

여러 개의 방을 만드는 것입니다.

```text
컴퓨터

│

├── Project A

│      Python

│      Library A

│

├── Project B

│      Python

│      Library B

│

└── Project C

       Python

       Library C
```

각 프로젝트는

서로 영향을 주지 않습니다.

---

### 왜 AI 프로젝트에서 특히 중요한가?

AI 라이브러리는

업데이트가 매우 빠릅니다.

예를 들어

```text
OpenAI SDK

↓

새 버전 출시

↓

함수 이름 변경

↓

기존 프로젝트 오류
```

가 발생할 수 있습니다.

따라서

실무에서는

프로젝트별 가상환경을 사용하는 것이 거의 필수입니다.

---

### Package Manager란?

Python에는

라이브러리를 설치하는 프로그램이 있습니다.

바로

> **pip**

입니다.

예를 들어

```bash
python -m pip install openai
```

를 실행하면

```text
PyPI(Python Package Index)

↓

다운로드

↓

설치

↓

사용 가능
```

과정이 자동으로 수행됩니다.

---

### PyPI란?

PyPI는

Python 라이브러리 저장소입니다.

비유하면

```text
Android

↓

Play Store
```

```text
iPhone

↓

App Store
```

처럼

Python에는

```text
PyPI
```

가 있습니다.

여기에서

수십만 개의 라이브러리를

설치할 수 있습니다.

---

### AI 개발에서 자주 사용하는 라이브러리

앞으로 Phase 1에서

직접 사용할 라이브러리들입니다.

| 라이브러리    | 역할            |
| ------------- | --------------- |
| openai        | OpenAI API 호출 |
| fastapi       | API 서버 구축   |
| uvicorn       | FastAPI 실행    |
| python-dotenv | 환경 변수 관리  |
| pydantic      | 데이터 검증     |
| pandas        | 데이터 처리     |
| numpy         | 수치 계산       |
| pymupdf       | PDF 처리        |
| pillow        | 이미지 처리     |

현재는

이름만 익혀도 충분합니다.

각 라이브러리는

해당 단원에서 자세히 학습합니다.

---

### 자주 발생하는 오류와 오해

##### ① Python만 설치하면 끝이라고 생각한다.

실제 개발에는

VS Code

Git

터미널

가상환경

라이브러리 관리

등이 모두 필요합니다.

---

##### ② 프로젝트를 바탕화면에 파일만 여러 개 만든다.

실무는

프로젝트 단위로 관리합니다.

---

##### ③ 모든 프로젝트가 같은 라이브러리를 사용한다고 생각한다.

프로젝트마다

버전이 다를 수 있습니다.

그래서

가상환경이 필요합니다.

---

##### ④ pip가 Python과 별개라고 생각한다.

`pip`는 Python 패키지를 설치하고 관리할 때
표준적으로 널리 사용하는 도구입니다.

`python -m pip`처럼 실행하면 현재 선택한 Python 환경의 `pip`를
사용한다는 점이 더 분명해집니다.

Windows에서 `python` 명령 대신 `py`를 사용하는 환경이라면
`py -m pip install openai`처럼 실행할 수 있습니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **Python을 사용하는 환경 전체**를 이해했습니다.

핵심은 다음과 같습니다.

- Python 개발은 언어만 배우는 것이 아니라 **개발환경 전체를 이해하는 것**이다.
- 실무에서는 **VS Code + Terminal + Git + Virtual Environment + pip**를 기본 도구로 사용한다.
- 프로젝트는 파일 단위가 아니라 **프로젝트 폴더 단위**로 관리한다.
- AI 프로젝트는 라이브러리 의존성이 많기 때문에 **가상환경**이 필수이다.
- `pip`는 PyPI에서 필요한 Python 패키지를 설치하고 관리할 때 표준적으로 널리 사용하는 도구이다.

---

#### AIKOS 학습 연결

지금까지의 흐름은 다음과 같습니다.

```text
AI 서비스 아키텍처
        │
        ▼
왜 Python을 사용하는가?
        │
        ▼
Python은 어떻게 실행되는가?
        │
        ▼
Python 개발환경과 프로젝트 구조   ✅
        │
        ▼
다음 Unit
Python 변수와 메모리의 원리
```

다음 Unit부터는 본격적으로 **Python 문법**을 배우기 시작하지만, 단순히 "변수는 값을 저장한다" 수준이 아니라 **메모리와 객체 관점에서 Python 변수가 어떻게 동작하는지**부터 AI 개발에 필요한 사고방식으로 학습합니다.

---

## Unit 4. 변수(Variable)의 진짜 의미와 메모리 구조

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> Unit 3. 개발환경과 프로젝트 구조 ✅
>
> **Unit 4. 변수와 메모리의 원리** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 변수는 실제로 무엇인가?
- 변수는 값을 저장하는 상자인가?
- Python에서는 메모리를 어떻게 사용하는가?
- 객체(Object)란 무엇인가?
- AI 개발에서는 왜 이 개념이 중요한가?

---

### ① 문제 이해 (Why)

프로그래밍을 처음 배우면 대부분 이렇게 배웁니다.

```python
a = 10
```

그리고

> "a라는 변수에 10을 저장한다."

라고 설명합니다.

하지만...

이 설명은 **완전히 틀린 것은 아니지만 정확하지도 않습니다.**

Python은 실제로 이렇게 동작하지 않습니다.

---

왜 이 차이가 중요할까요?

앞으로 우리는

- 리스트(List)
- 딕셔너리(Dictionary)
- Pandas
- NumPy
- PyTorch

를 사용하게 됩니다.

이때

메모리 구조를 이해하지 못하면

매우 이상한 버그를 만나게 됩니다.

---

예를 들어

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

학습자는

```text
[1, 2, 3]
```

이 출력될 것이라고 생각합니다.

하지만 실제 결과는

```text
[1, 2, 3, 4]
```

입니다.

왜 이런 일이 발생할까요?

오늘 그 이유를 이해합니다.

---

### 우리가 알고 있는 변수

학교에서 흔히 배우는 변수는

이런 그림입니다.

```text
┌──────┐
│  10  │
└──────┘
   ▲
   │
   a
```

즉

변수 안에 값이 들어 있다고 생각합니다.

이 설명은

C 언어처럼 일부 언어에서는 어느 정도 맞습니다.

하지만

Python은 조금 다릅니다.

---

### Python의 변수는 무엇일까?

Python에서 변수는

값을 저장하는 상자가 아닙니다.

Python의 변수는

> **객체(Object)를 가리키는 이름(Name)**

입니다.

이것이 Python을 이해하는 가장 중요한 개념입니다.

---

예를 들어

```python
a = 10
```

실제로는

이렇게 생각하는 것이 더 정확합니다.

```text
메모리

┌──────────┐
│ Integer  │
│    10    │
└──────────┘
      ▲
      │
      │
      a
```

즉

10이라는 객체가 메모리에 존재하고

a는

그 객체를 참조(reference)하는 이름입니다.

---

### Object(객체)란?

앞으로 Python에서는

계속

객체(Object)

라는 단어를 만나게 됩니다.

객체는

쉽게 말하면

> **메모리 안에 존재하는 하나의 데이터**

입니다.

예를 들어

```python
10
```

도 객체이고

```python
"Hello"
```

도 객체입니다.

```python
[1,2,3]
```

도 객체입니다.

```python
{"name":"Tom"}
```

도 객체입니다.

Python에서는

거의 모든 것이 객체입니다.

---

### 왜 객체로 만들까?

예를 들어

우리가

```python
10
```

을

100번 사용한다고 생각해봅시다.

상자를 100개 만드는 것보다

하나를 만들어 놓고

필요한 사람이 같이 사용하는 것이 효율적입니다.

비유하면

도서관의 책과 같습니다.

```text
책

▲
│
학생 A

학생 B

학생 C
```

책은 하나입니다.

읽는 사람만 여러 명입니다.

Python도 비슷한 철학을 사용합니다.

---

### 이름(Name)과 객체(Object)

예를 들어

```python
x = 100
```

을 보면

실제로는

```text
Name

x

↓

Object

100
```

입니다.

즉

Name은

객체를 찾기 위한 이름표입니다.

---

### 두 개의 변수가 같은 객체를 가리킬 수 있다.

예를 들어

```python
a = 10
b = a
```

많은 사람들이

이렇게 생각합니다.

```text
a → 10

b → 10(복사)
```

하지만 실제는

```text
      a

       \

        ▼

      Object

        10

        ▲

       /

      b
```

입니다.

두 이름이

같은 객체를 바라보고 있습니다.

---

### AI 개발에서도 계속 등장한다.

예를 들어

OpenAI의 응답도

객체입니다.

```python
response = client.responses.create(...)
```

response 안에

텍스트가 저장되는 것이 아니라

실제로는

응답 객체(Response Object)를 참조합니다.

나중에

우리는

이 객체 안에서

```python
response.output_text
```

처럼

필요한 데이터를 꺼내 사용합니다.

즉

AI 개발도

객체 중심으로 이루어집니다.

---

### 객체에는 정보와 기능이 함께 있다.

객체는

데이터만 있는 것이 아닙니다.

객체는

자신이 할 수 있는 기능도 함께 가지고 있습니다.

예를 들어

문자열

```python
text = "hello"
```

는

다음 기능을 사용할 수 있습니다.

```python
text.upper()
```

```python
text.lower()
```

```python
text.replace()
```

왜 가능할까요?

문자열 객체가

이 기능을 가지고 있기 때문입니다.

---

비유하면

자동차는

```text
자동차

↓

데이터

색상

속도

연식

+

기능

출발()

정지()

가속()
```

를 함께 가지고 있습니다.

객체도

이와 같습니다.

---

### Python은 Everything is Object

Python에는

유명한 특징이 있습니다.

> **Everything is an Object**

거의 모든 것이

객체입니다.

예를 들어

```python
10
```

도 객체

```python
3.14
```

도 객체

```python
True
```

도 객체

```python
[1,2,3]
```

도 객체

```python
"AI"
```

도 객체입니다.

이 특징은

Python을 매우 일관성 있게 만들어 줍니다.

---

### 메모리에는 무엇이 저장될까?

다음 설명은 **CPython을 이해하기 위한 단순화된 교육 모델**입니다.
Python 언어 명세가 특정 메모리 배치를 강제한다는 뜻은 아닙니다.

예를 들어

```python
name = "ChatGPT"
```

메모리는

대략

이런 구조입니다.

```text
Name Space

name

↓

Heap Memory

"ChatGPT"
```

즉

Name Space에는

이름이 있고

Heap Memory에는

객체가 존재합니다.

---

### Name Space란?

Name Space는

이름을 관리하는 공간입니다.

예를 들어

```python
user = "Kim"
age = 20
```

라면

```text
Name Space

user

↓

Object "Kim"

-----------------

age

↓

Object 20
```

입니다.

---

### Heap Memory란?

CPython을 단순화해서 보면 Heap은 Python이 객체를 관리하는
메모리 영역이라고 이해할 수 있습니다.

새 객체가 만들어지면 메모리가 필요하지만, 더 이상 사용하지 않는 객체의
메모리는 회수되거나 이후 객체를 위해 재사용될 수 있습니다.
따라서 객체 수가 늘어난다고 메모리가 항상 같은 비율로 계속 커지는 것은 아닙니다.

---

### Python은 왜 이런 구조를 사용할까?

가장 큰 이유는

객체를 효율적으로 관리하기 위해서입니다.

예를 들어

```python
message = "Hello"
```

를

함수에 전달하거나

다른 변수에 할당할 때

객체를 매번 복사하면

메모리가 낭비됩니다.

대신

객체의 위치만 참조하면

훨씬 빠르고 효율적입니다.

---

### AI 프로젝트에서 매우 중요한 이유

예를 들어

우리는 앞으로

수천 페이지 PDF를 읽고

수백 MB의 데이터를 처리합니다.

만약

매번 데이터를 복사한다면

속도는 크게 느려지고

메모리도 금방 부족해집니다.

Python의 참조 모델은 불필요한 객체 복사를 줄이는 기반이 됩니다.

다만 실제 대용량 처리에서는 NumPy 배열의 View와 Copy,
Pandas 객체의 복사 방식, Tensor의 CPU·GPU Device 이동처럼
사용하는 라이브러리의 메모리 관리 규칙도 함께 확인해야 합니다.

---

### 자주 발생하는 오류와 오해

##### ① 변수 안에 값이 저장된다고만 생각한다.

Python에서는

변수는

객체를 참조하는 이름입니다.

---

##### ② 변수끼리 대입하면 복사된다고 생각한다.

대부분은

같은 객체를 참조하게 됩니다.

(복사가 필요한 경우는 나중에 별도로 학습합니다.)

---

##### ③ 객체와 변수를 같은 개념이라고 생각한다.

둘은 다릅니다.

변수는 이름이고,

객체는 실제 데이터입니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 Python의 가장 중요한 개념인 **객체(Object)와 변수(Name)** 를 배웠습니다.

핵심은 다음과 같습니다.

- Python의 변수는 **값을 저장하는 상자**가 아니라 **객체를 참조하는 이름**이다.
- CPython을 이해하기 위한 단순화된 모델에서 객체는 Python이 관리하는 메모리 영역에 존재한다.
- **Name Space**는 이름과 객체의 연결 관계를 관리한다.
- 하나의 객체를 여러 변수가 함께 참조할 수 있다.
- Python은 **Everything is an Object**라는 철학을 기반으로 설계되었다.
- 이 개념은 앞으로 배우게 될 리스트, 딕셔너리, 함수, 클래스, Pandas, NumPy, OpenAI API 응답 객체까지 모두 연결되는 핵심 원리이다.

---

#### AIKOS 학습 연결

지금까지의 흐름은 다음과 같습니다.

```text
AI 서비스 아키텍처
        │
        ▼
왜 Python을 사용하는가?
        │
        ▼
Python 실행 구조
        │
        ▼
개발환경과 프로젝트 구조
        │
        ▼
변수와 객체(Object) 구조   ✅
        │
        ▼
다음 Unit
Python 자료형(Data Types)
```

## Unit 5. 참조(Reference), 가변(Mutable), 불변(Immutable)

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> Unit 3. 개발환경과 프로젝트 구조 ✅
>
> Unit 4. 변수와 객체(Object) ✅
>
> **Unit 5. 참조(Reference), Mutable, Immutable** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- Reference(참조)는 무엇인가?
- Mutable과 Immutable은 무엇인가?
- 왜 리스트는 변경되고 숫자는 변경되지 않는가?
- Assignment(대입)와 Copy(복사)는 무엇이 다른가?
- AI 프로젝트에서 왜 매우 중요한 개념인가?

---

### ① 문제 이해 (Why)

지난 Unit에서 우리는

Python의 변수는

> **객체를 가리키는 이름(Name)**

이라는 것을 배웠습니다.

그런데 여기서

학습자들이 반드시 한 번은 겪는 문제가 있습니다.

예를 들어

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

많은 사람들이

```text
[1, 2, 3]
```

을 예상합니다.

하지만 실제 결과는

```text
[1, 2, 3, 4]
```

입니다.

왜 그럴까요?

---

반대로

```python
a = 10
b = a

b = 20

print(a)
```

결과는

```text
10
```

입니다.

이번에는

왜 숫자는 안 바뀔까요?

---

이 두 가지를 이해하면

Python의 절반은 이해했다고 해도 과언이 아닙니다.

---

### Reference(참조)란?

참조란

> **객체가 저장된 위치를 가리키는 것**

입니다.

예를 들어

```python
a = [1, 2, 3]
```

메모리는

```text
Name Space

a

↓

Heap

[List Object]

[1,2,3]
```

입니다.

---

이제

```python
b = a
```

를 실행하면

많은 사람들이

새로운 리스트가 만들어진다고 생각합니다.

하지만 실제는

```text
        a

         \

          ▼

     List Object

      [1,2,3]

          ▲

         /

        b
```

입니다.

새로운 리스트는 만들어지지 않습니다.

이름만 하나 더 생깁니다.

---

### append()는 무엇을 변경할까?

다음 코드를 봅시다.

```python
b.append(4)
```

append는

새로운 리스트를 만드는 것이 아닙니다.

기존 리스트를 수정합니다.

즉

```text
기존

[1,2,3]

↓

append

↓

[1,2,3,4]
```

가 됩니다.

객체 자체가 바뀌었기 때문에

같은 객체를 바라보던

a도 변경된 결과를 보게 됩니다.

---

메모리에서는

```text
        a

         \

          ▼

     List Object

   [1,2,3,4]

          ▲

         /

        b
```

입니다.

---

### 숫자는 왜 다를까?

이번에는

```python
a = 10
b = a
```

입니다.

메모리

```text
      a

       \

        ▼

      Integer

        10

        ▲

       /

      b
```

여기까지는 같습니다.

---

이제

```python
b = 20
```

을 실행합니다.

많은 사람들이

10이

20으로 바뀐다고 생각합니다.

하지만

Python의 Integer는

변경할 수 없습니다.

그래서

새로운 객체를 만듭니다.

```text
a

↓

10

----------------

b

↓

20
```

즉

10은 그대로 있고

20이라는 새로운 객체가 생성됩니다.

---

### Immutable(불변 객체)

Immutable은

> **한 번 만들어지면 변경할 수 없는 객체**

입니다.

대표적으로

```python
10

3.14

True

"Hello"

(1,2,3)
```

모두 Immutable입니다.

---

예를 들어

```python
text = "Hello"
```

다음 코드를 실행하면

```python
text.upper()
```

Hello가

HELLO로 바뀌는 것이 아닙니다.

새로운 문자열

```text
HELLO
```

가 만들어집니다.

원래 문자열은 그대로 있습니다.

---

### Mutable(가변 객체)

Mutable은

> **객체 자체를 변경할 수 있는 객체**

입니다.

대표적으로

```python
list

dict

set
```

입니다.

예를 들어

```python
numbers = [1,2,3]
```

```python
numbers.append(4)
```

그러면

같은 리스트가 수정됩니다.

---

### Mutable과 Immutable 비교

| 구분         | Immutable              | Mutable         |
| ------------ | ---------------------- | --------------- |
| 객체 변경    | 불가능                 | 가능            |
| 새 객체 생성 | 필요                   | 불필요          |
| 예시         | int, float, str, tuple | list, dict, set |

---

### AI 프로젝트에서 왜 중요할까?

예를 들어

OpenAI API 응답이 있다고 가정합니다.

```python
response = client.responses.create(...)
```

여러 함수가

같은 response 객체를 사용합니다.

```python
save(response)

display(response)

log(response)
```

만약

어느 함수가

response를 수정하면

다른 함수도 영향을 받습니다.

즉

객체 공유는

매우 강력하지만

주의해서 사용해야 합니다.

---

### 함수에서도 같은 문제가 발생한다.

예를 들어

```python
def add_item(data):
    data.append(100)

numbers = [1,2,3]

add_item(numbers)

print(numbers)
```

결과는

```text
[1,2,3,100]
```

입니다.

왜냐하면

함수도

같은 객체를 참조하기 때문입니다.

---

메모리 구조는

```text
numbers

↓

List Object

↓

함수 parameter(data)

↓

같은 List Object
```

입니다.

새로운 리스트가 아닙니다.

---

### Copy(복사)는 언제 필요할까?

가끔은

같은 객체를 공유하면 안 됩니다.

예를 들어

원본 데이터를

보존해야 하는 경우입니다.

이때는

복사를 사용합니다.

```python
a = [1,2,3]

b = a.copy()

b.append(4)
```

그러면

```text
a

↓

[1,2,3]

--------------

b

↓

[1,2,3,4]
```

입니다.

이번에는

서로 다른 객체입니다.

---

메모리

```text
a

↓

List A

[1,2,3]

---------------

b

↓

List B

[1,2,3,4]
```

---

### Assignment와 Copy의 차이

많은 학습자가

가장 헷갈리는 부분입니다.

```python
b = a
```

은

복사가 아닙니다.

참조를 하나 더 만드는 것입니다.

반면

```python
b = a.copy()
```

는

새로운 객체를 생성합니다.

---

비교하면

```text
Assignment

a

↓

Object

↑

b

----------------------

Copy

a

↓

Object A

---------------

b

↓

Object B
```

입니다.

---

### id() 함수로 직접 확인하기

Python은

객체의 식별값을 확인하는 함수를 제공합니다.

```python
a = [1,2,3]
b = a

print(id(a))
print(id(b))
```

두 값은 같습니다.

같은 객체입니다.

---

반대로

```python
a = [1,2,3]

b = a.copy()

print(id(a))
print(id(b))
```

다른 값이 출력됩니다.

새로운 객체입니다.

---

### AI 개발에서 정말 자주 발생하는 실수

예를 들어

```python
config = default_config
```

라고 작성했는데

나중에

```python
config["model"] = "gpt-5"
```

를 수행하면

default_config도 변경됩니다.

왜냐하면

같은 Dictionary를 공유하고 있기 때문입니다.

실무에서도 매우 흔한 버그입니다.

---

### 실무 Best Practice

공유하면 안 되는 데이터는

반드시 복사합니다.

예를 들어

```python
config = default_config.copy()
```

여기서 주의할 점이 있습니다.

`list.copy()`와 `dict.copy()`는 **얕은 복사(Shallow Copy)** 입니다.
바깥쪽 객체만 새로 만들고, 안쪽에 중첩된 객체는 원본과 공유합니다.

```python
original = [["A"], ["B"]]
copied = original.copy()

copied[0].append("X")

xc # [['A', 'X'], ['B']]
print(copied)    # [['A', 'X'], ['B']]
```

바깥 리스트는 서로 다르지만 `original[0]`과 `copied[0]`은
같은 안쪽 리스트를 참조하기 때문에 두 결과가 함께 바뀝니다.

중첩된 객체까지 완전히 독립적으로 복사해야 한다면
`copy.deepcopy()`를 사용할 수 있습니다.

```python
from copy import deepcopy

original = [["A"], ["B"]]
copied = deepcopy(original)

copied[0].append("X")

print(original)  # [['A'], ['B']]
print(copied)    # [['A', 'X'], ['B']]
```

깊은 복사는 중첩 객체까지 새로 복사하므로 더 많은 시간과 메모리가
들 수 있습니다. 원본과 중첩 데이터까지 분리해야 할 때 선택합니다.

---

### 자주 발생하는 오류와 오해

##### ① = 를 복사라고 생각한다.

아닙니다.

기본적으로

참조를 하나 더 만드는 것입니다.

---

##### ② 리스트도 숫자처럼 동작한다고 생각한다.

리스트는

Mutable입니다.

---

##### ③ 문자열도 append가 가능하다고 생각한다.

문자열은

Immutable입니다.

새로운 문자열이 만들어집니다.

---

##### ④ 함수에 전달하면 자동으로 복사된다고 생각한다.

함수도

같은 객체를 참조합니다.

---

### 이번 Unit 핵심 정리

이번 Unit은 Python 전체에서 가장 중요한 개념 중 하나입니다.

핵심은 다음과 같습니다.

- 변수는 객체를 참조하는 이름이다.
- `=` 는 **복사(Copy)** 가 아니라 **참조(Reference)** 를 추가하는 연산이다.
- `list`, `dict`, `set`은 **Mutable** 이므로 객체 자체가 변경된다.
- `int`, `float`, `str`, `tuple`은 **Immutable** 이므로 변경 시 새로운 객체가 생성된다.
- `.copy()`는 바깥 객체만 복사하는 얕은 복사이며, 중첩 객체까지 분리하려면 필요에 따라 `deepcopy()`를 사용한다.
- AI 프로젝트에서는 API 응답, 설정(config), 데이터셋, 벡터 등 큰 객체를 자주 다루므로 **참조와 복사의 차이**를 이해하는 것이 매우 중요하다.

---

### AIKOS 학습 연결

지금까지의 흐름은 다음과 같습니다.

```text
AI 서비스 아키텍처
        │
        ▼
Python 실행 구조
        │
        ▼
개발환경
        │
        ▼
객체(Object)
        │
        ▼
Reference
        │
        ▼
Mutable / Immutable   ✅
        │
        ▼
다음 Unit
Python 자료형(Data Types)
```

## Unit 6. Python 자료형(Data Types)의 원리

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> Unit 3. 개발환경과 프로젝트 구조 ✅
>
> Unit 4. 변수와 객체(Object) ✅
>
> Unit 5. Reference / Mutable / Immutable ✅
>
> **Unit 6. Python 자료형(Data Types)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 자료형(Data Type)은 무엇인가?
- 왜 자료형이 필요한가?
- Python에는 어떤 자료형이 있는가?
- AI 개발에서는 어떤 자료형을 가장 많이 사용하는가?
- 자료형과 객체(Object)는 어떤 관계인가?

---

### ① 문제 이해 (Why)

우리는 지금까지

```python
a = 10

name = "ChatGPT"

numbers = [1,2,3]
```

같은 코드를 사용했습니다.

그런데 여기서 질문이 생깁니다.

> 컴퓨터는 어떻게 10과 "ChatGPT"를 구분할까요?

또는

> 숫자는 더하기가 가능한데 왜 문자열은 더하기 방식이 다를까요?

예를 들어

```python
10 + 20
```

은

```text
30
```

이 됩니다.

하지만

```python
"10" + "20"
```

은

```text
1020
```

이 됩니다.

왜 이런 차이가 생길까요?

바로

> **자료형(Data Type)**

때문입니다.

---

### 자료형(Data Type)이란?

자료형은

> **데이터가 어떤 종류인지 알려주는 정보**

입니다.

비유하면

택배 상자에 붙은 스티커와 같습니다.

```text
📦

"전자제품"

"냉장보관"

"유리"

```

같은 물건이라도

어떤 종류인지에 따라

다루는 방법이 달라집니다.

데이터도 마찬가지입니다.

---

### Python은 자료형을 객체가 가지고 있다.

많은 언어에서는

변수가 자료형을 가집니다.

예를 들어

```java
int number;
```

처럼

변수가 자료형을 가집니다.

---

하지만 Python은 다릅니다.

Python에서는

> **객체(Object)가 자료형을 가지고 있습니다.**

예를 들어

```python
a = 10
```

메모리에서는

```text
a

↓

Object

Value : 10

Type : int
```

입니다.

즉

변수는

이름만 가지고 있고,

자료형은 객체 안에 있습니다.

---

### 왜 이렇게 설계했을까?

Python은

모든 것을 객체로 다룹니다.

객체 안에는

```text
데이터

+

자료형

+

기능(Method)
```

이 함께 존재합니다.

그래서

```python
text = "hello"
```

는

문자열 객체이므로

```python
text.upper()
```

같은 기능을 사용할 수 있습니다.

반면

```python
number = 100
```

은

```python
number.upper()
```

를 사용할 수 없습니다.

숫자 객체에는

upper() 기능이 없기 때문입니다.

---

### 자료형을 확인하는 방법

Python에서는

`type()` 함수를 사용합니다.

예를 들어

```python
print(type(10))
```

결과

```text
<class 'int'>
```

---

```python
print(type("AI"))
```

결과

```text
<class 'str'>
```

---

```python
print(type([1,2,3]))
```

결과

```text
<class 'list'>
```

즉

Python은

객체가 어떤 타입인지

직접 알려줍니다.

---

### Python의 기본 자료형

Python에서 가장 많이 사용하는 자료형은 크게 네 가지 그룹으로 나눌 수 있습니다.

```text
숫자(Number)

↓

문자(String)

↓

논리(Boolean)

↓

컬렉션(Collection)
```

AI 개발도

거의 이 네 가지를 중심으로 이루어집니다.

---

### ① 숫자(Number)

숫자는

계산을 위한 자료형입니다.

대표적으로

```python
10
```

```python
3.14
```

---

세부적으로는

| 자료형  | 설명   | 예시 |
| ------- | ------ | ---- |
| int     | 정수   | 10   |
| float   | 실수   | 3.14 |
| complex | 복소수 | 3+4j |

AI 개발에서는

거의 대부분

int와 float를 사용합니다.

---

예를 들어

```python
temperature = 23.5
```

```python
tokens = 2048
```

---

### AI에서는 수치 표현이 매우 중요하다.

AI 모델의 학습과 추론은 주로 실수 기반 Tensor 연산을 사용합니다.

다만 성능과 메모리 효율을 위해 FP32뿐 아니라 FP16, BF16 같은
낮은 정밀도나 INT8·INT4 정수 양자화를 함께 사용할 수 있습니다.

예를 들어

Embedding

Vector

Neural Network

등은 주로 여러 수치가 모인 Tensor로 표현됩니다.

```text
0.1823

-0.4432

0.9991
```

이런 값들이

수천 개

수만 개 모여

AI 모델을 구성합니다.

---

### ② 문자열(String)

문자열은

문자를 저장하는 자료형입니다.

```python
name = "OpenAI"
```

```python
message = "Hello AI"
```

---

문자열은

Immutable입니다.

즉

수정이 아니라

새로운 문자열을 만듭니다.

---

AI 서비스에서는

가장 많이 사용하는 자료형입니다.

왜냐하면

LLM의 입력과 출력이

모두 문자열이기 때문입니다.

```text
사용자 질문

↓

String

↓

LLM

↓

String

↓

사용자 응답
```

---

### ③ Boolean

Boolean은

참(True)

거짓(False)

을 나타내는 자료형입니다.

```python
True

False
```

예를 들어

```python
is_login = True
```

```python
is_admin = False
```

---

AI 서비스에서도

Boolean은

자주 사용됩니다.

예를 들어

```python
is_pdf_uploaded
```

```python
is_authenticated
```

등의 상태를 관리할 때 사용합니다.

---

### ④ Collection

Collection은

여러 개의 데이터를 저장하는 자료형입니다.

Python에는

대표적으로

```text
List

Tuple

Dictionary

Set
```

가 있습니다.

이 네 가지는

앞으로 매우 중요합니다.

---

### Collection이 필요한 이유

예를 들어

학생 이름 하나라면

```python
name = "Kim"
```

이면 충분합니다.

하지만

학생이

100명이라면?

```python
student1

student2

student3
```

처럼

변수를 100개 만들 수는 없습니다.

그래서

Collection을 사용합니다.

---

### List

List는

순서가 있는 데이터 모음입니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

---

특징

- 순서 있음
- 수정 가능(Mutable)
- 가장 많이 사용

---

AI에서

대표적으로

```python
documents = []

messages = []

embeddings = []
```

처럼 사용합니다.

---

### Tuple

Tuple은

List와 비슷하지만

수정이 불가능합니다.

```python
point = (10,20)
```

---

특징

- 순서 있음
- Immutable

---

AI에서는

좌표

크기(Size)

설정값

등을 저장할 때 사용합니다.

---

### Dictionary

Dictionary는

Key와 Value를 저장합니다.

```python
user = {
    "name":"Kim",
    "age":20
}
```

---

비유하면

사전(Dictionary)

입니다.

```text
name

↓

Kim

------------

age

↓

20
```

AI 서비스에서는

가장 많이 사용하는 자료형 중 하나입니다.

---

예를 들어

OpenAI 응답도

JSON 형태입니다.

JSON은

Dictionary와 매우 비슷합니다.

```python
{
    "model":"gpt-5",
    "usage":123
}
```

나중에 FastAPI에서도

계속 사용합니다.

---

### Set

Set은

중복을 허용하지 않는 자료형입니다.

```python
tags = {
    "AI",
    "Python",
    "LLM"
}
```

---

같은 값을 넣어도

한 번만 저장됩니다.

예를 들어

```python
{
    "AI",
    "AI",
    "AI"
}
```

결과

```text
{"AI"}
```

---

AI에서는

중복 제거

태그 관리

등에 사용됩니다.

---

### AI 프로젝트에서 가장 많이 사용하는 자료형

실무에서는

거의 다음 순서입니다.

| 자료형 | 사용 빈도 |
| ------ | --------- |
| str    | ★★★★★     |
| dict   | ★★★★★     |
| list   | ★★★★★     |
| bool   | ★★★★☆     |
| int    | ★★★★☆     |
| float  | ★★★★☆     |
| tuple  | ★★★☆☆     |
| set    | ★★☆☆☆     |

---

왜 그럴까요?

AI 서비스는

거의

```text
문자열

↓

Dictionary(JSON)

↓

List

↓

LLM
```

구조로 동작하기 때문입니다.

---

### 자료형은 메서드도 결정한다.

예를 들어

문자열은

```python
text.upper()
```

를 사용할 수 있습니다.

리스트는

```python
numbers.append(10)
```

를 사용할 수 있습니다.

Dictionary는

```python
user.keys()
```

를 사용할 수 있습니다.

즉

자료형마다

사용 가능한 기능이 다릅니다.

---

### 자주 발생하는 오류와 오해

##### ① 숫자와 문자열을 같은 것으로 생각한다.

```python
10
```

과

```python
"10"
```

은

전혀 다른 객체입니다.

---

##### ② List와 Dictionary를 구분하지 못한다.

List는

순서 중심입니다.

Dictionary는

Key 중심입니다.

---

##### ③ 모든 Collection이 수정 가능하다고 생각한다.

Tuple은

Immutable입니다.

---

##### ④ Dictionary와 JSON이 같은 것이라고 생각한다.

엄밀히 말하면 다릅니다.

- Dictionary는 **Python의 자료형**
- JSON은 **데이터 교환 형식(문자열 표현 규격)**

하지만 구조가 매우 비슷하기 때문에 서로 자주 변환합니다.

이 차이는 FastAPI를 배울 때 자세히 다룹니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 Python 자료형의 원리를 이해했습니다.

핵심은 다음과 같습니다.

- 자료형은 **데이터가 어떤 종류인지 나타내는 정보**이다.
- Python에서는 **변수가 아니라 객체가 자료형을 가진다.**
- 기본 자료형은 `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`이다.
- AI 서비스에서는 특히 **`str`**, **`dict`**, **`list`**가 가장 많이 사용된다.
- 자료형에 따라 사용할 수 있는 메서드와 동작 방식이 달라진다.

---

### AIKOS 학습 연결

지금까지의 흐름은 다음과 같습니다.

```text
AI 서비스 아키텍처
        │
        ▼
Python 실행 구조
        │
        ▼
개발환경
        │
        ▼
Object
        │
        ▼
Reference
        │
        ▼
Data Types   ✅
        │
        ▼
다음 Unit
연산자(Operators)와 표현식(Expression)
```

## Unit 7. 연산자(Operator)와 표현식(Expression)

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> Unit 3. 개발환경과 프로젝트 구조 ✅
>
> Unit 4. 변수와 객체(Object) ✅
>
> Unit 5. Reference / Mutable / Immutable ✅
>
> Unit 6. 자료형(Data Types) ✅
>
> **Unit 7. 연산자와 표현식** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 연산자(Operator)는 무엇인가?
- 표현식(Expression)은 무엇인가?
- Python은 연산을 어떻게 수행하는가?
- 객체(Object)와 연산자는 어떤 관계인가?
- AI 개발에서는 어떤 연산자를 가장 많이 사용하는가?

---

### ① 문제 이해 (Why)

우리는 이미

```python
a = 10
b = 20

print(a + b)
```

같은 코드를 많이 봤습니다.

여기서 질문이 하나 생깁니다.

> "+"는 누구의 기능일까요?

많은 사람들이

> Python이 계산한다.

라고 생각합니다.

하지만 실제로는 조금 다릅니다.

Python은

객체에게

> "너희 둘이 더해질 수 있니?"

라고 물어보는 것입니다.

---

이 개념을 이해하면

왜

```python
10 + 20
```

은 가능하지만

```python
10 + "20"
```

은 오류가 발생하는지도 이해하게 됩니다.

---

### 연산자(Operator)란?

연산자는

> **객체에 어떤 동작을 수행하도록 요청하는 기호**

입니다.

예를 들어

```text
+
```

는

더하기를 의미합니다.

```text
-
```

는

빼기입니다.

```text
==
```

는

같은지 비교합니다.

---

즉

연산자는

객체에게

"이 작업을 수행해."

라고 요청하는 역할을 합니다.

---

### 표현식(Expression)이란?

표현식은

> **하나의 값을 만들어 내는 코드**

입니다.

예를 들어

```python
10 + 20
```

결과는

```text
30
```

입니다.

즉

이 코드 자체가

하나의 값을 생성합니다.

---

또 다른 예입니다.

```python
5 * 4
```

↓

```text
20
```

---

```python
True and False
```

↓

```text
False
```

---

모두

표현식입니다.

---

### 문장(Statement)과 표현식(Expression)

많이 헷갈리는 개념입니다.

예를 들어

```python
a = 10
```

은

대입문(Statement)입니다.

반면

```python
10 + 20
```

은

표현식(Expression)입니다.

왜냐하면

결과가 하나의 값이기 때문입니다.

---

비유하면

```text
Expression

↓

결과를 만든다.

----------------

Statement

↓

명령을 수행한다.
```

입니다.

---

### Python은 어떻게 더하기를 할까?

예를 들어

```python
10 + 20
```

을 실행하면

실제로는

이런 과정이 일어납니다.

```text
Integer Object

10

+

Integer Object

20

↓

새로운 Integer Object

30
```

여기서 중요한 점은

30이라는

새로운 객체가 만들어진다는 것입니다.

기존 10과 20은

변하지 않습니다.

---

### 문자열의 더하기

예를 들어

```text
"Hello"

+

"AI"
```

결과는

```text
HelloAI
```

입니다.

여기서

더하기는

숫자 계산이 아닙니다.

문자열 연결입니다.

---

즉

같은

```text
+
```

라도

객체의 자료형에 따라

동작이 달라집니다.

---

### 이것이 객체 지향의 특징이다.

Python은

객체에게

작업을 요청합니다.

예를 들어

```python
10 + 20
```

은

정수 객체의

더하기 기능을 호출합니다.

반면

```python
"AI" + "KOS"
```

는

문자열 객체의

연결 기능을 호출합니다.

같은 기호라도

객체가 다르면

동작도 달라집니다.

---

### 주요 연산자 종류

Python의 연산자는 크게 다음과 같이 구분됩니다.

```text
산술 연산자

↓

비교 연산자

↓

논리 연산자

↓

대입 연산자

↓

멤버십 연산자

↓

식별 연산자
```

AI 서비스에서는

이 정도만 이해해도 충분합니다.

---

### ① 산술 연산자

가장 많이 사용하는 연산자입니다.

| 연산자 | 의미   |
| ------ | ------ |
| +      | 더하기 |
| -      | 빼기   |
| \*     | 곱하기 |
| /      | 나누기 |
| //     | 몫     |
| %      | 나머지 |
| \*\*   | 제곱   |

예를 들어

```python
tokens = 2000

price = tokens * 0.000005
```

AI 서비스에서는

토큰 비용 계산 등에 사용됩니다.

---

### ② 비교 연산자

비교 결과는

Boolean입니다.

| 연산자 | 의미        |
| ------ | ----------- |
| ==     | 같다        |
| !=     | 다르다      |
| >      | 크다        |
| <      | 작다        |
| >=     | 크거나 같다 |
| <=     | 작거나 같다 |

예를 들어

```python
token_count > 8000
```

결과는

```python
True
```

또는

```python
False
```

입니다.

---

### AI 서비스 예제

예를 들어

```text
if token_count > 8000:
```

라는 코드는

토큰이 너무 많으면

문서를 분할하도록 만들 수 있습니다.

나중에

RAG에서

계속 등장합니다.

---

### ③ 논리 연산자

논리 연산자는

Boolean끼리 연산합니다.

```text
and

or

not
```

예를 들어

```python
is_login and is_admin
```

둘 다 True여야

True가 됩니다.

---

AI 서비스에서는

권한 확인

인증

조건 검사

등에 자주 사용됩니다.

---

### ④ 대입 연산자

우리가 가장 많이 사용하는 연산자입니다.

```text
=
```

뿐 아니라

```text
+=

-=

*=

/=
```

도 있습니다.

예를 들어

```python
count += 1
```

은

```python
count = count + 1
```

과 같은 의미입니다.

---

### ⑤ Membership Operator

AI 개발에서

의외로 많이 사용하는 연산자입니다.

```text
in

not in
```

예를 들어

```text
if ".pdf" in filename:
```

또는

```text
if "error" in response:
```

처럼

문자열이나 리스트 안에

특정 값이 있는지 확인합니다.

---

### ⑥ Identity Operator

지난 Unit과 연결되는 연산자입니다.

```text
is

is not
```

많은 사람들이

```text
==
```

와

같다고 생각하지만

전혀 다릅니다.

---

예를 들어

```python
a == b
```

는

값이 같은지 비교합니다.

반면

```python
a is b
```

는

같은 객체인지 비교합니다.

---

비유하면

```text
==

↓

내용 비교

----------------

is

↓

같은 객체 비교
```

입니다.

---

예를 들어

```python
a = [1,2]

b = [1,2]
```

```python
a == b
```

↓

```python
True
```

하지만

```python
a is b
```

↓

```python
False
```

입니다.

왜냐하면

서로 다른 객체이기 때문입니다.

---

반대로

```python
b = a
```

라면

```python
a is b
```

↓

```python
True
```

입니다.

---

### AI 프로젝트에서 중요한 이유

예를 들어

```python
response is None
```

이 코드는

매우 자주 사용됩니다.

왜

```python
response == None
```

보다

```python
response is None
```

를 사용할까요?

`None`은 특별한 **싱글턴(Singleton) 객체**이기 때문입니다.

따라서 **같은 객체인지 확인하는 `is`가 올바른 표현**입니다.

이것은 Python 공식 스타일 가이드(PEP 8)에서도 권장하는 방식입니다.

---

### 연산 우선순위

Python도

수학처럼

우선순위가 있습니다.

예를 들어

```python
10 + 2 * 3
```

결과는

```text
16
```

입니다.

왜냐하면

곱하기가 먼저 수행됩니다.

---

괄호를 사용하면

```python
(10 + 2) * 3
```

↓

```text
36
```

이 됩니다.

실무에서는

우선순위를 외우기보다

**괄호를 적극 사용하는 습관**이 가독성과 유지보수 측면에서 더 좋습니다.

---

### AI 프로젝트에서 가장 많이 사용하는 연산자

실무 기준으로 보면

| 연산자   | 사용 빈도 |
| -------- | --------- |
| =        | ★★★★★     |
| ==       | ★★★★★     |
| >        | ★★★★☆     |
| in       | ★★★★☆     |
| and / or | ★★★★☆     |
| +=       | ★★★☆☆     |
| is       | ★★★☆☆     |

---

예를 들어

```text
if response is None:
```

```text
if ".pdf" in filename:
```

```text
if token_count > MAX_TOKEN:
```

이런 조건 검사는 AI 서비스 코드에서 자주 작성합니다.

---

### 자주 발생하는 오류와 오해

##### ① `=` 와 `==`를 혼동한다.

```text
=
```

은 대입입니다.

```text
==
```

는 비교입니다.

---

##### ② `==`와 `is`를 같은 것으로 생각한다.

`==`

↓

값 비교

`is`

↓

객체 비교

입니다.

---

##### ③ 문자열도 숫자처럼 더해진다고 생각한다.

```python
"10" + "20"
```

은

숫자 계산이 아니라

문자열 연결입니다.

---

##### ④ 연산 결과가 기존 객체를 변경한다고 생각한다.

Immutable 객체의 연산은

대부분 새로운 객체를 생성합니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 Python 연산자의 원리를 이해했습니다.

핵심은 다음과 같습니다.

- 연산자는 **객체에 동작을 요청하는 기호**이다.
- 표현식(Expression)은 **하나의 값을 생성하는 코드**이다.
- 같은 연산자라도 자료형에 따라 동작 방식이 달라질 수 있다.
- `==`는 **값 비교**, `is`는 **객체 비교**이다.
- AI 서비스에서는 `=`, `==`, `in`, `is`, `and`, `or`를 가장 자주 사용한다.

---

### AIKOS 학습 연결

지금까지의 흐름입니다.

```text
AI 서비스 아키텍처
        │
        ▼
Python 실행 구조
        │
        ▼
개발환경
        │
        ▼
Object
        │
        ▼
Reference
        │
        ▼
Data Types
        │
        ▼
Operators & Expressions   ✅
        │
        ▼
다음 Unit
조건문(Conditional Statements)
```

---

## Unit 8. 조건문(Conditional Statements)과 프로그램의 의사결정

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1. 왜 Python을 사용하는가? ✅
>
> Unit 2. Python은 어떻게 실행되는가? ✅
>
> Unit 3. 개발환경과 프로젝트 구조 ✅
>
> Unit 4. 변수와 객체(Object) ✅
>
> Unit 5. Reference / Mutable / Immutable ✅
>
> Unit 6. 자료형(Data Types) ✅
>
> Unit 7. 연산자와 표현식 ✅
>
> **Unit 8. 조건문(Conditional Statements)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 조건문은 왜 필요한가?
- 프로그램은 어떻게 "판단"하는가?
- if, elif, else는 어떤 원리로 동작하는가?
- AI 서비스에서는 언제 조건문을 사용하는가?
- 좋은 조건문을 작성하는 방법은 무엇인가?

---

### ① 문제 이해 (Why)

지금까지 우리가 작성한 프로그램은 모두 같은 방식으로 실행되었습니다.

예를 들어

```python
print("프로그램 시작")

print("OpenAI 호출")

print("프로그램 종료")
```

실행 결과

```
프로그램 시작

OpenAI 호출

프로그램 종료
```

항상 같은 결과입니다.

---

그런데 실제 AI 서비스는 그렇지 않습니다.

예를 들어

```
사용자가 PDF를 업로드했는가?

YES

↓

PDF 분석

--------------------

NO

↓

오류 메시지 출력
```

상황에 따라

다른 동작을 해야 합니다.

이것이

조건문이 필요한 이유입니다.

---

### 프로그램은 어떻게 판단할까?

사람은

```
비가 오면

우산을 가져간다.

비가 안 오면

그냥 나간다.
```

처럼

상황에 따라 행동합니다.

프로그램도 똑같습니다.

```
조건 검사

↓

참(True)

↓

실행

-----------------

거짓(False)

↓

다른 실행
```

즉

조건문은

프로그램에게

> "상황에 따라 다른 행동을 하게 만드는 기능"

입니다.

---

### 조건문의 핵심

조건문은

복잡한 문법이 아닙니다.

핵심은 단 하나입니다.

> **Boolean(True / False)을 이용해 프로그램의 흐름을 결정한다.**

지난 Unit에서 배운

```
비교 연산자

↓

Boolean

↓

조건문
```

이렇게 연결됩니다.

즉

지금까지 배운 내용이

조건문에서 처음 활용됩니다.

---

### 가장 기본적인 if

예를 들어

```python
score = 90

if score >= 80:
    print("합격")
```

프로그램은

```
score >= 80

↓

True ?

↓

YES

↓

print 실행
```

순서로 동작합니다.

---

만약

```python
score = 50
```

이라면

```
50 >= 80

↓

False

↓

print 실행 안 함
```

입니다.

---

### if는 어떻게 동작할까?

Python은

먼저 조건식을 계산합니다.

예를 들어

```text
if token_count > 8000:
```

실제로는

```
Expression

↓

token_count > 8000

↓

Boolean

↓

True ?

↓

실행 여부 결정
```

입니다.

즉

조건문은

Boolean을 평가하는 프로그램입니다.

---

### 들여쓰기(Indentation)

Python에는

다른 언어와 매우 다른 특징이 있습니다.

예를 들어

```python
if True:
    print("Hello")

print("End")
```

여기서

```
print("Hello")
```

는

if에 속합니다.

하지만

```
print("End")
```

는

if 밖에 있습니다.

왜일까요?

들여쓰기 때문입니다.

---

### Python은 들여쓰기로 블록을 구분한다.

많은 언어는

중괄호를 사용합니다.

예를 들어

```
{

}
```

하지만

Python은

들여쓰기 자체가 문법입니다.

```
if

↓

들여쓰기

↓

실행 블록
```

입니다.

---

비유하면

책의 목차와 같습니다.

```
1.

    1-1

    1-2

2.
```

들여쓰기만 봐도

어디에 속하는지 알 수 있습니다.

Python도

같은 철학입니다.

---

### else

조건이 거짓이면

다른 작업을 수행할 수 있습니다.

```python
age = 15

if age >= 20:
    print("성인")
else:
    print("미성년자")
```

동작

```
조건

↓

True ?

↓

YES → 성인

NO → 미성년자
```

입니다.

---

### elif

조건이 여러 개라면?

예를 들어

점수에 따라

등급을 나누고 싶습니다.

```python
score = 85

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("F")
```

동작

```
90 이상?

↓

NO

↓

80 이상?

↓

YES

↓

B 출력
```

입니다.

---

### 조건문은 위에서 아래로 검사한다.

매우 중요한 원리입니다.

예를 들어

```python
score = 95

if score >= 70:
    print("C")

elif score >= 90:
    print("A")
```

결과는

```
C
```

입니다.

왜냐하면

첫 번째 조건이 이미 참이기 때문입니다.

---

따라서

더 구체적인 조건을

위에 작성해야 합니다.

올바른 예

```python
if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("F")
```

---

### AI 서비스에서 가장 많이 사용하는 조건문

#### 예제 1

파일 존재 확인

```python
if uploaded_file is None:
    print("파일이 없습니다.")
```

---

#### 예제 2

PDF 확인

```python
if ".pdf" not in filename:
    print("PDF만 업로드 가능합니다.")
```

---

#### 예제 3

로그인 확인

```python
if not is_login:
    print("로그인이 필요합니다.")
```

---

#### 예제 4

OpenAI 응답 확인

```python
if response is None:
    print("API 호출 실패")
```

---

#### 예제 5

토큰 제한 확인

```python
if token_count > MAX_TOKEN:
    split_document()
```

우리가 앞으로 만들 AI 서비스에는

이런 조건문이

수백 개 등장합니다.

---

### 조건문은 프로그램의 갈림길이다.

AI 서비스 전체를 보면

```
사용자 요청

↓

조건 검사

↓

파일 존재?

↓

YES

↓

PDF인가?

↓

YES

↓

OCR 필요?

↓

YES

↓

OCR 수행

↓

LLM 호출
```

거의 모든 단계가

조건문입니다.

---

### 조건은 너무 길지 않게 작성한다.

예를 들어

```python
if (
    is_login
    and is_admin
    and file_uploaded
    and token_count < MAX_TOKEN
):
    process_document()
```

이런 방식이

가독성이 좋습니다.

반대로

```text
if is_login and is_admin and file_uploaded and token_count < MAX_TOKEN:
```

처럼

너무 길게 쓰면

읽기 어렵습니다.

---

### 중첩 조건문

조건 안에

또 다른 조건도 가능합니다.

```python
if is_login:

    if is_admin:
        print("관리자")
```

하지만

중첩이 많아질수록

읽기 어려워집니다.

실무에서는

가능하면

깊이를 줄이는 방향으로 작성합니다.

---

### AI 프로젝트에서 자주 사용하는 패턴

##### Early Return 방식

나중에 함수에서 자세히 배우지만

실무에서는

```
잘못된 경우

↓

바로 종료
```

를 많이 사용합니다.

예를 들어

```python
if uploaded_file is None:
    return
```

이후

정상 로직만

계속 진행합니다.

이 방식은

코드를 훨씬 읽기 쉽게 만듭니다.

---

### 자주 발생하는 오류와 오해

##### ① `=` 와 `==`를 혼동한다.

```text
if score = 90:
```

❌ 오류

반드시

```text
if score == 90:
```

입니다.

---

##### ② 들여쓰기를 맞추지 않는다.

Python에서는

들여쓰기가

문법입니다.

---

##### ③ 조건 순서를 잘못 작성한다.

```text
if score >= 70
```

를 먼저 쓰면

90점도

70점 조건에서 끝납니다.

---

##### ④ Boolean을 직접 비교한다.

예를 들어

```text
if is_login == True:
```

보다는

```text
if is_login:
```

이 더 Python다운 코드입니다.

---

##### ⑤ None 비교를 `==`로 한다.

```text
if response == None:
```

보다

```text
if response is None:
```

를 사용합니다.

---

### 실무 Best Practice

좋은 조건문은

질문처럼 읽혀야 합니다.

예를 들어

```text
if uploaded_file is None:
```

↓

"업로드된 파일이 없는가?"

---

```text
if token_count > MAX_TOKEN:
```

↓

"토큰이 최대값을 초과했는가?"

이렇게 읽히면

좋은 조건문입니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 프로그램이 **상황에 따라 판단하는 방법**을 배웠습니다.

핵심은 다음과 같습니다.

- 조건문은 **Boolean(True/False)** 결과를 바탕으로 프로그램의 흐름을 제어한다.
- `if`, `elif`, `else`를 사용하여 다양한 조건을 표현할 수 있다.
- Python은 **들여쓰기**로 코드 블록을 구분한다.
- 조건은 **위에서 아래 순서대로 평가**되며, 처음 참이 되는 조건만 실행된다.
- AI 서비스에서는 파일 검사, 로그인 확인, API 응답 확인, 토큰 제한 등 거의 모든 로직에 조건문이 사용된다.

---

### AIKOS 학습 연결

지금까지의 흐름입니다.

```text
AI 서비스 아키텍처
        │
        ▼
Python 실행 구조
        │
        ▼
Object
        │
        ▼
Data Types
        │
        ▼
Operators
        │
        ▼
Conditional Statements   ✅
        │
        ▼
다음 Unit
반복문(Loop)
```

---

## Unit 9. 반복문(Loop)과 데이터 순회의 원리

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 8 ✅
>
> **Unit 9. 반복문(Loop)과 데이터 순회(Iteration)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 반복문은 왜 필요한가?
- for와 while은 어떤 차이가 있는가?
- Python에서 반복은 어떻게 동작하는가?
- AI 서비스에서는 반복문을 어디에 사용하는가?
- break, continue는 언제 사용하는가?

---

### ① 문제 이해 (Why)

지금까지 우리는

프로그램이

> "판단"

하는 방법을 배웠습니다.

이번에는

프로그램이

> "반복"

하는 방법을 배웁니다.

---

예를 들어

학생 이름 하나를 출력한다면

```python
print("Kim")
```

이면 충분합니다.

---

하지만

학생이 100명이라면?

```python
print("Kim")

print("Lee")

print("Park")

...

print("Hong")
```

100줄을 작성해야 합니다.

이것은

좋은 프로그램이 아닙니다.

---

AI 서비스도 마찬가지입니다.

예를 들어

```text
PDF

↓

500 페이지

↓

모든 페이지 분석
```

한 페이지마다

코드를 작성할 수는 없습니다.

---

반복문은

바로 이런 문제를 해결하기 위해 존재합니다.

---

### 반복문이란?

반복문은

> **같은 작업을 여러 번 수행하는 구조**

입니다.

비유하면

공장의 생산 라인과 같습니다.

```text
제품

↓

작업

↓

다음 제품

↓

작업

↓

다음 제품

↓

작업
```

작업은 같습니다.

대상만 바뀝니다.

---

### AI 서비스는 반복의 연속이다.

실제 AI 서비스는

거의 대부분

반복으로 이루어집니다.

예를 들어

```text
문서 목록

↓

첫 번째 문서

↓

Embedding 생성

↓

두 번째 문서

↓

Embedding 생성

↓

...

↓

완료
```

반복이 없다면

AI 서비스는 거의 만들 수 없습니다.

---

### Python에는 두 가지 반복문이 있다.

```text
for

↓

데이터를 순회

------------------

while

↓

조건이 참인 동안 반복
```

둘 다

반복하지만

사용 목적이 다릅니다.

---

### for 문

Python에서

가장 많이 사용하는 반복문입니다.

예를 들어

```python
fruits = [
    "Apple",
    "Banana",
    "Orange"
]

for fruit in fruits:
    print(fruit)
```

결과

```text
Apple

Banana

Orange
```

---

### 어떻게 동작할까?

많은 사람들이

for는

숫자를 반복하는 문법이라고 생각합니다.

하지만

Python의 for는

숫자가 아니라

> **데이터를 하나씩 꺼내는 문법**

입니다.

---

실제로는

```text
List

↓

첫 번째

↓

두 번째

↓

세 번째

↓

끝
```

입니다.

---

비유하면

택배 상자를 하나씩 꺼내는 것입니다.

```text
상자

↓

1

↓

2

↓

3

↓

끝
```

---

### for의 핵심

예를 들어

```python
documents = [
    "doc1",
    "doc2",
    "doc3"
]
```

```python
for document in documents:
    print(document)
```

의 의미는

```text
documents에서

하나 꺼낸다.

↓

document

↓

사용

↓

다음 하나 꺼낸다.
```

입니다.

---

### AI 서비스 예제

예를 들어

사용자가

PDF를 여러 개 업로드했다고 합시다.

```python
files = [
    "A.pdf",
    "B.pdf",
    "C.pdf"
]
```

그러면

```python
for file in files:
    print(file)
```

결과

```text
A.pdf

B.pdf

C.pdf
```

입니다.

실제 프로젝트에서는

```python
for file in files:
    extract_text(file)
```

처럼

각 PDF를 분석하게 됩니다.

---

### 문자열도 반복할 수 있다.

문자열도

데이터의 모음입니다.

```python
for ch in "AI":
    print(ch)
```

결과

```text
A

I
```

입니다.

---

### Dictionary도 반복할 수 있다.

예를 들어

```python
user = {
    "name":"Kim",
    "age":20
}
```

```python
for key in user:
    print(key)
```

결과

```text
name

age
```

입니다.

---

실무에서는

```text
for key, value in user.items():
```

를 더 많이 사용합니다.

이 부분은

함수와 Dictionary를 충분히 학습한 뒤

다시 자세히 다룹니다.

---

### range()

숫자를 반복하고 싶을 때

사용합니다.

```python
for i in range(5):
    print(i)
```

결과

```text
0

1

2

3

4
```

---

왜

5가 아니라

4까지일까요?

Python의 range는

> **시작은 포함하고 끝은 포함하지 않는다.**

라는 규칙을 사용합니다.

즉

```text
range(5)

↓

0

1

2

3

4
```

입니다.

---

### range()가 이렇게 설계된 이유

이 규칙은 처음에는 낯설지만, 프로그래밍에서는 매우 편리합니다.

예를 들어 리스트가 있다면

```python
numbers = [10, 20, 30, 40, 50]
```

이 리스트의 길이는 5입니다.

인덱스는

```text
0   1   2   3   4
```

입니다.

즉

```python
range(len(numbers))
```

를 사용하면

인덱스와 정확히 일치합니다.

이 때문에 대부분의 프로그래밍 언어는

**시작 포함(Start Inclusive), 끝 제외(End Exclusive)** 규칙을 사용합니다.

---

### enumerate()

AI 프로젝트에서는

반복하면서

번호도 필요할 때가 많습니다.

예를 들어

```python
documents = [
    "A.pdf",
    "B.pdf",
    "C.pdf"
]
```

```python
for index, document in enumerate(documents):
    print(index, document)
```

결과

```text
0 A.pdf

1 B.pdf

2 C.pdf
```

입니다.

---

실무에서는

페이지 번호,

문서 번호,

검색 결과 번호 등을 처리할 때

매우 많이 사용합니다.

---

### while 문

while은

조건이 참인 동안

반복합니다.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

결과

```text
0

1

2
```

---

동작 과정

```text
count < 3 ?

↓

YES

↓

실행

↓

count 증가

↓

다시 검사
```

입니다.

---

### for와 while의 차이

이 차이는 매우 중요합니다.

| for                            | while                 |
| ------------------------------ | --------------------- |
| 데이터를 순회                  | 조건이 참인 동안 반복 |
| 끝이 명확함                    | 끝을 직접 관리해야 함 |
| AI 프로젝트에서 가장 많이 사용 | 특수한 경우 사용      |

---

AI 서비스에서는

90% 이상

for를 사용합니다.

while은

특별한 상황에서만 사용합니다.

---

### break

반복을

즉시 종료합니다.

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

결과

```text
0

1

2

3

4
```

5에서

반복이 종료됩니다.

---

### continue

현재 반복만

건너뜁니다.

```python
for number in range(5):

    if number == 2:
        continue

    print(number)
```

결과

```text
0

1

3

4
```

2만

건너뜁니다.

---

### AI 서비스에서 break

예를 들어

검색 결과가

100개 있어도

상위 5개만 사용한다면

```text
검색 결과

↓

5개 수집

↓

break
```

처럼

사용할 수 있습니다.

---

### AI 서비스에서 continue

예를 들어

업로드한 파일 중

이미지만 처리한다고 합시다.

```python
files = [
    "cat.jpg",
    "report.pdf",
    "dog.png"
]
```

```python
for file in files:

    if ".pdf" in file:
        continue

    print(file)
```

PDF는 건너뛰고

이미지만 처리할 수 있습니다.

---

### 반복문의 내부 원리

Python의 for는

사실

Iterator(반복자)

라는 개념 위에서 동작합니다.

```text
Collection

↓

Iterator

↓

하나 반환

↓

다음 반환

↓

다음 반환

↓

Stop
```

현재는

"하나씩 꺼낸다."

정도로 이해하면 충분합니다.

Iterator는

나중에 Generator와 함께 자세히 학습합니다.

---

### AI 프로젝트에서 가장 많이 사용하는 반복

실무에서는

거의 다음 형태입니다.

```text
for document in documents:
```

```text
for message in messages:
```

```text
for page in pages:
```

```text
for result in search_results:
```

```text
for chunk in chunks:
```

RAG,

OCR,

Embedding,

FastAPI

모두

이 형태를 계속 사용합니다.

---

### 자주 발생하는 오류와 오해

##### ① while에서 종료 조건을 잊는다.

```text
while True:
```

만 작성하면

무한 반복이 됩니다.

---

##### ② 리스트를 직접 수정한다.

반복하면서

같은 리스트를 변경하면

예상하지 못한 결과가 나올 수 있습니다.

이 문제는

조금 뒤에 따로 다룹니다.

---

##### ③ 인덱스를 직접 관리한다.

```text
for item in items:
```

가 더 Python다운 코드입니다.

필요할 때만

`enumerate()`를 사용합니다.

---

##### ④ range()가 마지막 숫자를 포함한다고 생각한다.

```python
range(5)
```

는

0~4입니다.

---

### 실무 Best Practice

Python에서는

가능하면

```text
for item in items:
```

처럼

데이터 자체를 순회하는 방식을 권장합니다.

```text
for i in range(len(items)):
```

도 가능하지만

정말 인덱스가 필요한 경우가 아니라면

첫 번째 방식이

더 읽기 쉽고

오류도 적습니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 프로그램이 **같은 작업을 여러 번 수행하는 원리**를 배웠습니다.

핵심은 다음과 같습니다.

- 반복문은 **같은 작업을 여러 번 수행하기 위한 구조**이다.
- `for`는 **데이터를 하나씩 순회**하는 반복문이다.
- `while`은 **조건이 참인 동안 반복**하는 반복문이다.
- `range()`는 숫자 범위를 생성하며 **끝 값은 포함하지 않는다.**
- `break`는 반복을 종료하고, `continue`는 현재 반복만 건너뛴다.
- AI 서비스에서는 문서, 페이지, 메시지, 검색 결과 등을 처리하기 위해 반복문이 매우 많이 사용된다.

---

### AIKOS 학습 연결

지금까지의 흐름입니다.

```text
AI 서비스 아키텍처
        │
        ▼
Python 실행 구조
        │
        ▼
Object & Memory
        │
        ▼
Data Types
        │
        ▼
Operators
        │
        ▼
Conditional Statements
        │
        ▼
Loop (Iteration)   ✅
        │
        ▼
다음 Unit
Function(함수)
```

---

## Unit 10. 함수(Function)와 재사용 가능한 프로그램의 설계

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 9 ✅
>
> **Unit 10. 함수(Function)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 함수(Function)는 왜 필요한가?
- 함수는 무엇인가?
- 함수 호출(Call)과 함수 정의(Definition)의 차이는 무엇인가?
- Parameter와 Argument는 무엇인가?
- Return은 왜 필요한가?
- AI 서비스에서는 함수를 어떻게 사용하는가?

---

### ① 문제 이해 (Why)

지금까지 우리는

조건문과 반복문을 배웠습니다.

이제 웬만한 프로그램은 만들 수 있습니다.

예를 들어

```python
documents = [
    "A.pdf",
    "B.pdf",
    "C.pdf"
]

for document in documents:
    print(f"문서를 분석합니다 : {document}")

print("분석 완료")
```

작은 프로그램이라면 충분합니다.

---

그런데 AI 서비스는 어떨까요?

예를 들어

문서를 하나 처리하는 과정만 생각해봅시다.

```text
PDF 업로드

↓

텍스트 추출

↓

전처리

↓

Chunk 분할

↓

Embedding 생성

↓

Vector DB 저장

↓

LLM 호출

↓

결과 저장
```

이 작업을

문서가 하나 들어올 때마다 수행합니다.

---

사용자가

100개의 PDF를 업로드했다면?

같은 코드를

100번 작성해야 할까요?

물론 아닙니다.

---

여기서 등장하는 것이

> **Function(함수)**

입니다.

---

### 함수란 무엇인가?

함수는

한 문장으로 정의하면

> **특정 작업을 수행하는 코드의 묶음**

입니다.

---

비유하면

커피 머신과 같습니다.

우리는

버튼만 누릅니다.

```text
버튼

↓

커피 머신

↓

커피 완성
```

커피가

어떻게 만들어지는지는

몰라도 됩니다.

---

함수도 같습니다.

```text
함수 호출

↓

함수 내부 작업

↓

결과 반환
```

사용자는

함수를 사용하기만 하면 됩니다.

---

### 왜 함수가 필요할까?

같은 코드를

여러 번 작성한다고 생각해 봅시다.

```python
print("=" * 30)
print("OpenAI 호출")
print("=" * 30)
```

이 코드를

프로그램 곳곳에서

20번 사용한다면

어떻게 될까요?

---

나중에

출력 형식을 수정해야 한다면

20곳을

모두 수정해야 합니다.

---

하지만

함수로 만들면

```python
def print_title():
    print("=" * 30)
    print("OpenAI 호출")
    print("=" * 30)
```

사용은

```python
print_title()
```

한 줄이면 됩니다.

---

수정도

함수 하나만 수정하면

모든 곳에 적용됩니다.

---

### 함수의 핵심 목적

함수는

단순히 코드를 줄이는 기능이 아닙니다.

함수의 진짜 목적은

```text
재사용(Reuse)

+

유지보수(Maintainability)

+

가독성(Readability)

+

역할 분리(Responsibility)
```

입니다.

---

### AI 서비스는 함수의 집합이다.

AI 서비스는 일반적으로 다음과 같은 흐름으로 동작합니다.

```text
사용자

↓

PDF 업로드

↓

OCR

↓

Embedding

↓

RAG

↓

LLM

↓

응답
```

실제로는

거의 모두

함수입니다.

예를 들어

```python
upload_file()

extract_text()

create_embedding()

search_vector()

call_llm()

save_result()
```

AI 서비스는

이 함수들을 연결한 프로그램입니다.

---

### 함수 정의(Definition)

함수를 만들려면

`def`

키워드를 사용합니다.

예를 들어

```python
def hello():
    print("Hello AI")
```

이 코드는

함수를 **실행하는 것이 아닙니다.**

함수를

만드는 것입니다.

---

많은 학습자가

여기서 헷갈립니다.

```python
def hello():
    print("Hello AI")
```

이 코드는

아무것도 출력하지 않습니다.

왜냐하면

아직 호출하지 않았기 때문입니다.

---

### 함수 호출(Call)

함수를 실행하려면

이름 뒤에

괄호를 붙입니다.

```python
hello()
```

그러면

```text
Hello AI
```

가 출력됩니다.

---

동작 구조

```text
Function Definition

↓

메모리에 등록

↓

Function Call

↓

실행
```

입니다.

---

### 함수는 프로그램 안의 작은 프로그램이다.

비유하면

회사 조직과 같습니다.

```text
대표

↓

인사팀

↓

회계팀

↓

개발팀
```

대표는

모든 일을 직접 하지 않습니다.

각 부서에게

일을 맡깁니다.

---

프로그램도 같습니다.

```text
main()

↓

upload()

↓

extract()

↓

summarize()

↓

save()
```

각 함수가

자신의 역할만 수행합니다.

---

### Parameter(매개변수)

함수는

데이터를 받을 수도 있습니다.

예를 들어

```python
def hello(name):
    print(f"안녕하세요 {name}")
```

여기서

```python
name
```

을

Parameter(매개변수)

라고 합니다.

---

### Argument(인자)

함수를 호출할 때

실제로 전달하는 값입니다.

```python
hello("Kim")
```

여기서

```python
"Kim"
```

이

Argument입니다.

---

비유하면

```text
Parameter

↓

빈 택배 상자

------------------

Argument

↓

실제로 넣는 물건
```

입니다.

---

### Parameter와 Argument의 차이

```text
def greet(name):
```

↓

name

↓

Parameter

---

```python
greet("OpenAI")
```

↓

"OpenAI"

↓

Argument

---

학습자가

매우 많이 헷갈리는 개념입니다.

---

### Return이란?

함수는

결과를 돌려줄 수도 있습니다.

예를 들어

```python
def add(a, b):
    return a + b
```

사용

```python
result = add(10,20)
```

결과

```text
30
```

---

### Return은 왜 필요할까?

예를 들어

OpenAI를 호출합니다.

```python
response = call_llm(prompt)
```

여기서

LLM이 생성한 결과를

다음 단계에서 사용해야 합니다.

따라서

함수는

결과를 반환해야 합니다.

---

비유하면

```text
재료 전달

↓

요리

↓

완성 음식 반환
```

입니다.

---

### Return과 print의 차이

많은 입문자가

가장 헷갈리는 부분입니다.

예를 들어

```python
def add(a,b):
    print(a+b)
```

는

화면에 출력만 합니다.

---

반면

```python
def add(a,b):
    return a+b
```

는

결과를

호출한 곳으로 돌려줍니다.

---

AI 서비스에서는

거의 대부분

return을 사용합니다.

왜냐하면

결과를

다음 함수가 계속 사용해야 하기 때문입니다.

---

### 함수 실행 과정

예를 들어

```python
result = add(10,20)
```

실제로는

```text
10

20

↓

add()

↓

계산

↓

30

↓

result
```

입니다.

---

### 함수 안의 변수

함수 안에서 만든 변수는

함수 밖에서는 사용할 수 없습니다.

```python
def test():
    message = "Hello"
```

여기서

```python
message
```

는

함수 안에서만 존재합니다.

이것을

**지역 변수(Local Variable)**

라고 합니다.

---

나중에

Scope(스코프)를 배울 때

더 자세히 학습합니다.

---

### AI 프로젝트에서 함수

실제 AI 프로젝트는

다음처럼 구성됩니다.

```python
def upload_file():
    ...

def extract_text():
    ...

def split_document():
    ...

def create_embedding():
    ...

def search_vector():
    ...

def call_llm():
    ...

def save_result():
    ...
```

그리고

```python
def main():

    upload_file()

    extract_text()

    split_document()

    create_embedding()

    search_vector()

    call_llm()

    save_result()
```

이런 형태가 됩니다.

즉

프로그램은

함수들의 연결입니다.

---

### 좋은 함수의 조건

좋은 함수는

하나의 일만 합니다.

좋은 예

```python
extract_text()
```

↓

텍스트 추출만 한다.

---

나쁜 예

```python
extract_text_and_save_database_and_send_email()
```

↓

너무 많은 일을 한다.

---

이를

**Single Responsibility Principle(단일 책임 원칙)**

이라고 합니다.

우리는 이후 FastAPI에서도

계속 이 원칙을 사용합니다.

---

### AI 서비스 Best Practice

AI 프로젝트에서는

함수 이름을

동사(Verb)로 시작하는 것이 일반적입니다.

예를 들어

```python
load_document()

save_result()

call_llm()

create_embedding()

search_vector()

split_text()
```

이런 이름만 봐도

무슨 일을 하는지

바로 이해할 수 있습니다.

---

### 자주 발생하는 오류와 오해

##### ① 함수를 정의하면 실행된다고 생각한다.

아닙니다.

호출해야 실행됩니다.

---

##### ② print와 return을 같은 것으로 생각한다.

print

↓

화면 출력

return

↓

값 반환

입니다.

---

##### ③ 하나의 함수에 너무 많은 기능을 넣는다.

함수는

한 가지 역할만 담당해야 합니다.

---

##### ④ 의미 없는 함수 이름을 사용한다.

```python
do()

run()

test()
```

보다

```python
extract_text()
```

처럼

역할이 드러나는 이름을 사용합니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **함수(Function)** 의 원리를 배웠습니다.

핵심은 다음과 같습니다.

- 함수는 **특정 작업을 수행하는 코드의 묶음**이다.
- 함수의 목적은 **재사용**, **유지보수**, **가독성**, **역할 분리**이다.
- `def`는 함수를 정의하고, `()`를 사용하여 함수를 호출한다.
- Parameter는 **함수를 정의할 때 받는 변수**, Argument는 **호출할 때 전달하는 실제 값**이다.
- `return`은 결과를 호출한 곳으로 돌려준다.
- AI 서비스는 여러 개의 작은 함수를 연결하여 하나의 큰 기능을 완성한다.

---

### AIKOS 학습 연결

```text
AI 서비스 아키텍처
        │
        ▼
Python 기초 문법
        │
        ▼
조건문
        │
        ▼
반복문
        │
        ▼
Function   ✅
        │
        ▼
다음 Unit
Module(모듈)과 Package(패키지)
```

---

## Unit 11. 모듈(Module), 패키지(Package), import와 프로젝트의 구조

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 10 ✅
>
> **Unit 11. Module(모듈)과 Package(패키지)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 모듈(Module)은 무엇인가?
- 패키지(Package)는 무엇인가?
- import는 어떻게 동작하는가?
- 왜 파일을 여러 개로 나누는가?
- AI 프로젝트는 어떤 구조로 관리하는가?

---

### ① 문제 이해 (Why)

지난 Unit에서 우리는

함수(Function)를 배웠습니다.

함수를 사용하면

코드를 재사용할 수 있습니다.

예를 들어

```python
def extract_text():
    ...

def split_text():
    ...

def create_embedding():
    ...

def search_vector():
    ...

def call_llm():
    ...
```

여기까지는 좋습니다.

---

그런데 AI 프로젝트가 커지면 어떻게 될까요?

예를 들어

```text
main.py

↓

함수 10개

↓

함수 30개

↓

함수 100개

↓

함수 300개
```

하나의 파일이

수천 줄이 됩니다.

---

이런 파일을

수정하려면 어떻게 될까요?

```text
main.py

4,500 Lines
```

원하는 함수를 찾는 것조차

어렵습니다.

---

실제 AI 프로젝트에서는

이런 구조를 사용하지 않습니다.

---

### 함수만으로는 부족하다.

함수는

하나의 기능을 분리합니다.

하지만

프로젝트 전체를 관리하기에는

부족합니다.

그래서

다음 단계가 필요합니다.

```text
Function

↓

Module

↓

Package

↓

Project
```

---

### 모듈(Module)이란?

모듈은

한 문장으로 정의하면

> **Python 파일(.py) 하나**

입니다.

예를 들어

```text
math.py

user.py

config.py

database.py
```

모두

모듈입니다.

---

즉

우리가 지금까지 만든

```text
hello.py
```

도

사실은 하나의 모듈입니다.

---

### 왜 Module이라고 부를까?

모듈(Module)은

기능 단위입니다.

예를 들어

```text
OCR

↓

ocr.py
```

---

```text
Embedding

↓

embedding.py
```

---

```text
OpenAI

↓

llm.py
```

---

기능별로

파일을 나누는 것입니다.

---

### AI 프로젝트 예제

예를 들어

Document AI 프로젝트라면

```text
document_ai/

│

├── main.py

├── pdf.py

├── ocr.py

├── embedding.py

├── llm.py

├── database.py
```

처럼

역할별로 나눕니다.

---

이렇게 하면

OCR를 수정할 때는

```text
ocr.py
```

만 열면 됩니다.

---

### import란?

모듈을 만들면

다른 파일에서

사용할 수 있어야 합니다.

이때 사용하는 것이

> **import**

입니다.

---

예를 들어

```python
### math_util.py

def add(a,b):
    return a+b
```

다른 파일에서

```python
import math_util
```

하면

이제

```python
math_util.add(10,20)
```

를 사용할 수 있습니다.

---

동작 구조

```text
main.py

↓

import

↓

math_util.py

↓

함수 사용
```

입니다.

---

### import는 복사일까?

많은 학습자가

이렇게 생각합니다.

> import하면
>
> 코드가 복사된다.

아닙니다.

Python은

모듈을 메모리에 로드한 뒤

참조합니다.

즉

```text
main.py

↓

참조

↓

math.py
```

입니다.

---

### import는 언제 실행될까?

예를 들어

```python
import openai
```

를 실행하면

Python은

대략 다음 순서로 동작합니다.

```text
모듈 찾기

↓

파일 읽기

↓

실행

↓

메모리에 저장

↓

사용 준비 완료
```

중요한 점은

모듈은

**처음 import될 때 한 번만 실행**됩니다.

---

### 여러 파일이 하나의 프로젝트를 만든다.

실무 프로젝트는

거의 모두

이런 구조입니다.

```text
Project

│

├── main.py

├── config.py

├── database.py

├── utils.py

├── service.py
```

각 파일은

하나의 역할만 담당합니다.

---

### Package란?

프로젝트가

더 커지면

파일도 많아집니다.

예를 들어

```text
main.py

config.py

database.py

user.py

admin.py

ocr.py

llm.py

vector.py

pdf.py

image.py

...
```

파일이

수십 개가 됩니다.

---

이번에는

파일도 정리해야 합니다.

그래서 등장하는 것이

Package입니다.

---

### Package란?

Package는

> **Python 모듈들을 모아 놓은 폴더**

입니다.

예를 들어

```text
app/

    api/

    models/

    services/

    utils/
```

여기서

각 폴더가

Package입니다.

---

### AIKOS에서 사용할 프로젝트 구조

Phase 1에서는

다음 구조를 표준으로 사용합니다.

```text
ai_project/

│

├── app/

│      ├── api/

│      ├── services/

│      ├── models/

│      ├── utils/

│      ├── config/

│

├── data/

│

├── tests/

│

├── docs/

│

├── main.py
```

이 구조는

이후 FastAPI에서도

그대로 사용합니다.

---

### 각 Package의 역할

#### api/

외부 요청을 받습니다.

```text
React

↓

API
```

---

#### services/

실제 비즈니스 로직입니다.

예를 들어

```text
OpenAI 호출

OCR

Embedding
```

등이 들어갑니다.

---

#### models/

데이터 구조를 정의합니다.

나중에

Pydantic에서

자세히 학습합니다.

---

#### utils/

공통 기능입니다.

예를 들어

```text
날짜

파일명 생성

문자열 처리
```

등입니다.

---

#### config/

설정을 관리합니다.

예를 들어

```text
API KEY

Model

환경변수
```

등을 관리합니다.

---

### 왜 이렇게 나눌까?

좋은 프로젝트는

역할이 명확합니다.

비유하면

병원과 같습니다.

```text
병원

↓

접수

↓

진료

↓

수납

↓

약국
```

모든 사람이

한 자리에서

모든 일을 하지 않습니다.

---

AI 프로젝트도 같습니다.

```text
API

↓

Service

↓

Database

↓

LLM
```

각자

역할을 담당합니다.

---

### import 방식

가장 많이 사용하는 방법은

```python
import module
```

입니다.

또는

```python
from module import function
```

도 사용할 수 있습니다.

예를 들어

```python
from math import sqrt
```

처럼

필요한 기능만 가져올 수도 있습니다.

---

### 어떤 import가 좋을까?

실무에서는

상황에 따라 다릅니다.

예를 들어

```python
import os
```

는

```python
os.path.join()
```

처럼 사용하는 것이

가독성이 좋습니다.

반면

```python
from pathlib import Path
```

처럼

자주 사용하는 객체는

직접 가져오기도 합니다.

---

AIKOS에서는

초기에는

다음 원칙을 권장합니다.

```python
import module
```

↓

명확하다.

---

필요할 때만

```python
from module import function
```

를 사용합니다.

---

### AI 프로젝트 예제

실제 AI 서비스에서는

다음과 같이 구성됩니다.

```python
### main.py

from services.llm import call_llm

from services.embedding import create_embedding

from services.ocr import extract_text
```

이후

```python
text = extract_text(file)

vector = create_embedding(text)

response = call_llm(vector)
```

이런 식으로

프로젝트 전체가 연결됩니다.

---

### import와 메모리

Python은

같은 모듈을

여러 번 import해도

매번 다시 읽지 않습니다.

```text
import

↓

이미 메모리에 있음?

↓

YES

↓

기존 객체 사용
```

이 덕분에

속도가 빨라집니다.

---

### AI 프로젝트 Best Practice

실무에서는

파일 하나가

500줄을 넘기기 시작하면

분리를 고려합니다.

또한

한 모듈은

하나의 책임만 가지도록 설계합니다.

예를 들어

```text
llm.py
```

는

LLM 호출만 담당합니다.

OCR 기능까지 넣지 않습니다.

---

### 자주 발생하는 오류와 오해

##### ① 모든 코드를 main.py에 작성한다.

프로젝트가 커질수록

유지보수가 어려워집니다.

---

##### ② 기능과 관계없이 파일을 나눈다.

파일은

역할 기준으로 분리해야 합니다.

---

##### ③ 같은 코드를 여러 파일에 복사한다.

공통 기능은

하나의 모듈로 만들어

import해서 사용합니다.

---

##### ④ import 순환(Circular Import)

A가 B를 import하고

B가 다시 A를 import하면

문제가 발생할 수 있습니다.

이 문제는

FastAPI 프로젝트에서

자세히 다룹니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **프로젝트를 구조적으로 설계하는 방법**을 배웠습니다.

핵심은 다음과 같습니다.

- **Module**은 하나의 `.py` 파일이다.
- **Package**는 여러 모듈을 모아 놓은 폴더이다.
- `import`는 다른 모듈의 기능을 재사용하기 위한 메커니즘이다.
- AI 프로젝트는 기능별(Module), 역할별(Package)로 분리하여 관리한다.
- 좋은 프로젝트 구조는 유지보수와 확장성을 크게 향상시킨다.

---

### AIKOS 학습 연결

```text
Python 기초
        │
        ▼
조건문
        │
        ▼
반복문
        │
        ▼
함수(Function)
        │
        ▼
Module
        │
        ▼
Package   ✅
        │
        ▼
다음 Unit
Exception(예외 처리)
```

---

## Unit 12. 예외 처리(Exception)와 안정적인 AI 서비스 만들기

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 11 ✅
>
> **Unit 12. Exception(예외 처리)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 예외(Exception)란 무엇인가?
- 오류라는 일반 용어와 Python의 예외는 어떤 관계인가?
- try / except는 어떻게 동작하는가?
- AI 서비스에서는 왜 예외 처리가 중요한가?
- 실무에서는 예외를 어떻게 관리하는가?

---

### ① 문제 이해 (Why)

지금까지 만든 프로그램은

항상 정상적으로 동작한다고 가정했습니다.

예를 들어

```python
documents = [
    "A.pdf",
    "B.pdf"
]

for document in documents:
    print(document)
```

문제없이 실행됩니다.

---

하지만 현실은 어떨까요?

AI 서비스는

항상 문제가 발생합니다.

예를 들어

```text
사용자가 PDF를 업로드하지 않았다.

↓

OpenAI 서버가 응답하지 않는다.

↓

인터넷이 끊어졌다.

↓

파일이 손상되었다.

↓

API Key가 틀렸다.

↓

JSON 형식이 잘못되었다.
```

이런 상황은

매일 발생합니다.

---

여기서 질문입니다.

프로그램은

오류가 하나 발생했다고

바로 종료되어야 할까요?

아니면

오류를 처리하고

계속 실행되어야 할까요?

실제 서비스는

당연히

후자를 선택합니다.

---

### 오류(Error)와 예외(Exception)의 관계

`오류(error)`는 프로그램에서 발생한 문제를 넓게 부르는 일반적인 표현입니다.

Python은 문제 상황을 **예외 객체와 예외 타입**으로 표현하고 전달합니다.
`SyntaxError`, `ValueError`, `FileNotFoundError`도 모두
Python 예외 계층에 포함됩니다.

문제가 발견되는 시점은 서로 다를 수 있습니다.

예를 들어 문법 오류는 정상적인 프로그램 실행이 시작되기 전에 발견될 수 있습니다.

```text
if True
    print("Hello")
```

결과

```text
SyntaxError
```

입니다. 이 코드는 문법부터 고쳐야 하므로 `try / except`로
정상 실행을 이어 가는 문제가 아닙니다.

반면 다음 문제는 문법 분석을 통과한 뒤 실행 중에 발생합니다.

```python
number = int("AI")
```

결과

```text
ValueError
```

입니다.

코드의 문법은 맞지만 입력값을 정수로 바꿀 수 없어 `ValueError`가 발생합니다.

따라서 `Error`와 `Exception`을 서로 완전히 반대되는 두 종류로
외우기보다, **오류는 문제를 가리키는 넓은 말이고 Python은 그 문제를
예외 타입과 객체로 다룬다**고 이해하는 편이 정확합니다.

AI 서비스에서는 파일, 네트워크, 사용자 입력, 외부 API처럼
실행 중 발생할 수 있는 예외를 예상하고 처리하는 일이 특히 중요합니다.

---

### Exception이 필요한 이유

예를 들어

PDF를 읽습니다.

```python
text = extract_text("report.pdf")
```

그런데

파일이 없다면?

```text
File Not Found
```

입니다.

이때

프로그램이 종료되면

서비스는 사용할 수 없습니다.

---

그래서

예외를 처리해야 합니다.

---

### try / except

Python에서는

예외를 처리하기 위해

다음 구조를 사용합니다.

```text
try:
    실행할 코드

except:
    오류 처리
```

---

예를 들어

```python
try:
    number = int("AI")

except:
    print("숫자로 변환할 수 없습니다.")
```

결과

```text
숫자로 변환할 수 없습니다.
```

프로그램은

종료되지 않습니다.

---

### 어떻게 동작할까?

Python은

다음 순서로 실행합니다.

```text
try

↓

실행

↓

오류 발생?

↓

NO

↓

계속 실행

-----------------

YES

↓

except 이동

↓

오류 처리

↓

계속 실행
```

---

### AI 서비스 예제

예를 들어

OpenAI를 호출합니다.

```python
response = client.responses.create(...)
```

만약

인터넷이 끊기면?

예외가 발생합니다.

---

실무에서는

이렇게 작성합니다.

```python
try:
    response = client.responses.create(...)

except:
    print("OpenAI 호출 실패")
```

이제

서비스가

갑자기 종료되지 않습니다.

---

### except는 어떤 오류를 처리할까?

사실

오류는

종류가 매우 많습니다.

예를 들어

```text
ValueError

TypeError

FileNotFoundError

KeyError

ZeroDivisionError
```

등이 있습니다.

---

예를 들어

```python
try:
    int("AI")

except ValueError:
    print("숫자가 아닙니다.")
```

이처럼

특정 예외만 처리할 수도 있습니다.

---

### 여러 개의 except

예를 들어

파일을 읽습니다.

```python
try:

    ...

except FileNotFoundError:

    ...

except PermissionError:

    ...

except Exception:

    ...
```

Python은

위에서 아래 순서대로

가장 먼저 맞는 예외를 처리합니다.

---

### Exception 객체

예외도

객체입니다.

따라서

오류 정보를 받을 수 있습니다.

```python
try:

    ...

except Exception as e:

    print(e)
```

예를 들어

```text
No such file or directory
```

같은

실제 오류 내용을 확인할 수 있습니다.

---

AI 서비스에서는

로그를 남길 때

매우 많이 사용합니다.

---

### else

예외가 발생하지 않았을 때만

실행됩니다.

```python
try:

    ...

except:

    ...

else:

    print("성공")
```

동작

```text
try

↓

오류 없음

↓

else 실행
```

---

### finally

성공하든

실패하든

반드시 실행됩니다.

```python
try:

    ...

finally:

    print("정리 작업")
```

예를 들어

파일을 닫거나

데이터베이스 연결을 종료할 때 사용합니다.

---

### 전체 구조

```python
try:

    ...

except:

    ...

else:

    ...

finally:

    ...
```

실무에서도

가장 많이 사용하는 형태입니다.

---

### AI 서비스에서 가장 많이 발생하는 예외

#### 파일 없음

```text
FileNotFoundError
```

---

#### JSON 오류

```text
JSONDecodeError
```

---

#### OpenAI API 오류

```text
APIConnectionError

AuthenticationError

RateLimitError
```

(실제 예외 이름은 사용하는 SDK 버전에 따라 달라질 수 있으며, 해당 SDK에서 제공하는 예외 클래스를 사용하는 것이 좋습니다.)

---

#### PDF 읽기 실패

```text
ValueError

RuntimeError
```

또는 라이브러리별 예외가 발생합니다.

---

#### 데이터 없음

```text
KeyError
```

---

### 실무 예제

예를 들어

Document AI를 만든다고 합시다.

```text
PDF 업로드

↓

PDF 읽기

↓

OCR

↓

Embedding

↓

LLM

↓

저장
```

각 단계마다

예외가 발생할 수 있습니다.

따라서

실무에서는

모든 단계에서

예외 처리를 합니다.

---

### 나쁜 예외 처리

많은 학습자가

다음처럼 작성합니다.

```python
try:

    ...

except:

    pass
```

이처럼 모든 예외를 한꺼번에 잡고 아무 처리 없이 숨기는 방식은
일반적으로 권장하지 않습니다.

왜냐하면

오류가 발생해도

아무것도 모른 채

계속 진행하기 때문입니다.

---

### 좋은 예외 처리

최소한

로그는 남겨야 합니다.

```python
try:

    ...

except Exception as e:

    print(e)
```

실무에서는

print 대신

Logging을 사용합니다.

Logging은

조금 뒤에 학습합니다.

---

### 예외를 너무 많이 잡으면 안 된다.

예를 들어

```text
except Exception:
```

은

모든 오류를 잡습니다.

편리하지만

너무 넓습니다.

가능하면

```text
except FileNotFoundError:
```

처럼

구체적으로 작성하는 것이 좋습니다.

---

### AI 프로젝트 Best Practice

예외는

숨기지 말고

의미 있게 처리합니다.

예를 들어

나쁜 예

```text
Error
```

좋은 예

```text
PDF 파일을 열 수 없습니다.

파일이 손상되었거나 존재하지 않습니다.
```

사용자가

이해할 수 있어야 합니다.

---

### 자주 발생하는 오류와 오해

##### ① 모든 except를 Exception으로 작성한다.

가능하면

구체적인 예외를 사용합니다.

---

##### ② except에서 아무것도 하지 않는다.

오류는

반드시 기록해야 합니다.

---

##### ③ try를 너무 크게 작성한다.

필요한 코드만

try 안에 넣는 것이 좋습니다.

---

##### ④ 정상 흐름을 예외 처리로 작성한다.

예외는

정말 예외적인 상황만

처리해야 합니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **예외 처리(Exception)** 의 원리를 배웠습니다.

핵심은 다음과 같습니다.

- Python은 문제 상황을 **예외 타입과 예외 객체**로 표현하고 전달하며, 일부 예외는 미리 예상할 수 있고 일부는 예상하지 못할 수도 있다.
- `try`는 예외가 발생할 수 있는 코드를 실행한다.
- `except`는 예외를 처리하여 프로그램이 갑자기 종료되지 않도록 한다.
- `else`는 예외가 없을 때 실행되고, `finally`는 정상적인 제어 흐름에서는 예외 발생 여부와 관계없이 정리 작업을 수행한다. 다만 프로세스가 강제 종료되는 상황까지 보장하는 것은 아니다.
- AI 서비스에서는 API 호출, 파일 처리, 네트워크 통신처럼 실패 가능성이 있는 경계에서 예외 처리가 중요하다.
- 좋은 예외 처리는 오류를 숨기는 것이 아니라 **적절히 기록하고 사용자에게 의미 있는 메시지를 제공하는 것**이다.

---

### AIKOS 학습 연결

```text
Python 기초
        │
        ▼
조건문
        │
        ▼
반복문
        │
        ▼
함수
        │
        ▼
모듈 / 패키지
        │
        ▼
Exception Handling   ✅
        │
        ▼
다음 Unit
File I/O(파일 입출력)
```

---

## Unit 13. 파일 입출력(File I/O)과 AI 서비스의 시작

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 12 ✅
>
> **Unit 13. File I/O(파일 입출력)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- 파일 입출력(File I/O)은 무엇인가?
- 왜 AI 서비스에서 가장 중요한 기능 중 하나인가?
- 파일은 메모리와 어떤 관계가 있는가?
- 파일을 읽고 쓰는 원리는 무엇인가?
- AI 프로젝트에서는 어떤 파일들을 다루는가?

---

### ① 문제 이해 (Why)

지금까지 우리는

Python 문법을 배웠습니다.

그런데 아직

진짜 AI 서비스를 만들 수는 없습니다.

왜일까요?

AI 서비스는 데이터를 입력받아 처리하기 때문입니다.

예를 들어

```text
사용자

↓

PDF 업로드

↓

AI 분석
```

또는

```text
사용자

↓

이미지 업로드

↓

OCR

↓

LLM
```

또는

```text
CSV 업로드

↓

데이터 분석

↓

AI 보고서 생성
```

특히 이번 과정에서 만들 Document AI 서비스는
PDF와 이미지 같은 **파일(File)** 을 주요 입력으로 사용합니다.

일반 AI 서비스의 입력은 파일뿐 아니라 JSON 요청, 데이터베이스 조회,
메시지 또는 실시간 Stream 등 다양한 형태가 될 수 있습니다.

---

### 프로그램은 데이터를 어디에 저장할까?

지난 Unit에서

우리는 객체(Object)를 배웠습니다.

객체는

메모리(Heap)에 저장됩니다.

```text
Python Object

↓

Heap Memory
```

그런데 문제가 있습니다.

메모리는

프로그램이 종료되면

모두 사라집니다.

예를 들어

```python
message = "Hello AI"
```

프로그램이 종료되면

```text
Heap Memory

↓

삭제
```

됩니다.

---

그렇다면

계속 보관해야 하는 데이터는

어디에 저장할까요?

바로

> **파일(File)**

입니다.

---

### 메모리와 파일의 차이

이 차이를 이해하는 것이 매우 중요합니다.

| 메모리(Memory)        | 파일(File)    |
| --------------------- | ------------- |
| 빠름                  | 느림          |
| 프로그램 종료 시 삭제 | 계속 유지     |
| 임시 데이터           | 영구 데이터   |
| CPU가 직접 사용       | 디스크에 저장 |

---

비유하면

메모리는

책상입니다.

파일은

서랍입니다.

```text
작업 중

↓

책상

(Memory)

-------------------

보관

↓

서랍

(File)
```

작업할 때는

책상을 사용하지만,

퇴근할 때는

서랍에 넣어둡니다.

---

AI 서비스도 같습니다.

```text
PDF

↓

Memory

↓

AI 처리

↓

결과

↓

File 저장
```

---

### 파일 입출력(File I/O)이란?

I/O는

Input / Output의 약자입니다.

즉,

```text
Input

↓

파일 읽기

------------------

Output

↓

파일 저장
```

입니다.

---

### AI 프로젝트에서 다루는 파일

실무에서는

다음과 같은 파일을 자주 다룹니다.

| 파일 종류 | 용도             |
| --------- | ---------------- |
| PDF       | 문서 분석        |
| TXT       | 텍스트 저장      |
| JSON      | API 데이터 저장  |
| CSV       | 데이터 분석      |
| PNG/JPG   | OCR, 이미지 분석 |
| DOCX      | 문서 처리        |
| XLSX      | 엑셀 데이터      |

Phase 1에서

이 파일들을

모두 다루게 됩니다.

---

### 파일을 읽는 과정

예를 들어

```text
report.txt
```

를 읽는다고 합시다.

실제로는

```text
Disk

↓

Operating System

↓

Python

↓

Memory

↓

String Object
```

순서로 동작합니다.

---

중요한 점은

파일을

직접 사용하는 것이 아니라

메모리로 읽어온 후

작업한다는 것입니다.

---

### 파일을 저장하는 과정

반대로

저장할 때는

```text
Python Object

↓

Memory

↓

Operating System

↓

Disk
```

입니다.

즉,

메모리와 파일은

계속 데이터를 주고받습니다.

---

### 왜 open()을 사용할까?

Python에서

파일을 읽으려면

먼저

파일을 열어야 합니다.

예를 들어

```python
file = open("hello.txt")
```

많은 입문자가

파일을 여는 것이

곧 읽는 것이라고 생각합니다.

하지만

그렇지 않습니다.

---

`open()`은

단지

> "파일을 사용할 준비"

를 하는 것입니다.

비유하면

책을 읽기 전에

책장을 여는 것과 같습니다.

```text
책장 열기

↓

책 꺼내기

↓

읽기

↓

책 넣기

↓

책장 닫기
```

---

파일도 같습니다.

```text
open()

↓

read()

↓

close()
```

---

### 파일은 왜 닫아야 할까?

운영체제는

파일을 사용할 수 있도록

자원을 할당합니다.

파일을 닫지 않으면

자원이 계속 사용됩니다.

그래서

반드시

닫아야 합니다.

---

예전에는

```python
file = open(...)

...

file.close()
```

를 사용했습니다.

---

하지만

실무에서는

거의 사용하지 않습니다.

---

### with 문

Python에서는

다음 방식을 사용합니다.

```text
with open(...) as file:
```

이 방식은

작업이 끝나면

자동으로

파일을 닫아 줍니다.

---

동작은

```text
open()

↓

사용

↓

자동 close()
```

입니다.

따라서 기본 `open()`으로 파일을 다룰 때는
가능하면 `with`를 사용해 닫기 작업을 자동으로 관리합니다.

---

### AI 서비스 예제

예를 들어

텍스트 파일을 읽습니다.

```text
prompt.txt

↓

Python

↓

String

↓

OpenAI API
```

또는

```text
config.json

↓

Dictionary

↓

환경 설정
```

또는

```text
report.pdf

↓

텍스트 추출

↓

Chunk

↓

Embedding
```

모두

파일 입출력입니다.

---

### File Path(파일 경로)

파일을 읽으려면

위치를 알아야 합니다.

예를 들어

```text
data/report.pdf
```

처럼

파일의 위치를

지정합니다.

---

프로젝트 구조에서는

```text
project/

    data/

        report.pdf

    output/

        summary.txt
```

처럼

폴더를 나누어 관리합니다.

---

### 상대 경로와 절대 경로

실무에서는

상대 경로를

더 많이 사용합니다.

예를 들어

```text
data/report.pdf
```

는

현재 프로젝트를 기준으로 찾습니다.

반면

```text
C:/Users/Kim/Documents/report.pdf
```

처럼

컴퓨터 전체 위치를 지정하는 것은

절대 경로입니다.

---

AI 프로젝트에서는

상대 경로를 사용하는 것이

프로젝트를 다른 컴퓨터로 옮기기 쉽습니다.

---

### AI 서비스에서 가장 많이 하는 파일 작업

```text
사용자 업로드

↓

저장

↓

읽기

↓

분석

↓

결과 저장

↓

다운로드
```

우리가 만들 Document AI도

이 흐름으로 동작합니다.

---

### 실무 Best Practice

파일을 다룰 때는

다음 원칙을 지킵니다.

① 기본 `open()`에는 `with` 사용

```text
with open(...) as file:
```

---

② 파일 존재 여부 확인

```text
존재?

↓

YES

↓

읽기

----------------

NO

↓

예외 처리
```

---

③ 인코딩을 명시한다.

텍스트 파일은

UTF-8을 사용하는 것이 일반적입니다.

---

④ 예외 처리를 함께 사용한다.

파일은

항상 실패할 가능성이 있습니다.

따라서

지난 Unit의

Exception과 함께 사용합니다.

---

### AI 프로젝트 연결

앞으로 Phase 1에서

계속 사용할 흐름입니다.

```text
PDF

↓

File I/O

↓

OCR

↓

Text

↓

Chunk

↓

Embedding

↓

Vector DB

↓

LLM

↓

Summary.txt 저장
```

즉,

File I/O는

Document AI와 파일 기반 AI 서비스의

중요한 출발점입니다.

---

### 자주 발생하는 오류와 오해

##### ① 메모리와 파일을 같은 것으로 생각한다.

메모리는

임시 저장입니다.

파일은

영구 저장입니다.

---

##### ② open()만 하면 읽은 것이라고 생각한다.

open은

준비만 합니다.

실제로는

read가 필요합니다.

(다음 Unit에서 자세히 학습합니다.)

---

##### ③ 파일을 닫지 않는다.

실무에서는

`with`를 사용하면

자동으로 닫힙니다.

---

##### ④ 절대 경로를 사용한다.

프로젝트에서는

상대 경로를 사용하는 것이 좋습니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **파일 입출력의 원리**를 이해했습니다.

핵심은 다음과 같습니다.

- 파일은 **프로그램이 종료되어도 유지되는 영구 저장소**이다.
- 이번 과정의 Document AI 서비스는 **파일을 주요 입력으로 받아 처리**한다. 일반 AI 서비스는 JSON, 메시지, 데이터베이스 조회, Stream 등 다양한 입력을 사용할 수 있다.
- 파일 작업은 **디스크 ↔ 메모리** 사이의 데이터 이동 과정이다.
- `open()`은 파일을 사용할 준비를 하고, 실무에서는 `with`를 사용하여 자동으로 파일을 닫는다.
- PDF, JSON, CSV, 이미지 등 다양한 파일 형식은 이후 AI 서비스 개발에서 핵심 입력 데이터가 된다.

---

### AIKOS 학습 연결

```text
Python 기초
        │
        ▼
조건문
        │
        ▼
반복문
        │
        ▼
함수
        │
        ▼
모듈
        │
        ▼
예외 처리
        │
        ▼
File I/O 원리   ✅
        │
        ▼
다음 Unit
텍스트 파일 읽기/쓰기와 Context Manager(with)의 실제 동작
```

---

## Unit 14. 텍스트 파일 읽기/쓰기와 Context Manager의 원리

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 13 ✅
>
> **Unit 14. Text File I/O와 Context Manager** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- `open()`은 실제로 무엇을 반환하는가?
- `read()`, `readline()`, `readlines()`의 차이는 무엇인가?
- `write()`는 어떻게 동작하는가?
- `with`는 왜 사용하는가?
- AI 서비스에서는 텍스트 파일을 어떻게 활용하는가?

---

### ① 문제 이해 (Why)

지난 Unit에서는

파일 입출력의 원리를 배웠습니다.

하지만 아직

실제로 파일을 읽지는 않았습니다.

예를 들어

AI 프로젝트에는

다음과 같은 텍스트 파일이 있습니다.

```text
prompt.txt
```

내용

```text
당신은 문서를 요약하는 AI입니다.
```

이 파일를

Python으로 읽어서

OpenAI에게 전달해야 합니다.

그렇다면

Python은

파일을 어떻게 읽을까요?

---

### open()은 무엇을 반환할까?

많은 입문자는

```python
file = open("prompt.txt")
```

를 보면

file 안에

문자열이 저장되었다고 생각합니다.

하지만

그렇지 않습니다.

---

실제로는

```text
prompt.txt

↓

open()

↓

File Object

↓

file
```

입니다.

즉,

`file`은 문자열이 아니라

> **파일 객체(File Object)**

입니다.

---

### File Object란?

지난 Unit에서

우리는

Everything is Object를 배웠습니다.

파일도

객체입니다.

```text
String Object

List Object

Dictionary Object

File Object
```

모두

객체입니다.

---

File Object는

다음과 같은 기능을 가지고 있습니다.

```text
read()

write()

close()

seek()

tell()
```

즉

파일을 다루는

기능을 가진 객체입니다.

---

### read()

가장 많이 사용하는 함수입니다.

```python
with open("prompt.txt") as file:

    text = file.read()
```

동작

```text
Disk

↓

File Object

↓

Memory

↓

String Object
```

결과

```python
text
```

안에는

파일의 모든 내용이

문자열(String)로 들어갑니다.

---

### AI 서비스에서 가장 많이 사용하는 방식

예를 들어

프롬프트를

파일에 저장했다고 합시다.

```text
prompt.txt

↓

당신은 AI입니다...
```

그러면

```python
with open(...) as file:

    prompt = file.read()
```

↓

```python
client.responses.create(
    ...
)
```

이런 흐름이 됩니다.

실무에서도

가장 많이 사용하는 패턴입니다.

---

### readline()

이번에는

한 줄만 읽습니다.

예를 들어

```text
Line1

Line2

Line3
```

가 있다면

```python
line = file.readline()
```

결과

```text
Line1
```

입니다.

다시

```python
file.readline()
```

을 호출하면

```text
Line2
```

가 반환됩니다.

---

### 왜 그럴까?

파일 객체는

현재 위치를

기억하기 때문입니다.

```text
파일

↓

현재 위치(Cursor)

↓

다음 읽기
```

입니다.

---

### Cursor(커서)

파일에는

읽는 위치가 있습니다.

예를 들어

```text
ABCDEF

^

처음
```

한 글자를 읽으면

```text
ABCDEF

 ^

다음 위치
```

입니다.

이것을

파일 포인터(File Pointer) 또는

커서(Cursor)라고 합니다.

---

### readlines()

이번에는

모든 줄을

리스트로 읽습니다.

예를 들어

```text
A

B

C
```

↓

```python
lines = file.readlines()
```

결과

```python
[
    "A\n",
    "B\n",
    "C"
]
```

입니다.

---

### read()와 readlines() 차이

| read()                           | readlines()           |
| -------------------------------- | --------------------- |
| 문자열 반환                      | 리스트 반환           |
| 파일 전체를 하나의 문자열로 읽음 | 한 줄씩 리스트에 저장 |

---

AI에서는

둘 다 많이 사용합니다.

예를 들어

Prompt는

```python
read()
```

가 많고,

로그 파일은

```python
readlines()
```

를 많이 사용합니다.

---

### write()

파일에

저장하는 함수입니다.

```python
with open("result.txt","w") as file:

    file.write("Hello AI")
```

동작

```text
String

↓

File Object

↓

Disk
```

입니다.

---

### "w"는 무엇일까?

open에는

모드(Mode)가 있습니다.

대표적으로

| 모드 | 설명         |
| ---- | ------------ |
| r    | 읽기(Read)   |
| w    | 쓰기(Write)  |
| a    | 추가(Append) |

---

예를 들어

```python
open("a.txt","r")
```

↓

읽기

---

```python
open("a.txt","w")
```

↓

새로 쓰기

---

```python
open("a.txt","a")
```

↓

뒤에 이어쓰기

---

### append()

AI 로그는

계속 추가됩니다.

예를 들어

```text
사용자 질문

↓

LLM 응답

↓

사용자 질문

↓

LLM 응답
```

이런 경우

기존 내용을

지우면 안 됩니다.

따라서

Append Mode를 사용합니다.

---

### Encoding

텍스트 파일에는

문자 인코딩이 있습니다.

텍스트 파일은 호환성이 높은 `UTF-8`을 우선 고려합니다.

다만 외부 시스템에서 받은 파일은 EUC-KR 등 다른 인코딩일 수 있으므로
파일을 만든 시스템과 데이터 형식을 확인해야 합니다.

예를 들어

```python
with open(
    "prompt.txt",
    encoding="utf-8"
) as file:
    text = file.read()
```

입니다.

---

왜 필요할까?

예를 들어

한글 파일을

잘못 읽으면

```text
����
```

처럼

깨질 수 있습니다.

---

### with는 어떻게 동작할까?

지난 Unit에서는

자동으로 close한다고 배웠습니다.

이번에는

조금 더 깊게 이해해봅시다.

```text
with open(...) as file:
```

실제로는

```text
open()

↓

File Object 생성

↓

사용

↓

예외 발생?

↓

YES / NO

↓

무조건 close()
```

입니다.

즉

예외가 발생해도

파일은

닫힙니다.

---

### Context Manager

with는

사실

Context Manager라는 기능입니다.

현재는

이 정도만 이해하면 됩니다.

```text
자원 획득

↓

사용

↓

자동 정리
```

입니다.

파일뿐 아니라

Database

Network

Lock

등도

같은 구조를 사용합니다.

---

### AI 프로젝트 예제

실제 프로젝트에서는

```text
system_prompt.txt
```

↓

```python
prompt = read()
```

↓

```text
사용자 질문
```

↓

```python
prompt + question
```

↓

LLM 호출

이런 흐름이

매우 많습니다.

---

### 실무 Best Practice

① 기본 `open()`에는 `with` 사용

```text
with open(...)
```

---

② UTF-8 명시

```python
encoding="utf-8"
```

---

③ Prompt는 txt로 관리

예를 들어

```text
prompts/

    summary.txt

    translate.txt

    qa.txt
```

처럼

프롬프트를

파일로 관리하면

수정하기 쉽습니다.

---

④ 결과도 파일로 저장

```text
output/

summary.txt

report.txt
```

---

### AI 서비스 연결

Document AI에서는

다음과 같이 사용됩니다.

```text
PDF

↓

텍스트 추출

↓

summary.txt 저장

↓

LLM

↓

result.txt 저장
```

---

Prompt Engineering에서도

```text
Prompt Template

↓

txt

↓

Python

↓

OpenAI
```

형태를

가장 많이 사용합니다.

---

### 자주 발생하는 오류와 오해

##### ① open()이 문자열을 반환한다고 생각한다.

아닙니다.

File Object를 반환합니다.

---

##### ② write()가 이어쓴다고 생각한다.

`w`

는

기존 내용을

지웁니다.

---

##### ③ read()와 readlines()를 혼동한다.

read

↓

문자열

readlines

↓

리스트

---

##### ④ UTF-8을 지정하지 않는다.

한글 프로젝트에서는

반드시

UTF-8을 사용하는 습관을 들입니다.

---

##### ⑤ 파일을 직접 close()한다.

실무에서는

with를 사용합니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **텍스트 파일을 실제로 다루는 방법**을 배웠습니다.

핵심은 다음과 같습니다.

- `open()`은 **파일 객체(File Object)** 를 반환한다.
- `read()`는 파일 전체를 문자열로 읽고, `readline()`은 한 줄씩, `readlines()`는 모든 줄을 리스트로 읽는다.
- `write()`는 파일에 데이터를 저장하며, `"w"`는 덮어쓰기, `"a"`는 이어쓰기를 의미한다.
- `with`는 **Context Manager**를 사용하여 파일을 안전하게 열고 자동으로 닫는다.
- AI 서비스에서는 프롬프트, 로그, 결과 보고서 등을 텍스트 파일로 관리하는 경우가 매우 많다.

---

### AIKOS 학습 연결

```text
Python 기초
        │
        ▼
조건문
        │
        ▼
반복문
        │
        ▼
함수
        │
        ▼
모듈
        │
        ▼
예외 처리
        │
        ▼
텍스트 File I/O   ✅
        │
        ▼
다음 Unit
JSON 파일과 CSV 파일 처리
```

---

## Unit 15. JSON의 원리와 AI 서비스에서 가장 많이 사용하는 데이터 형식

> **AIKOS Phase 1 커리큘럼**
>
> ① AI 애플리케이션 아키텍처 ✅
>
> **② Python for AI** ← 현재 학습
>
> Unit 1 ~ Unit 14 ✅
>
> **Unit 15. JSON(JavaScript Object Notation)** ← 현재 학습

---

### 이번 Unit 학습 목표

이번 Unit이 끝나면 다음 질문에 답할 수 있어야 합니다.

- JSON은 무엇인가?
- 왜 AI 서비스에서 JSON이 가장 중요한 데이터 형식인가?
- Dictionary와 JSON은 무엇이 다른가?
- Python에서 JSON을 어떻게 읽고 저장하는가?
- OpenAI API와 FastAPI는 왜 JSON을 사용하는가?

---

### ① 문제 이해 (Why)

지금까지 우리는

Python 안에서 데이터를 다루었습니다.

예를 들어

```python
user = {
    "name": "Kim",
    "age": 20
}
```

이 데이터는

Python 프로그램 안에서는 사용할 수 있습니다.

그런데 질문이 하나 생깁니다.

> React는 이 데이터를 어떻게 받을까요?

또는

> OpenAI 서버는 Python Dictionary를 이해할까요?

정답은

**아니오.**

Python Dictionary는 Python 실행 환경에서 사용하는 객체입니다.

다른 프로그램과 데이터를 주고받으려면

모두가 이해할 수 있는 공통 언어가 필요합니다.

그것이

> **JSON**

입니다.

---

### Python 프로그램은 혼자 존재하지 않는다.

Phase 1에서 우리가 만들 서비스를 다시 떠올려 봅시다.

```text
React

↓

FastAPI

↓

OpenAI API

↓

Vector DB

↓

Database
```

이 시스템들은

모두 서로 다른 프로그램입니다.

각 프로그램은

서로 데이터를 주고받습니다.

---

그렇다면

어떤 형식으로 데이터를 보낼까요?

바로

JSON입니다.

---

### JSON이 등장한 이유

예전에는

프로그램마다

데이터 형식이 달랐습니다.

예를 들어

```text
Program A

↓

자체 형식

------------------

Program B

↓

XML

------------------

Program C

↓

CSV

------------------

Program D

↓

Binary
```

서로 통신하기가 매우 어려웠습니다.

---

그래서

누구나 사용할 수 있는

가볍고 읽기 쉬운 형식이 만들어졌습니다.

그것이

JSON입니다.

---

### JSON이란?

JSON은

> **데이터를 저장하거나 프로그램끼리 주고받기 위한 표준 형식**

입니다.

중요한 점은

JSON은

프로그래밍 언어가 아니라

**데이터 형식(Data Format)** 이라는 것입니다.

---

### JSON은 어떻게 생겼을까?

예를 들어

사용자 정보입니다.

```json
{
  "name": "Kim",
  "age": 20,
  "city": "Seoul"
}
```

사람도 읽기 쉽고

컴퓨터도 읽기 쉽습니다.

---

### Dictionary와 매우 비슷하다.

Python에서는

이렇게 생겼습니다.

```python
user = {
    "name": "Kim",
    "age": 20
}
```

JSON도

```json
{
  "name": "Kim",
  "age": 20
}
```

거의 같습니다.

그래서

많은 사람들이

같은 것이라고 생각합니다.

하지만

엄밀히 말하면

다릅니다.

---

### Dictionary와 JSON의 차이

이 부분은 매우 중요합니다.

| Dictionary                     | JSON                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| Python의 Key-Value 객체        | 언어에 독립적인 텍스트 데이터 형식                           |
| Python 실행 중 메모리에서 사용 | 문자열로 만들고 Byte로 인코딩해 파일 저장·네트워크 전송 가능 |
| Python 코드에서 직접 사용      | 다양한 언어의 JSON Parser로 해석 가능                        |

즉,

Dictionary는

객체(Object)이고,

JSON은

문자열(String) 기반의 데이터 형식입니다.

---

### 메모리 구조로 이해하기

```python
user = {
    "name": "Kim"
}
```

메모리에는

```text
Dictionary Object

↓

Heap Memory
```

가 존재합니다.

---

이 Dictionary를

JSON으로 변환하면

```json
{
  "name": "Kim"
}
```

문자열이 됩니다.

즉

```text
Dictionary

↓

JSON 문자열

↓

파일

↓

네트워크
```

입니다.

---

### 왜 문자열일까?

네트워크는 최종적으로 Byte를 전송합니다.

따라서 Python 객체를 그대로 보내는 대신 JSON 문자열로 직렬화하고,
UTF-8 같은 인코딩을 사용해 Byte로 변환하여 전송할 수 있습니다.

이를

> **Serialization(직렬화)**

라고 합니다.

---

반대로 JSON 문자열을 그 구조에 대응하는 Python 객체로 바꾸는 것을

> **Deserialization(역직렬화)**

라고 합니다.

---

### Python에서는 어떻게 할까?

Python에는

JSON을 다루는 표준 라이브러리가 있습니다.

```python
import json
```

이 라이브러리는

Python에 기본 포함되어 있으므로

별도 설치가 필요 없습니다.

---

### Python 객체 → JSON

Python 객체를

JSON 문자열로 변환합니다.

```python
import json

user = {
    "name": "Kim",
    "age": 20
}

json_text = json.dumps(user)
```

여기서

`dumps`

는

**dump string**

이라고 기억하면 됩니다.

결과는

JSON 문자열입니다.

---

### JSON → Python 객체

반대로

JSON 문자열을

Python 객체로 변환합니다.

```python
import json

json_text = '{"name":"Kim"}'

user = json.loads(json_text)
```

여기서

`loads`

는

**load string**

입니다.

이 예제의 최상위 JSON 값은 Object이므로 결과는 Dictionary입니다.

JSON의 최상위 값이 Array이면 List가 반환되고, 문자열·숫자·Boolean·`null`은
각각 대응하는 `str`, `int` 또는 `float`, `bool`, `None`으로 변환됩니다.

| JSON    | Python         |
| ------- | -------------- |
| Object  | dict           |
| Array   | list           |
| String  | str            |
| Number  | int 또는 float |
| Boolean | bool           |
| null    | None           |

---

### JSON 파일 저장

파일로 저장할 수도 있습니다.

```python
import json

user = {
    "name": "Kim"
}

with open(
    "user.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(user, file, ensure_ascii=False, indent=4)
```

---

#### 각 옵션의 의미

```python
ensure_ascii=False
```

↓

한글 같은 비 ASCII 문자를 `\uXXXX` 형태로 Escape하지 않고
사람이 읽을 수 있는 문자 그대로 출력합니다.

---

```python
indent=4
```

↓

사람이 읽기 좋게

들여쓰기를 추가합니다.

---

### JSON 파일 읽기

```python
import json

with open(
    "user.json",
    encoding="utf-8"
) as file:

    user = json.load(file)
```

파일의 최상위 JSON 값이 Object이므로 이 예제에서는 Dictionary가 반환됩니다.

---

### dump()와 dumps()

많은 학습자가

매우 헷갈립니다.

| 함수    | 역할        |
| ------- | ----------- |
| dump()  | 파일에 저장 |
| dumps() | 문자열 반환 |

---

반대로

| 함수    | 역할        |
| ------- | ----------- |
| load()  | 파일 읽기   |
| loads() | 문자열 읽기 |

---

### AI 서비스에서 JSON

우리가 앞으로

OpenAI를 호출하면

HTTP API의 원본 응답 본문은 JSON인 경우가 많습니다.

다만 Python SDK는 JSON을 그대로 돌려주지 않고 편의를 위한 응답 객체로
변환할 수 있으므로, 사용하는 SDK의 반환 타입을 확인해야 합니다.

예를 들어

```json
{
  "model": "gpt-5",
  "usage": {
    "input_tokens": 500,
    "output_tokens": 120
  }
}
```

Python에서는

Dictionary처럼

사용하게 됩니다.

---

### FastAPI도 JSON

FastAPI는

기본적으로

JSON을 사용합니다.

예를 들어

React가

```json
{
  "question": "AI란 무엇인가?"
}
```

를 보내면

FastAPI가

이를 Python 객체로 변환합니다.

---

응답도

```json
{
  "answer": "AI는..."
}
```

형태로 반환합니다.

즉

FastAPI의 핵심 데이터 형식도

JSON입니다.

---

### AI 프로젝트에서 JSON을 사용하는 곳

거의 모든 곳입니다.

```text
환경 설정(config)

↓

OpenAI API 요청

↓

OpenAI API 응답

↓

FastAPI Request

↓

FastAPI Response

↓

로그 저장

↓

Document Metadata
```

---

### 실무 프로젝트 예제

실제 AI 프로젝트에서는

다음과 같은 파일이 존재합니다.

```text
config/

    model.json

    prompt.json

    settings.json
```

또는

```text
output/

    result.json

    metadata.json

    usage.json
```

JSON은

사람도 읽을 수 있고

프로그램도 처리하기 쉽기 때문에

매우 많이 사용됩니다.

---

### JSON과 AI 서비스의 흐름

앞으로 만들 서비스를 보면

```text
React

↓

JSON

↓

FastAPI

↓

Dictionary

↓

OpenAIconst [text, setText] = useState("");

const [fileName, setFileName] = useState("");



async function handleFileChange(event) {

const file = event.target.files?.[0];

if (!file) return;



setText(await file.text());

setFileName(file.name);

event.target.value = ""; // 같은 파일을 다시 선택해도 반영되도록 초기화

}



return (

<main className="mx-auto max-w-3xl px-4 py-10">

<h1 className="mb-6 text-3xl font-bold">Ollama Doc Assistant</h1>



<div className="mb-2 flex items-center justify-between">

<label

htmlFor="doc-text"

className="block text-sm font-medium text-gray-700"

>

요약할 문서

</label>



<label className="cursor-pointer rounded-lg border border-gray-300 px-3 py-1.5 text-sm hover:bg-gray-50">

파일 첨부 (.md, .txt)

<input

type="file"

accept=".md,.txt"

onChange={handleFileChange}

className="hidden"

/>

</label>

</div>



{fileName && (

<p className="mb-2 text-sm text-gray-500">첨부된 파일: {fileName}</p>

)}

↓

JSON

↓

Dictionary

↓

React
```

즉

JSON과 Dictionary를

계속 변환하게 됩니다.

---

### 실무 Best Practice

① UTF-8 사용

```python
encoding="utf-8"
```

---

② `indent=4`

사람이 읽기 쉽게 저장합니다.

---

③ 사람이 읽기 쉬운 비 ASCII 문자 출력이 필요하면 `ensure_ascii=False`

기본값인 `True`도 유효한 JSON을 만들지만 한글 등이 `\uXXXX` 형태로
Escape됩니다. 파일 인코딩 문제는 별도로 `encoding="utf-8"`을 확인합니다.

---

④ JSON 구조를 미리 설계한다.

AI 프로젝트에서는

데이터 구조(JSON Schema)를 먼저 설계한 후

개발을 시작하는 경우가 많습니다.

이 개념은 FastAPI와 API 설계에서 다시 다룹니다.

---

### 자주 발생하는 오류와 오해

##### ① Dictionary와 JSON을 같은 것으로 생각한다.

Dictionary는

Python 객체입니다.

JSON은

텍스트 형식입니다.

---

##### ② dump와 dumps를 혼동한다.

`dump`

↓

파일

`dumps`

↓

문자열

---

##### ③ load와 loads를 혼동한다.

`load`

↓

파일

`loads`

↓

문자열

---

##### ④ 한글이 `\uXXXX` 형태로 보여 깨진 것으로 오해한다.

`ensure_ascii=True`가 만든 Escape 표기도 정상 JSON이며 다시 읽으면
원래 문자열로 복원됩니다. 사람이 파일을 직접 읽기 쉽게 만들고 싶다면
`ensure_ascii=False`를 사용하고, 실제 글자 깨짐은 파일 인코딩을 확인합니다.

---

##### ⑤ JSON에 주석을 작성한다.

표준 JSON은

주석을 지원하지 않습니다.

설명은

별도의 문서나 다른 필드로 관리해야 합니다.

---

### 이번 Unit 핵심 정리

이번 Unit에서는 **JSON의 원리와 AI 서비스에서의 역할**을 이해했습니다.

핵심은 다음과 같습니다.

- JSON은 **프로그램 간 데이터를 교환하기 위한 표준 데이터 형식**이다.
- Dictionary는 Python 객체이고, JSON은 문자열 기반의 데이터 형식이다.
- `json.dumps()`는 JSON으로 표현 가능한 Python 객체를 JSON 문자열로 변환하고, `json.loads()`는 JSON 문자열을 구조에 대응하는 Python 객체로 변환한다.
- `json.dump()`와 `json.load()`는 JSON 파일을 저장하고 읽는 함수이다.
- OpenAI API와 많은 Web API는 요청·응답 본문에서 JSON을 널리 사용하며, FastAPI와 React를 연결할 때도 자주 활용한다.

---

### AIKOS 학습 연결

```text
Python 기초
        │
        ▼
File I/O
        │
        ▼
Text File
        │
        ▼
JSON   ✅
        │
        ▼
다음 Unit
Collection과 데이터 구조
```

---

---

# Part 2. FastAPI를 읽기 위한 실전 Python

Part 1에서 Python의 기본 원리를 배웠다. 이제 같은 개념을 **AI Backend 코드에서 실제로 어떻게 사용하는지** 다시 본다.

일부 내용은 앞에서 배운 내용과 겹친다. 의도적인 반복이다. 처음에는 Python 자체를 이해하기 위해 배웠고, 여기서는 다음과 같이 Backend 관점에서 다시 해석한다.

```text
List / Dictionary
  → Request와 Response 데이터

Function
  → Service 로직

Class / Object
  → Service, Repository, Provider Client

Decorator
  → FastAPI Routing

Type Hint
  → 데이터 계약과 자동 검증의 기반

Dataclass / Composition
  → 객체 설계와 책임 분리
```

## Part 2-1. Collection을 Backend 데이터 구조로 다시 보기

### Module 01. 컬렉션(Collection)과 자료구조의 이해

#### Module 실습 예제

- [예제 1: collection_basics.py](examples/module_01/collection_basics.py) — List·Tuple·Set·Dictionary의 선택 기준을 확인합니다.
- [예제 2: ai_payload_collection.py](examples/module_01/ai_payload_collection.py) — AI 요청과 검색 결과를 Collection으로 모델링합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Collection이란 무엇인가?
- Python에는 왜 여러 Collection이 존재하는가?
- List, Tuple, Set, Dictionary는 언제 사용하는가?
- AI 개발에서는 각각 어디에 사용하는가?
- 앞으로 배우게 될 데이터 처리에서 Collection이 왜 중요한가?

---

#### ① 문제 이해 (Why)

#### 지금까지 배운 내용의 한계

우리는 지금까지 다음과 같은 변수들을 사용했습니다.

```python
name = "Kim"
age = 30
score = 95
```

각 변수는 하나의 값만 저장합니다.

그런데 현실의 프로그램은 어떨까요?

예를 들어 학생 100명의 이름을 저장한다고 생각해봅시다.

```python
student1 = "Kim"
student2 = "Lee"
student3 = "Park"
...
student100 = "Choi"
```

이렇게 만드는 것은 사실상 불가능합니다.

---

이번에는 AI 서비스를 생각해봅시다.

사용자가 업로드한 PDF가 있습니다.

```
page1
page2
page3
...
page150
```

각 페이지를 변수 하나씩 만들까요?

```python
page1 = ...
page2 = ...
page3 = ...
```

역시 비효율적입니다.

---

그렇다면 하나의 변수 안에 여러 데이터를 저장할 수 있다면 어떨까요?

```
pages

├── page1
├── page2
├── page3
└── ...
```

훨씬 관리하기 쉬워집니다.

이것이 Collection이 등장한 이유입니다.

---

#### Collection이 해결하는 문제

Collection은

> **"여러 개의 데이터를 하나로 관리한다."**

를 해결하기 위해 만들어졌습니다.

예를 들어

학생 목록

```
Kim
Lee
Park
Choi
```

한 변수로 관리합니다.

```python
students = ["Kim", "Lee", "Park", "Choi"]
```

이제 학생이 몇 명이든

```
10명

100명

10,000명
```

모두 하나의 변수에서 관리할 수 있습니다.

---

#### AI 서비스에서는?

많은 AI 서비스의 주요 데이터 흐름은 Collection으로 표현할 수 있습니다.

예를 들어

사용자의 질문

```
Question1
Question2
Question3
```

LLM에게 보낼 Message

```
System

User

Assistant
```

검색된 문서

```
Doc1

Doc2

Doc3

Doc4
```

OCR 결과

```
Line1

Line2

Line3
```

Embedding

```
Vector1

Vector2

Vector3
```

거의 모든 데이터가 Collection 형태입니다.

즉,

AI 서비스를 개발한다는 것은

> **Collection을 다루는 프로그램을 만든다고 해도 과언이 아닙니다.**

---

#### Collection을 모르면 생기는 문제

예를 들어 PDF를 읽었다고 해봅시다.

페이지가 300장입니다.

페이지마다 OCR을 해야 합니다.

Collection을 모른다면

```
page1 OCR

page2 OCR

page3 OCR
```

하나씩 처리해야 합니다.

하지만 Collection을 배우면

```python
for page in pages:
    OCR(page)
```

한 줄로 끝납니다.

---

#### AI 프로젝트에서 Collection이 등장하는 곳

| 기능        | Collection 사용 |
| ----------- | --------------- |
| PDF 페이지  | List            |
| OCR 결과    | List            |
| 검색 결과   | List            |
| 채팅 기록   | List            |
| 사용자 정보 | Dictionary      |
| 환경설정    | Dictionary      |
| 파일 목록   | List            |
| 중복 제거   | Set             |

많은 AI 프로젝트에서 Collection은 데이터 흐름을 구성하는 핵심 자료구조입니다.

---

#### ② 개념 이해 (Concept)

#### Collection이란?

Collection은

> **여러 개의 데이터를 하나의 객체(Object)로 관리하는 자료형입니다.**

예를 들어

```
학생

Kim
Lee
Park
```

Collection으로 표현하면

```
Students

├── Kim
├── Lee
└── Park
```

---

Collection은 단순한 배열이 아닙니다.

각 Collection은

- 저장 방식
- 검색 방식
- 수정 방식
- 삭제 방식

이 서로 다릅니다.

그래서 목적에 따라 다른 Collection을 사용합니다.

---

#### Python의 대표 Collection

Python에는 대표적으로 네 가지 Collection이 있습니다.

```
Collection

├── List
├── Tuple
├── Set
└── Dictionary
```

이 네 가지가 Python 개발의 핵심입니다.

---

#### ① List

가장 많이 사용하는 Collection입니다.

```
학생 목록

Kim
Lee
Park
```

```python
students = ["Kim", "Lee", "Park"]
```

특징

- 순서 있음
- 수정 가능
- 중복 허용

---

예를 들어

```
0
1
2
```

라는 위치(Index)를 가집니다.

```
0 → Kim

1 → Lee

2 → Park
```

---

#### ② Tuple

Tuple도 여러 개를 저장합니다.

```python
point = (10, 20)
```

하지만

Tuple 자체의 요소 참조를 추가·교체·삭제할 수 없습니다.

```
Tuple

읽기 가능

수정 불가
```

왜 이런 것이 필요할까요?

요소의 개수와 위치가 의미를 가지는 고정된 구조를 표현하기 위해서입니다.

예를 들어

```
RGB

(255,255,255)
```

GPS 좌표

```
(37.56,126.97)
```

등은 함부로 변경되면 안 됩니다.

---

#### ③ Set

Set은

중복을 허용하지 않습니다.

```python
numbers = {1,2,3}
```

만약

```python
numbers = {1,2,2,2,3}
```

라면

결과는

```
1
2
3
```

입니다.

---

AI에서는

검색 결과 중복 제거

문서 중복 제거

파일 중복 제거

등에서 많이 사용됩니다.

---

#### ④ Dictionary

가장 중요한 Collection 중 하나입니다.

Dictionary는

값을 이름으로 찾습니다.

예를 들어

```python
student = {
    "name": "Kim",
    "age": 30
}
```

이 구조는

```
name → Kim

age → 30
```

입니다.

---

List는

```
0

1

2
```

처럼 위치로 찾습니다.

Dictionary는

```
"name"

"age"
```

처럼 Key로 찾습니다.

이 차이가 매우 중요합니다.

---

#### Collection 비교

| 종류       | 순서              | 수정 | 중복       | 검색 기준 |
| ---------- | ----------------- | ---- | ---------- | --------- |
| List       | O                 | O    | O          | Index     |
| Tuple      | O                 | X    | O          | Index     |
| Set        | X                 | O    | X          | Value     |
| Dictionary | O(삽입 순서 유지) | O    | Key 중복 X | Key       |

---

#### 객체(Object) 관점에서 이해하기

우리는 Unit 4에서

모든 변수는 객체를 참조한다고 배웠습니다.

Collection도 마찬가지입니다.

```python
numbers = [1,2,3]
```

실제로는

```
numbers

↓

List Object

├──1
├──2
└──3
```

입니다.

즉,

Collection도 하나의 Object입니다.

다만

그 안에

여러 Object를 저장하는 것입니다.

---

#### Collection 안에는 무엇이 들어갈 수 있을까?

모든 객체가 들어갈 수 있습니다.

```python
[
    1,
    3.14,
    "Hello",
    True
]
```

심지어

Collection 안에 Collection도 들어갑니다.

```python
[
    [1,2],
    [3,4]
]
```

이러한 **중첩(Collection of Collections)** 구조는 AI 데이터 처리에서 매우 흔하게 사용됩니다.

---

#### AI 서비스에서의 역할 (Architecture)

```
사용자

   │

   ▼

PDF 업로드

   │

   ▼

Page List
(List)

   │

   ▼

OCR Result
(List)

   │

   ▼

Embedding
(List)

   │

   ▼

Vector Search

   │

   ▼

Retrieved Documents
(List)

   │

   ▼

LLM Messages
(List + Dictionary)

   │

   ▼

Response
```

여기서 주목해야 할 점은 **거의 모든 단계가 Collection을 기반으로 데이터를 전달**한다는 것입니다.

---

#### 이번 Unit 핵심 정리

이번 Unit에서는 **Collection이 왜 필요한지와 Python의 대표적인 Collection 종류**를 이해했습니다.

핵심은 다음과 같습니다.

- 변수 하나에는 하나의 값만 저장하는 것이 아니라, Collection을 사용하면 여러 값을 하나의 객체로 관리할 수 있다.
- Python의 대표 Collection은 **List, Tuple, Set, Dictionary** 네 가지이다.
- 각 Collection은 저장 방식과 검색 방식이 다르므로 목적에 맞게 선택해야 한다.
- AI 서비스에서는 PDF 페이지, OCR 결과, 검색 결과, 대화 기록, 환경 설정 등 대부분의 데이터가 Collection 형태로 관리된다.
- Collection 역시 하나의 객체(Object)이며, 내부에는 다른 객체나 또 다른 Collection을 저장할 수 있다.

---

### Module 02. List - Python에서 가장 많이 사용하는 Collection

#### Module 실습 예제

- [예제 1: list_operations.py](examples/module_02/list_operations.py) — List의 추가·수정·삭제·순회를 연습합니다.
- [예제 2: chat_messages.py](examples/module_02/chat_messages.py) — 대화 메시지를 List로 누적하고 마지막 메시지를 조회합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- List는 내부적으로 어떻게 동작하는가?
- Index는 왜 0부터 시작하는가?
- List와 Object는 어떤 관계인가?
- List의 요소를 추가·수정·삭제하는 원리를 이해한다.
- AI 프로젝트에서 List를 어떻게 활용하는가?

---

#### ① 문제 이해 (Why)

지난 Unit에서는 Collection의 종류를 살펴보았습니다.

그중에서도 Python에서 가장 많이 사용하는 Collection은 List입니다.

왜 그럴까요?

AI 서비스를 하나 떠올려 봅시다.

사용자가 PDF를 업로드했습니다.

```text
AI.pdf
```

PDF를 읽으면

```text
1 Page

2 Page

3 Page

...

150 Page
```

150개의 페이지가 생성됩니다.

이를 하나씩 변수로 만들지는 않습니다.

```python
page1 = ...
page2 = ...
page3 = ...
```

이렇게 만드는 것은 불가능에 가깝습니다.

대신

```python
pages = [...]
```

하나의 List에 저장합니다.

---

이번에는 OCR을 수행합니다.

```text
Page1 → Text

Page2 → Text

Page3 → Text
```

결과도

```python
texts = [...]
```

List입니다.

---

Embedding도 마찬가지입니다.

```python
vectors = [...]
```

검색 결과도

```python
documents = [...]
```

LLM Message도

```python
messages = [...]
```

결국 AI 서비스는

> **List를 생성하고, 수정하고, 반복하는 프로그램**

이라고 해도 과언이 아닙니다.

---

#### 왜 List가 가장 많이 사용될까?

List는

- 순서가 있고
- 수정할 수 있고
- 반복하기 쉽고
- 데이터를 계속 추가할 수 있기 때문입니다.

예를 들어

```text
사용자 질문
```

처음에는 하나입니다.

```python
questions = [
    "안녕하세요"
]
```

질문이 하나 더 생깁니다.

```python
questions = [
    "안녕하세요",
    "오늘 날씨는?"
]
```

또 하나 생깁니다.

```python
questions = [
    "안녕하세요",
    "오늘 날씨는?",
    "맛집 추천해줘"
]
```

계속 커질 수 있습니다.

이것이 List입니다.

---

#### ② 개념 이해 (Concept)

#### List란?

List는

> **순서가 있는 여러 객체(Object)를 저장하는 Collection**

입니다.

예를 들어

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

메모리에서는

```text
students

↓

List Object

┌─────────────┐
│0 → "Kim"    │
│1 → "Lee"    │
│2 → "Park"   │
└─────────────┘
```

입니다.

여기서 중요한 점은

List 안에는

값(Value)이 아니라

객체(Object)의 참조(Reference)가 저장됩니다.

---

#### Index란?

List에는 위치 번호가 존재합니다.

이를

> **Index**

라고 합니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

```text
Index

0 → Kim

1 → Lee

2 → Park
```

---

#### 왜 0부터 시작할까?

많은 학습자가 궁금해하는 질문입니다.

왜

```text
1

2

3
```

이 아니라

```text
0

1

2
```

일까요?

0 기반 Index는 배열 계열 자료구조에서 시작 위치로부터의
이동 거리(Offset)를 표현하기 편리해 널리 사용되어 온 관례입니다.

첫 번째 요소는 시작 위치에서 0칸, 두 번째 요소는 1칸 떨어져 있다고
표현할 수 있으며 Python도 이 관례를 따릅니다.

이것은 개념을 위한 설명입니다. 실제 CPython List는 객체 자체를
연속으로 저장하기보다 객체를 가리키는 참조를 관리하며,
구체적인 주소 계산은 구현 세부 사항입니다.

---

#### List 생성하기

가장 기본적인 방법입니다.

```python
numbers = [1, 2, 3]
```

문자열도 가능합니다.

```python
names = ["Kim", "Lee", "Park"]
```

혼합도 가능합니다.

```python
data = [
    "Kim",
    30,
    True,
    95.5
]
```

Python은 모든 것이 객체이므로

서로 다른 타입도 함께 저장할 수 있습니다.

---

#### 빈 List 만들기

처음부터 데이터가 있는 것은 아닙니다.

AI에서는

처음에는 비어 있다가

점점 채워지는 경우가 많습니다.

```python
results = []
```

또는

```python
results = list()
```

둘 다 동일합니다.

---

예를 들어

OCR 결과를 저장한다고 하면

```python
ocr_results = []
```

처음에는 아무것도 없습니다.

OCR을 수행하면서

하나씩 추가합니다.

---

#### 요소 접근하기

Index를 이용합니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

첫 번째

```python
students[0]
```

결과

```text
Kim
```

---

두 번째

```python
students[1]
```

결과

```text
Lee
```

---

세 번째

```python
students[2]
```

결과

```text
Park
```

---

#### 음수 Index

Python만의 매우 편리한 기능입니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

```python
students[-1]
```

결과

```text
Park
```

---

```python
students[-2]
```

결과

```text
Lee
```

---

즉

```text
앞에서

0

1

2
```

뒤에서는

```text
-3

-2

-1
```

입니다.

마지막 요소를 자주 사용할 때 매우 편리합니다.

---

#### 요소 수정하기

List는 Mutable입니다.

Unit 5에서 배운 내용입니다.

즉

수정 가능합니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

```python
students[1] = "Hong"
```

결과

```text
Kim

Hong

Park
```

---

메모리에서는

```text
students

↓

List

0 → Kim

1 → Hong

2 → Park
```

기존 참조가 새로운 객체를 가리키도록 변경된 것입니다.

---

#### 요소 추가하기

가장 많이 사용하는 메서드입니다.

```python
students = [
    "Kim",
    "Lee"
]
```

```python
students.append("Park")
```

결과

```text
Kim

Lee

Park
```

append()는

항상

> **맨 뒤에 추가**

합니다.

---

AI에서는

검색 결과를 계속 저장할 때

```python
documents.append(result)
```

처럼 매우 자주 사용합니다.

---

#### 요소 삭제하기

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

```python
students.remove("Lee")
```

결과

```text
Kim

Park
```

---

Index로 삭제할 수도 있습니다.

```python
students.pop(1)
```

결과

```text
Kim

Park
```

---

둘의 차이는

```python
remove()
```

→ 값을 찾아 삭제

```python
pop()
```

→ 위치(Index)를 삭제

입니다.

---

#### List 길이 구하기

```python
students = [
    "Kim",
    "Lee",
    "Park"
]
```

```python
len(students)
```

결과

```text
3
```

AI에서는

```python
len(documents)
```

처럼 검색 결과 개수를 확인할 때 자주 사용합니다.

---

#### 반복문과 함께 사용하기

List는 반복문과 가장 잘 어울립니다.

```python
students = [
    "Kim",
    "Lee",
    "Park"
]

for student in students:
    print(student)
```

결과

```text
Kim
Lee
Park
```

이 방식은 AI 프로젝트의 목록 처리에서 매우 자주 사용합니다.

예를 들어

```python
for page in pages:
    ...
```

```python
for chunk in chunks:
    ...
```

```python
for message in messages:
    ...
```

---

#### AI 서비스에서의 역할 (Architecture)

```text
PDF

↓

List(Page)

↓

for page

↓

OCR

↓

List(Text)

↓

for text

↓

Embedding

↓

List(Vector)

↓

for vector

↓

Vector Search

↓

List(Document)

↓

LLM
```

AI 서비스의 대부분은

> **List를 생성하고 반복하는 과정**

으로 이루어져 있습니다.

---

#### 실무 Best Practice

#### ① 의미 있는 변수명을 사용한다.

좋지 않은 예

```python
a = []
```

좋은 예

```python
documents = []
```

또는

```python
ocr_results = []
```

변수명만 보고도 무엇을 담고 있는지 알 수 있어야 합니다.

---

#### ② 반복문을 적극 활용한다.

좋지 않은 예

```python
print(students[0])
print(students[1])
print(students[2])
```

좋은 예

```python
for student in students:
    print(student)
```

데이터 개수가 늘어나도 코드 수정이 필요 없습니다.

---

#### ③ Index보다 값을 활용할 수 있으면 값을 사용한다.

불필요하게 Index를 직접 다루기보다는

```text
for student in students:
```

와 같이 요소 자체를 사용하는 것이 더 읽기 쉽고 오류도 적습니다.

---

#### 자주 발생하는 실수

##### 1. 존재하지 않는 Index 접근

```python
students = ["Kim", "Lee"]
print(students[2])
```

결과

```text
IndexError
```

List의 길이를 확인하거나 유효한 Index를 사용해야 합니다.

---

##### 2. append()와 =를 혼동

```python
students = ["Kim"]
students = ["Lee"]
```

이는 추가가 아니라 **새로운 List로 교체**한 것입니다.

추가하려면

```python
students.append("Lee")
```

를 사용해야 합니다.

---

##### 3. remove()와 pop()의 차이를 혼동

```python
students.remove("Kim")
```

→ 값을 기준으로 삭제

```python
students.pop(0)
```

→ 위치(Index)를 기준으로 삭제

상황에 맞는 메서드를 선택해야 합니다.

---

동작 결과의 결정적 차이: "반환값(Return Value)"

- **`pop()`은 '삭제된 값을 반환'합니다.**
  - 리스트에서 아이템을 꺼내서 **그 값을 다른 변수에 저장하거나 즉시 사용**할 수 있습니다.
  - _예: `X = my_list.pop(0)` -> 0번 인덱스의 값을 지우면서 `X`에 할당._
- **`remove()`는 반환값이 없습니다 (`None`).**
  - 오직 리스트에서 해당 값을 **지우는 행위(Side Effect)**만 수행합니다. 지워진 값을 돌려주지 않습니다.
  - _예: `my_list.remove("apple")` -> 리스트에서 "apple"을 지우고 끝._

2. 🏗️ 설계 목적의 차이: 자료구조의 구현

두 메서드는 컴퓨터 과학에서 사용하는 서로 다른 **자료구조의 행동 양식**을 지원하기 위해 분리되었습니다.

- **`pop()`은 '스택(Stack)'과 '큐(Queue)'를 위해 존재합니다.**
  - 데이터를 쌓아두고 **"맨 뒤나 맨 앞의 원소를 꺼내서(Pop) 확인하고 처리한다"**는 개념을 구현할 때 필수적입니다. 매개변수를 넣지 않으면 기본값으로 가장 마지막 인덱스(`-1`)를 꺼내는 이유도 스택(LIFO) 구조를 쉽게 쓰기 위함입니다.
- **`remove()`는 '집합(Set)'이나 일반적인 '리스트 관리'를 위해 존재합니다.**
  - 데이터가 어디에 위치해 있는지(인덱스)는 상관없고, **"이 목록에서 특정 항목(값)을 제거해라"**라는 비즈니스 로직을 수행할 때 사용합니다.

3. ⚠️ 중복 데이터 처리와 예외 발생의 차이

| 특성                | `pop(index)`                                        | `remove(value)`                                                                   |
| ------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------- |
| **중복 데이터**     | 지정한 인덱스의 데이터 **딱 1개만** 정확히 삭제함.  | 리스트에 같은 값이 여러 개 있다면, **가장 앞쪽(첫 번째)에 있는 값 1개만** 삭제함. |
| **에러(Exception)** | 범위를 벗어난 인덱스 지정 시 **`IndexError`** 발생. | 리스트에 존재하지 않는 값을 지우려고 하면 **`ValueError`** 발생.                  |

💡 한 줄 요약

- **값의 위치를 알고, 그 값을 꺼내서 써야 한다** ➡️ `pop()`
- **값의 위치는 모르고, 특정 값 자체를 삭제하는 게 목적이다** ➡️ `remove()`

---

#### 핵심 내용 정리

이번 Unit에서는 Python에서 가장 많이 사용하는 Collection인 **List**를 학습했습니다.

핵심은 다음과 같습니다.

- List는 **순서가 있는 여러 객체를 저장하는 Mutable Collection**이다.
- 각 요소는 **Index(0부터 시작)** 를 통해 접근한다.
- 음수 Index를 사용하면 뒤에서부터 요소에 접근할 수 있다.
- `append()`는 요소를 추가하고, `remove()`와 `pop()`은 각각 값과 위치를 기준으로 요소를 삭제한다.
- `len()`으로 요소 개수를 확인하고, `for` 반복문과 함께 사용하면 대량의 데이터를 효율적으로 처리할 수 있다.
- AI 서비스에서는 PDF 페이지, OCR 결과, 임베딩 벡터, 검색 결과, 대화 메시지 등 거의 모든 데이터 흐름이 List를 기반으로 이루어진다.

---

### Module 03. List Comprehension - Python다운 반복문

#### Module 실습 예제

- [예제 1: comprehension_basics.py](examples/module_03/comprehension_basics.py) — List Comprehension의 변환과 필터링을 확인합니다.
- [예제 2: filter_documents.py](examples/module_03/filter_documents.py) — 문서 검색 결과를 필터링하고 응답 형태로 변환합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- List Comprehension은 왜 등장했는가?
- 일반 반복문과 어떤 차이가 있는가?
- 언제 사용하는 것이 좋은가?
- AI 프로젝트에서는 어떤 상황에서 사용하는가?
- 언제 사용하지 않는 것이 더 좋은가?

---

#### ① 문제 이해 (Why)

지난 Unit까지 우리는 List를 만들고, 수정하고, 반복하는 방법을 배웠습니다.

예를 들어 숫자를 제곱한 새로운 List를 만들고 싶다면 다음과 같이 작성했습니다.

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

결과

```text
[1, 4, 9, 16, 25]
```

동작에는 아무 문제가 없습니다.

하지만 Python 개발자들은 이런 생각을 했습니다.

> **"이 패턴을 너무 많이 작성하는데 더 간단하게 표현할 수 없을까?"**

왜냐하면

새로운 List를 만드는 작업이 너무 자주 등장했기 때문입니다.

---

예를 들어

OCR 결과를 모두 소문자로 변환한다.

```python
results = []

for text in ocr_results:
    results.append(text.lower())
```

Embedding 길이를 계산한다.

```python
lengths = []

for vector in vectors:
    lengths.append(len(vector))
```

파일 이름만 추출한다.

```python
names = []

for file in files:
    names.append(file.name)
```

이런 코드가 프로젝트 곳곳에 반복됩니다.

Python은 이를 위해

> **List Comprehension**

이라는 문법을 제공합니다.

---

#### 왜 중요한가?

AI 프로젝트는 대부분

```text
데이터 읽기

↓

변환

↓

저장

↓

변환

↓

저장
```

의 반복입니다.

즉,

**"기존 List를 새로운 List로 변환하는 작업"**

이 매우 많습니다.

List Comprehension은 바로 이 작업을 가장 효율적으로 표현하는 문법입니다.

---

#### ② 개념 이해 (Concept)

#### List Comprehension이란?

List Comprehension은

> **기존 Collection을 이용하여 새로운 List를 만드는 표현식(Expression)**

입니다.

가장 중요한 점은

> **반복문을 대체하는 것이 아니라**
>
> **새로운 List를 생성하기 위한 문법**이라는 것입니다.

이 차이를 반드시 기억해야 합니다.

---

#### 기본 문법

일반 반복문

```python
result = []

for item in items:
    result.append(item)
```

List Comprehension

```python
result = [
    item
    for item in items
]
```

동일한 결과를 만듭니다.

---

#### 구조 이해

문법을 보면

```python
[
    표현식
    for 변수 in Collection
]
```

입니다.

순서를 보면

```text
① 무엇을 저장할 것인가?

↓

② 어디서 가져올 것인가?
```

입니다.

처음에는 조금 어색하지만

익숙해지면 매우 자연스럽습니다.

---

#### 가장 기본적인 예제

```python
numbers = [1, 2, 3, 4, 5]

result = [
    number
    for number in numbers
]

print(result)
```

결과

```text
[1, 2, 3, 4, 5]
```

그대로 복사한 것입니다.

---

이번에는 제곱합니다.

```python
numbers = [1, 2, 3, 4, 5]

result = [
    number ** 2
    for number in numbers
]

print(result)
```

결과

```text
[1, 4, 9, 16, 25]
```

---

메모리에서 일어나는 일은

```text
numbers

↓

1

↓

1²

↓

result
```

```text
2

↓

2²

↓

result
```

```text
3

↓

3²

↓

result
```

반복이 끝날 때까지 계속됩니다.

---

#### 문자열 변환

```python
names = [
    "Kim",
    "Lee",
    "Park"
]

result = [
    name.upper()
    for name in names
]

print(result)
```

결과

```text
['KIM', 'LEE', 'PARK']
```

---

#### 조건 추가하기

조건도 넣을 수 있습니다.

기존 방식

```python
result = []

for number in numbers:

    if number % 2 == 0:
        result.append(number)
```

List Comprehension

```python
result = [
    number
    for number in numbers
    if number % 2 == 0
]
```

결과

```text
[2,4]
```

---

구조는

```text
표현식

↓

for

↓

if
```

입니다.

---

#### 조건 + 변환

짝수만 제곱합니다.

```python
numbers = [1,2,3,4,5]

result = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]
```

결과

```text
[4,16]
```

---

#### 일반 반복문과 비교

기존 코드

```python
result = []

for number in numbers:

    if number > 10:
        result.append(number * 2)
```

List Comprehension

```python
result = [
    number * 2
    for number in numbers
    if number > 10
]
```

기능은 같습니다.

하지만 훨씬 간결합니다.

---

#### AI 프로젝트에서는 어떻게 사용할까?

#### OCR 결과 정리

```python
clean_texts = [
    text.strip()
    for text in ocr_results
]
```

모든 문자열의 앞뒤 공백을 제거합니다.

---

#### PDF 페이지 번호 생성

```python
pages = [
    page.number
    for page in pdf.pages
]
```

페이지 번호만 추출합니다.

---

#### 파일 이름 추출

```python
file_names = [
    file.name
    for file in files
]
```

---

#### Embedding 길이 확인

```python
dimensions = [
    len(vector)
    for vector in embeddings
]
```

---

#### 빈 문자열 제거

```python
texts = [
    text
    for text in texts
    if text != ""
]
```

---

#### 긴 문장만 선택

```python
documents = [
    doc
    for doc in documents
    if len(doc) > 100
]
```

실제 RAG 전처리 과정에서 자주 사용하는 패턴입니다.

---

#### List Comprehension의 장점

#### ① 코드가 짧다.

기존

```python
result = []

for item in items:
    result.append(...)
```

↓

```python
result = [
    ...
    for item in items
]
```

---

#### ② 새로운 List를 만든다는 의도가 명확하다.

코드를 읽는 사람도

> "아, 이건 기존 데이터를 변환해서 새로운 List를 만드는구나."

를 바로 이해할 수 있습니다.

---

#### ③ Python다운 코드

Python 공식 문서와 대부분의 오픈소스 프로젝트에서는

List Comprehension을 매우 많이 사용합니다.

---

#### 언제 사용하지 않는 것이 좋을까?

이 부분이 매우 중요합니다.

많은 학습자는

> "List Comprehension이 더 멋져 보인다."

고 생각하여 모든 반복문을 바꾸려고 합니다.

하지만 좋은 개발자는

**가독성**을 더 중요하게 생각합니다.

---

예를 들어

이런 코드는 좋습니다.

```python
[
    text.strip()
    for text in texts
]
```

한눈에 이해됩니다.

---

하지만

```python
[
    process(text)
    for text in texts
    if validate(text)
]
```

여기까지는 괜찮습니다.

---

그러나

```python
[
    process(text)
    for text in texts
    if validate(text)
    if check(text)
    if verify(text)
]
```

처럼 조건이 여러 개 붙기 시작하면

읽기 어려워집니다.

이 경우에는

일반 반복문이 더 좋은 선택입니다.

---

#### 실무 Best Practice

#### ① 단순한 변환만 사용한다.

좋은 예

```python
[
    text.lower()
    for text in texts
]
```

---

#### ② 필터링도 적당한 수준까지만 사용한다.

좋은 예

```python
[
    doc
    for doc in docs
    if len(doc) > 100
]
```

---

#### ③ 복잡한 로직은 반복문을 사용한다.

좋은 예

```python
result = []

for doc in docs:

    if validate(doc):

        processed = process(doc)

        result.append(processed)
```

이렇게 작성하는 것이 훨씬 읽기 쉽습니다.

---

#### 자주 발생하는 실수ollama pull bge-m3

#### 1. append()를 같이 사용하는 경우

잘못된 예

```python
result = [
    result.append(x)
    for x in numbers
]
```

List Comprehension 자체가 새로운 List를 생성합니다.

append()는 사용할 필요가 없습니다.

---

#### 2. 너무 복잡하게 작성

```text
[
    ...
    if ...
    if ...
    if ...
]
```

읽기 어렵다면

반복문으로 바꾸는 것이 맞습니다.

---

#### 3. 단순 반복도 List Comprehension으로 작성

예를 들어

```python
[
    print(x)
    for x in numbers
]
```

이렇게 사용하는 것은 좋지 않습니다.

List를 만들 목적이 아니므로

```python
for x in numbers:
    print(x)
```

가 올바른 코드입니다.

List Comprehension은 **새로운 List를 생성할 때** 사용하는 문법입니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
OCR 결과(List)

↓

List Comprehension

↓

공백 제거

↓

소문자 변환

↓

빈 문자열 제거

↓

정제된 Text(List)

↓

Embedding
```

또는

```text
검색 결과(List)

↓

List Comprehension

↓

필요한 필드만 추출

↓

LLM 입력 생성
```

AI 파이프라인에서는 데이터를 다음 단계에 맞게 **변환(Transformation)** 하는 작업이 매우 많으며, List Comprehension은 이를 간결하고 명확하게 표현하는 데 적합합니다.

---

#### 핵심 내용 정리

이번 Unit에서는 **List Comprehension**을 학습했습니다.

핵심은 다음과 같습니다.

- List Comprehension은 **기존 Collection을 이용해 새로운 List를 만드는 Python의 표현식**이다.
- `표현식 → for → if` 순서로 작성하며, 변환과 필터링을 한 번에 수행할 수 있다.
- 단순한 데이터 변환에서는 일반 반복문보다 코드가 짧고 의도가 명확하다.
- AI 프로젝트에서는 OCR 결과 정제, 파일명 추출, 문서 필터링, 임베딩 전처리 등에서 매우 자주 사용된다.
- 하지만 조건이 복잡하거나 여러 단계의 처리가 필요한 경우에는 일반 `for` 반복문이 더 읽기 쉽고 유지보수하기 좋다.

---

### Module 04. Dictionary - AI 서비스에서 가장 많이 사용하는 자료구조

#### Module 실습 예제

- [예제 1: dictionary_basics.py](examples/module_04/dictionary_basics.py) — Dictionary의 생성·조회·수정과 안전한 조회를 연습합니다.
- [예제 2: api_payload.py](examples/module_04/api_payload.py) — JSON 요청에 대응하는 Dictionary를 구성합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Dictionary는 왜 등장했는가?
- List와 Dictionary의 차이는 무엇인가?
- Key와 Value는 무엇인가?
- Dictionary는 내부적으로 어떻게 동작하는가?
- AI 프로젝트에서는 왜 Dictionary를 가장 많이 사용하는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 List를 사용해 데이터를 저장했습니다.

예를 들어 학생 정보를 저장한다고 해봅시다.

```python
student = [
    "Kim",
    20,
    "Computer Engineering"
]
```

이 데이터를 보면 다음과 같습니다.

```text
Index    Value

0        Kim
1        20
2        Computer Engineering
```

---

그런데 한 가지 문제가 있습니다.

학생의 나이를 가져오고 싶다면

```python
student[1]
```

이라고 작성해야 합니다.

그런데

**1이 무엇을 의미하는지 기억해야 합니다.**

---

이번에는 조금 더 복잡한 데이터를 생각해봅시다.

```python
employee = [
    "Kim",
    32,
    "AI Team",
    "Manager",
    5000
]
```

여기서

```python
employee[3]
```

이 무엇일까요?

잠시 코드를 떠나 생각해 보면,

3이 직급인지,

부서인지,

연봉인지

코드만 보고는 알 수 없습니다.

---

실제 AI 서비스에서는 이런 문제가 훨씬 심각합니다.

예를 들어 사용자 정보입니다.

```text
이름

나이

이메일

가입일

권한

마지막 로그인
```

이 데이터를 List에 저장하면

```python
user = [
    "Kim",
    30,
    "kim@test.com",
    "2026-01-01",
    "Admin",
    "2026-07-08"
]
```

6개의 Index를 모두 기억해야 합니다.

현실적으로 불가능합니다.

---

그래서 개발자들은 생각했습니다.

> **"위치(Index)가 아니라 이름으로 데이터를 찾으면 어떨까?"**

바로 이것이 Dictionary입니다.

---

#### Dictionary가 해결한 문제

List

```text
0 → Kim

1 → 30

2 → kim@test.com
```

↓

Dictionary

```text
"name"

↓

Kim
```

```text
"age"

↓

30
```

```text
"email"

↓

kim@test.com
```

이렇게 이름으로 접근할 수 있습니다.

---

#### AI 서비스에서는?

AI 서비스에서 사용하는 데이터는 대부분

"속성(Property)"

으로 이루어져 있습니다.

예를 들어

OCR 결과

```text
text

confidence

bounding_box
```

사용자 정보

```text
id

name

email
```

LLM 응답

```text
role

content
```

Embedding 정보

```text
vector

metadata
```

모두

**이름이 있는 데이터**

입니다.

따라서 Dictionary가 가장 적합합니다.

---

#### ② 개념 이해 (Concept)

#### Dictionary란?

Dictionary는

> **Key와 Value의 쌍(Pair)으로 데이터를 저장하는 Collection**

입니다.

예를 들어

```python
student = {
    "name": "Kim",
    "age": 20,
    "major": "Computer Engineering"
}
```

입니다.

---

메모리에서는

```text
student

↓

Dictionary Object

"name"

↓

Kim


"age"

↓

20


"major"

↓

Computer Engineering
```

입니다.

---

#### Key와 Value

Dictionary는 항상

```text
Key

↓

Value
```

구조입니다.

예를 들어

```python
student = {
    "name": "Kim",
    "age": 20
}
```

여기서

```text
Key

"name"

"age"
```

입니다.

---

Value는

```text
Kim

20
```

입니다.

---

즉

Dictionary는

> **이름(Key)으로 데이터를 찾는 Collection**

입니다.

---

#### Dictionary 생성하기

```python
student = {
    "name": "Kim",
    "age": 20,
    "major": "Computer Engineering"
}
```

---

빈 Dictionary

```python
student = {}
```

또는

```python
student = dict()
```

---

#### 값 가져오기

List는

```python
students[0]
```

처럼 Index를 사용했습니다.

Dictionary는

```python
student["name"]
```

결과

```text
Kim
```

---

```python
student["age"]
```

결과

```text
20
```

---

Index가 아니라

Key를 사용한다는 것이 핵심입니다.

---

#### 값 수정

```python
student["age"] = 21
```

결과

```text
age

20

↓

21
```

---

#### 새로운 값 추가

Dictionary는

없는 Key를 넣으면

자동으로 추가됩니다.

```python
student["email"] = "kim@test.com"
```

결과

```text
name

age

major

email
```

---

#### 값 삭제

```python
del student["major"]
```

또는

```python
student.pop("major")
```

둘 다 가능합니다.

---

#### 존재 여부 확인

```python
"name" in student
```

결과

```text
True
```

---

없는 경우

```python
"phone" in student
```

결과

```text
False
```

---

#### get() 메서드

Dictionary에서

가장 많이 사용하는 메서드입니다.

예를 들어

```python
student["phone"]
```

phone이 없으면

오류가 발생합니다.

```text
KeyError
```

---

하지만

```python
student.get("phone")
```

결과

```text
None
```

입니다.

오류가 발생하지 않습니다.

---

기본값도 줄 수 있습니다.

```python
student.get("phone", "없음")
```

결과

```text
없음
```

`get()`은 Key가 없어도 괜찮은 **선택 필드**를 조회할 때 유용합니다.

반대로 반드시 있어야 하는 필드는 `student["name"]`처럼 조회하여,
누락되었을 때 `KeyError`로 문제를 즉시 발견하는 편이 안전할 수 있습니다.

---

#### Dictionary 반복

```python
student = {
    "name": "Kim",
    "age": 20
}
```

기본 반복

```python
for key in student:
    print(key)
```

결과

```text
name

age
```

---

Value도 가져오기

```python
for key in student:
    print(student[key])
```

---

더 좋은 방법

```python
for key, value in student.items():
    print(key, value)
```

결과

```text
name Kim

age 20
```

---

#### 주요 메서드

#### keys()

```python
student.keys()
```

결과

```text
name

age

major
```

---

#### values()

```python
student.values()
```

결과

```text
Kim

20

Computer Engineering
```

---

#### items()

```python
student.items()
```

결과

```text
(name, Kim)

(age, 20)

(major, Computer Engineering)
```

`items()`는 **(Key, Value)** 형태의 Tuple을 반환합니다.

---

#### Dictionary 내부 구조

Dictionary도 Set과 마찬가지로

**Hash 기반 자료구조**를 사용합니다.

예를 들어

```python
student["name"]
```

을 실행하면

Python은

```text
Hash("name")

↓

메모리 위치 계산

↓

바로 접근
```

합니다.

즉,

List처럼

```text
0

1

2

3
```

하나씩 찾지 않습니다.

그래서 매우 빠릅니다.

---

#### AI 프로젝트에서는 어떻게 사용할까?

#### 사용자 정보

```python
user = {
    "id": 1,
    "name": "Kim",
    "email": "kim@test.com"
}
```

---

#### OCR 결과

```python
ocr = {
    "text": "OpenAI",
    "confidence": 0.98
}
```

---

#### Embedding 정보

```python
embedding = {
    "vector": [...],
    "dimension": 1536
}
```

---

#### LLM Message

```python
message = {
    "role": "user",
    "content": "안녕하세요."
}
```

여기서 많은 분들이 눈치챌 것입니다.

이 구조는 어디서 많이 봤습니다.

---

OpenAI API의 Message도

```python
{
    "role": "...",
    "content": "..."
}
```

입니다.

즉,

Dictionary입니다.

---

JSON도

```json
{
  "name": "Kim",
  "age": 20
}
```

입니다.

JSON Object는 Python에서 읽으면 일반적으로 Dictionary로 표현됩니다.

앞서 Unit 15에서 배운 **JSON**과 Dictionary가 자연스럽게 연결되는 이유입니다.

---

#### List와 Dictionary 비교

| 항목           | List                | Dictionary         |
| -------------- | ------------------- | ------------------ |
| 검색 기준      | Index               | Key                |
| 순서 기반 접근 | O                   | X (이름 기반 접근) |
| 가독성         | 낮음(복잡한 데이터) | 높음               |
| 실무 활용      | 연속 데이터         | 속성 데이터        |

> **참고:** Python 3.7부터는 Dictionary가 **삽입 순서(Insertion Order)** 를 유지합니다. 하지만 Dictionary의 핵심 목적은 **순서를 이용한 접근이 아니라 Key를 이용한 접근**입니다.

---

#### 언제 Dictionary를 사용할까?

데이터에 **의미 있는 이름**이 있다면 Dictionary가 적합합니다.

예를 들어

```python
student = {
    "name": "Kim",
    "age": 20
}
```

---

LLM Message

```python
{
    "role": "assistant",
    "content": "안녕하세요."
}
```

---

OCR 결과

```python
{
    "text": "...",
    "confidence": 0.95
}
```

---

#### 실무 Best Practice

#### ① Index보다 Key를 선호한다.

좋지 않은 예

```python
user[2]
```

좋은 예

```python
user["email"]
```

코드의 의미가 훨씬 명확합니다.

---

#### ② 필수 Key와 선택 Key를 구분한다.

선택 필드는 없을 수 있으므로 `get()`과 기본값을 활용합니다.

```python
nickname = user.get("nickname", "이름 없음")
```

필수 필드는 대괄호로 조회하여 누락을 조기에 발견합니다.

```python
email = user["email"]
```

외부 API나 사용자 입력처럼 신뢰할 수 없는 데이터는 Dictionary 접근만으로
검증을 끝내지 말고, 이후 FastAPI 과정에서 배울 Pydantic Schema처럼
필드의 필수 여부와 타입을 명시하는 검증 도구를 사용하는 것이 좋습니다.

---

#### ③ 관련 데이터를 하나의 Dictionary로 묶는다.

좋지 않은 예

```python
name = "Kim"
age = 20
email = "kim@test.com"
```

좋은 예

```python
user = {
    "name": "Kim",
    "age": 20,
    "email": "kim@test.com"
}
```

관련 정보가 하나의 객체로 관리되어 유지보수가 쉬워집니다.

---

#### 자주 발생하는 실수

#### Dictionary Key의 조건

Dictionary의 Key는 값을 저장한 뒤에도 Hash 값이 안정적으로 유지되는
**Hashable 객체**여야 합니다.

문자열, 숫자, 그리고 Hashable한 값만 담은 Tuple은 Key로 사용할 수 있습니다.

```python
data = {
    "name": "Kim",
    1: "first",
    (10, 20): "coordinate",
}
```

반면 변경 가능한 `list`, `dict`, `set`은 Key로 사용할 수 없습니다.

```python
data = {
    [10, 20]: "coordinate"
}
```

이 코드는 `TypeError: unhashable type: 'list'`를 발생시킵니다.

---

#### 1. 없는 Key에 접근

```python
student["phone"]
```

Key가 없으면 `KeyError`가 발생합니다.

선택 필드라면 `get()`이나 `in`을 사용하고, 필수 필드라면 이 오류를
무조건 숨기기보다 데이터 누락을 조기에 발견하고 처리해야 합니다.

---

#### 2. Key와 Value를 혼동

```python
student["Kim"]
```

여기서 `"Kim"`은 Value이지 Key가 아닙니다.

올바른 접근은

```python
student["name"]
```

입니다.

---

#### 3. 중복 Key 사용

```python
student = {
    "name": "Kim",
    "name": "Lee"
}
```

Dictionary에서 Key는 **중복될 수 없습니다.**

결과적으로 `"Lee"`만 남고 `"Kim"`은 덮어써집니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
사용자 요청

↓

Dictionary(JSON)

↓

FastAPI

↓

Dictionary

↓

LLM API

↓

Dictionary(JSON)

↓

응답
```

또는

```text
OCR

↓

Dictionary

(text,
confidence,
bbox)

↓

RAG

↓

Dictionary

↓

LLM
```

많은 Web 기반 AI 서비스에서 요청·응답 데이터는 JSON으로 이동하고,
Python 내부에서는 Dictionary 등으로 변환해 처리합니다. 따라서 Dictionary를
이해하면 AI 서비스의 주요 데이터 흐름을 읽는 데 도움이 됩니다.

---

#### 핵심 내용 정리

이번 Unit에서는 **Dictionary**를 학습했습니다.

핵심은 다음과 같습니다.

- Dictionary는 **Key와 Value의 쌍으로 데이터를 저장하는 Collection**이다.
- List가 Index로 데이터를 찾는다면, Dictionary는 **Key(이름)** 로 데이터를 찾는다.
- `get()`은 없어도 되는 선택 Key를 조회할 때 유용하며, 필수 Key는 대괄호 접근이나 Schema 검증으로 누락을 명확히 처리한다.
- 내부적으로 Hash 기반 구조를 사용하므로 Key를 통한 조회 속도가 매우 빠르다.
- AI 프로젝트에서는 사용자 정보, OCR 결과, API 요청·응답, LLM Message처럼 이름이 있는 속성 데이터를 Dictionary로 표현하는 경우가 많다.

---

### Module 05. Collection 활용 패턴 - 중첩 자료구조(Nested Data Structure)

#### Module 실습 예제

- [예제 1: nested_access.py](examples/module_05/nested_access.py) — 중첩 Dictionary와 List의 데이터에 접근합니다.
- [예제 2: group_documents.py](examples/module_05/group_documents.py) — 문서를 상태별로 그룹화하는 활용 패턴을 연습합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Collection은 실제 프로젝트에서 어떻게 사용하는가?
- List 안에 Dictionary를 넣는 이유는 무엇인가?
- Dictionary 안에 List를 넣는 이유는 무엇인가?
- 중첩 자료구조(Nested Data Structure)는 왜 중요한가?
- AI 서비스에서는 어떤 형태의 데이터가 오고 가는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 각각의 Collection을 따로 배웠습니다.

- List
- Tuple
- Set
- Dictionary

하지만 실제 프로젝트에서는

이들을 따로 사용하는 경우는 거의 없습니다.

거의 항상

**여러 Collection을 조합해서 사용합니다.**

---

예를 들어

학생 여러 명을 저장한다고 해봅시다.

학생 한 명은

```text
이름

나이

학과
```

를 가집니다.

그러면

List일까요?

Dictionary일까요?

둘 다 아닙니다.

학생 한 명은

```python
{
    "name": "Kim",
    "age": 20,
    "major": "AI"
}
```

Dictionary입니다.

---

학생이 여러 명이라면?

```text
학생

학생

학생

학생
```

여러 개입니다.

그러므로

```text
List

↓

Dictionary

↓

학생 정보
```

가 됩니다.

즉

```python
students = [
    {
        "name": "Kim",
        "age": 20
    },
    {
        "name": "Lee",
        "age": 21
    }
]
```

이 됩니다.

---

이것이

실제 프로그램에서 가장 많이 사용하는 형태입니다.

---

#### AI 프로젝트에서는?

LLM Message를 생각해봅시다.

OpenAI API는

Message를 하나만 보내지 않습니다.

여러 개를 보냅니다.

```text
Message

Message

Message
```

각 Message는

```text
role

content
```

를 가집니다.

즉

Message 하나는

Dictionary입니다.

여러 개의 Message는

List입니다.

결국

```python
messages = [
    {
        "role": "system",
        "content": "..."
    },
    {
        "role": "user",
        "content": "..."
    }
]
```

가 됩니다.

이 구조는 앞으로 FastAPI와 OpenAI API를 배울 때 자주 보게 됩니다.

---

#### ② 개념 이해 (Concept)

#### 중첩 자료구조(Nested Data Structure)

Nested Data Structure란

> **Collection 안에 다른 Collection이 들어 있는 구조**

입니다.

예를 들어

```python
[
    [1,2],
    [3,4]
]
```

입니다.

List 안에 List가 있습니다.

---

또는

```python
{
    "scores": [
        90,
        80,
        70
    ]
}
```

Dictionary 안에 List가 있습니다.

---

또는

```python
[
    {
        "name":"Kim"
    }
]
```

List 안에 Dictionary가 있습니다.

---

Collection은

서로 자유롭게 포함할 수 있습니다.

---

#### 가장 많이 사용하는 구조

#### ① List of Dictionary

가장 많이 사용합니다.

```python
users = [
    {
        "id":1,
        "name":"Kim"
    },
    {
        "id":2,
        "name":"Lee"
    }
]
```

구조

```text
List

│

├── Dictionary(User1)

└── Dictionary(User2)
```

---

왜 사용할까요?

사용자가 여러 명이기 때문입니다.

---

AI 프로젝트에서는

```python
documents = [
    {
        "title":"AI",
        "score":0.95
    },
    {
        "title":"Python",
        "score":0.91
    }
]
```

검색 결과도

거의 이 형태입니다.

---

#### ② Dictionary of List

이번에는 반대입니다.

```python
student = {
    "name":"Kim",
    "scores":[
        95,
        88,
        91
    ]
}
```

구조

```text
Dictionary

│

"name"

↓

Kim


"scores"

↓

List

95

88

91
```

---

왜 사용할까요?

학생은 한 명인데

점수는 여러 개이기 때문입니다.

---

AI 프로젝트에서는

```python
embedding = {
    "text":"AI",
    "vector":[
        0.15,
        0.82,
        0.33
    ]
}
```

처럼 사용합니다.

---

#### ③ Dictionary 안에 Dictionary

```python
user = {

    "profile":{

        "name":"Kim",

        "age":20

    },

    "setting":{

        "theme":"dark"

    }

}
```

구조

```text
User

│

├── profile

│      │

│      ├── name

│      └── age

│

└── setting

       │

       └── theme
```

---

설정을 그룹으로 묶을 때 자주 사용합니다.

---

#### ④ List 안에 List

```python
matrix = [

    [1,2,3],

    [4,5,6]

]
```

AI에서는

이미지

행렬(Matrix)

Tensor의 기초 개념을 이해할 때 중요합니다.

---

#### 데이터 접근하기

예를 들어

```python
students = [

    {

        "name":"Kim",

        "age":20

    },

    {

        "name":"Lee",

        "age":21

    }

]
```

Kim 이름

```python
students[0]["name"]
```

결과

```text
Kim
```

---

Lee 나이

```python
students[1]["age"]
```

결과

```text
21
```

---

접근 순서를 보면

```text
List

↓

Dictionary

↓

Value
```

입니다.

---

#### Dictionary 안의 List 접근

```python
student = {

    "scores":[

        95,

        88,

        91

    ]

}
```

첫 번째 점수

```python
student["scores"][0]
```

결과

```text
95
```

---

접근 순서는

```text
Dictionary

↓

List

↓

Value
```

입니다.

---

#### 반복문 사용

List of Dictionary

```python
users = [

    {

        "name":"Kim"

    },

    {

        "name":"Lee"

    }

]
```

반복

```python
for user in users:

    print(user["name"])
```

결과

```text
Kim

Lee
```

이 패턴은

실무에서 매우 자주 사용합니다.

---

#### AI 프로젝트에서는 어떻게 사용할까?

#### OpenAI Message

```python
messages = [

    {

        "role":"system",

        "content":"You are helpful."

    },

    {

        "role":"user",

        "content":"안녕하세요."

    }

]
```

구조

```text
List

↓

Dictionary

↓

role

content
```

---

#### OCR 결과

```python
ocr_results = [

    {

        "text":"Hello",

        "confidence":0.98

    },

    {

        "text":"World",

        "confidence":0.96

    }

]
```

---

#### 검색 결과

```python
documents = [

    {

        "title":"Python",

        "score":0.91

    },

    {

        "title":"AI",

        "score":0.95

    }

]
```

---

#### Embedding

```python
embedding = {

    "text":"OpenAI",

    "vector":[

        0.15,

        0.81,

        0.22

    ]

}
```

---

#### 사용자 정보

```python
user = {

    "profile":{

        "name":"Kim",

        "age":20

    },

    "history":[

        "Hello",

        "Python"

    ]

}
```

실제 서비스는

거의 이런 구조입니다.

---

#### Collection 선택 기준

실무에서는 먼저 다음 질문을 합니다.

#### 하나인가? 여러 개인가?

하나

↓

Dictionary

여러 개

↓

List

---

#### 속성이 있는가?

있다

↓

Dictionary

없다

↓

List

---

#### 순서가 중요한가?

중요하다

↓

List

---

중복 제거가 필요한가?

↓

Set

---

변경하면 안 되는가?

↓

Tuple

---

이 네 가지 질문만 해도 대부분의 Collection을 선택할 수 있습니다.

---

#### 실무 Best Practice

#### ① 현실 세계를 그대로 모델링한다.

예를 들어

학생이 여러 명이라면

```text
학생들

↓

List
```

학생 한 명은

```text
학생

↓

Dictionary
```

이 자연스럽습니다.

---

#### ② 의미 있는 그룹을 Dictionary로 묶는다.

좋지 않은 예

```python
name = "Kim"

age = 20

email = "..."
```

좋은 예

```python
user = {

    "name":"Kim",

    "age":20,

    "email":"..."
}
```

---

#### ③ 반복 대상은 List로 만든다.

예를 들어

OCR 결과는

여러 개입니다.

```python
ocr_results = [
    {...},
    {...},
    {...}
]
```

반복하기 쉽습니다.

---

#### 자주 발생하는 실수

#### 1. List와 Dictionary의 역할을 반대로 설계

잘못된 예

```python
students = {

    "Kim":20,

    "Lee":21
}
```

학생이 계속 추가되고 다양한 속성을 가져야 한다면 확장성이 떨어집니다.

다음과 같이 표현하는 것이 더 자연스럽습니다.

```python
students = [
    {
        "name": "Kim",
        "age": 20
    },
    {
        "name": "Lee",
        "age": 21
    }
]
```

---

#### 2. 중첩 접근 순서를 혼동

```python
students["name"]
```

`students`는 List인데 Dictionary처럼 접근하면 오류가 발생합니다.

올바른 접근은

```python
students[0]["name"]
```

입니다.

---

#### 3. 데이터 구조를 먼저 이해하지 않고 코드 작성

실무에서는 코드를 작성하기 전에 먼저 다음과 같이 구조를 그려보는 것이 좋습니다.

```text
Users (List)

│

├── User (Dictionary)

│      ├── name

│      ├── age

│      └── email

│

└── User (Dictionary)

       ├── name

       ├── age

       └── email
```

이 과정을 거치면 코드 작성이 훨씬 쉬워집니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
사용자 요청(JSON)

        │

        ▼

Dictionary

        │

        ▼

Messages(List)

        │

        ▼

Message(Dictionary)

        │

        ├── role

        └── content

        │

        ▼

LLM
```

또는

```text
검색 결과(List)

        │

        ▼

Document(Dictionary)

        │

        ├── title

        ├── score

        └── content

        │

        ▼

RAG

        │

        ▼

LLM
```

여기서 알 수 있는 중요한 사실이 있습니다.

> **AI 서비스는 단순히 Collection을 사용하는 것이 아니라, Collection을 계층적으로 조합한 중첩 자료구조를 다루는 프로그램입니다.**

---

#### 핵심 내용 정리

이번 Unit에서는 **Collection 활용 패턴과 중첩 자료구조(Nested Data Structure)**를 학습했습니다.

핵심은 다음과 같습니다.

- 실제 프로젝트에서는 하나의 Collection만 사용하는 경우보다 **여러 Collection을 조합**하여 사용하는 경우가 대부분이다.
- 가장 많이 사용되는 구조는 **List of Dictionary**와 **Dictionary of List**이다.
- 데이터에 접근할 때는 자료구조의 계층을 따라 접근해야 한다. (`students[0]["name"]`)
- AI 서비스의 요청(Request), 응답(Response), OCR 결과, 검색 결과, LLM Message 등은 대부분 중첩 자료구조로 표현된다.
- 코드를 작성하기 전에 **현실 세계의 데이터를 자료구조로 모델링**하는 습관이 중요하다.

---

## Part 2-2. 함수를 확장하는 Decorator

### Module 06. Decorator - 함수를 수정하지 않고 기능을 추가하는 방법

#### Module 실습 예제

- [예제 1: decorator_timing.py](examples/module_06/decorator_timing.py) — Decorator로 함수 실행 시간을 측정합니다.
- [예제 2: route_decorator_model.py](examples/module_06/route_decorator_model.py) — 간단한 Route Registry로 @ 문법의 원리를 확인합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Decorator는 왜 등장했는가?
- Decorator는 어떤 문제를 해결하는가?
- 함수 객체와 Decorator는 어떤 관계가 있는가?
- `@` 문법은 실제로 무엇을 의미하는가?
- FastAPI에서는 왜 Decorator를 사용하는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 함수를 만들었습니다.

예를 들어

```python
def login(user):
    print(f"{user} 로그인")
```

잘 동작합니다.

---

그런데 어느 날 새로운 요구사항이 생겼습니다.

로그인할 때마다

- 실행 시간을 측정하고 싶다.
- 로그를 남기고 싶다.
- 권한을 확인하고 싶다.
- 예외를 처리하고 싶다.

기존 함수는

```python
def login(user):
    print("로그 시작")
    print(f"{user} 로그인")
    print("로그 종료")
```

---

이번에는

회원가입 함수도 있습니다.

```python
def register(user):
    print(f"{user} 회원가입")
```

역시

로그를 추가해야 합니다.

```python
def register(user):
    print("로그 시작")
    print(f"{user} 회원가입")
    print("로그 종료")
```

---

파일 저장도 있습니다.

```python
def save():
    print("저장")
```

역시

같은 코드를 추가합니다.

```python
def save():
    print("로그 시작")
    print("저장")
    print("로그 종료")
```

---

코드를 보면

```text
로그 시작

...

로그 종료
```

가 계속 반복됩니다.

이런 코드는 좋은 코드가 아닙니다.

---

Python 개발자들은 생각했습니다.

> **"함수는 그대로 두고, 밖에서 기능만 추가할 수 없을까?"**

바로 이것이

Decorator가 등장한 이유입니다.

---

#### AI 서비스에서는?

AI 서비스를 생각해 봅시다.

모든 API는

```text
요청

↓

로그

↓

권한 확인

↓

실행 시간 측정

↓

실제 함수 실행

↓

응답
```

을 수행합니다.

모든 함수마다

같은 코드를 넣으면

유지보수가 어렵습니다.

Decorator는

이 문제를 해결합니다.

---

#### ② 개념 이해 (Concept)

#### Decorator란?

Decorator는

> **기존 함수를 수정하지 않고 새로운 기능을 추가하는 함수**

입니다.

핵심은

함수 자체는 변경하지 않는다는 것입니다.

---

#### 함수도 객체였다

지난 Unit에서

우리는

함수도 객체라고 배웠습니다.

```python
def hello():
    print("Hello")
```

메모리에서는

```text
hello

↓

Function Object
```

였습니다.

---

객체라면

다른 함수로 전달할 수 있습니다.

```python
def process(func):
    ...
```

여기서

```python
process(hello)
```

가능합니다.

Decorator는

바로

이 원리를 이용합니다.

---

#### 가장 간단한 Decorator

먼저

함수를 매개변수로 받습니다.

```python
def decorator(func):

    print("Decorator 실행")

    return func
```

사용

```python
def hello():
    print("Hello")

hello = decorator(hello)
```

---

실행하면

```text
Decorator 실행
```

이 출력됩니다.

---

그리고

```python
hello()
```

는

원래 함수가 실행됩니다.

---

#### 그런데 기능은 어디서 추가될까?

Decorator는

함수를

다른 함수로 감쌉니다.

```text
hello

↓

wrapper

↓

원래 hello
```

이 구조가 핵심입니다.

---

#### Wrapper 함수

Decorator의 진짜 모습입니다.

```python
def decorator(func):

    def wrapper():

        print("시작")

        func()

        print("끝")

    return wrapper
```

사용

```python
def hello():

    print("Hello")

hello = decorator(hello)

hello()
```

결과

```text
시작

Hello

끝
```

---

원래

hello()

는

```text
Hello
```

만 출력했습니다.

Decorator가

앞뒤에 기능을 추가했습니다.

---

#### 메모리에서 일어나는 일

원래

```text
hello

↓

Function
```

입니다.

Decorator 적용 후

```text
hello

↓

Wrapper Function

↓

Original Function
```

입니다.

즉

변수 hello가

원래 함수를 가리키는 것이 아니라

Wrapper를 가리키게 됩니다.

---

#### @ 문법

지금까지는

```python
hello = decorator(hello)
```

를 사용했습니다.

Python에서는

이를

더 쉽게 쓸 수 있습니다.

```python
@decorator
def hello():

    print("Hello")
```

이것은

사실

아래 코드와

완전히 같습니다.

```python
def hello():

    print("Hello")

hello = decorator(hello)
```

이것이

`@`

의 의미입니다.

---

#### 매개변수가 있는 함수

Decorator는

매개변수가 있는 함수도 처리해야 합니다.

```python
def login(name):

    print(name)
```

Wrapper도

같이 받아야 합니다.

```python
def decorator(func):

    def wrapper(name):

        print("시작")

        func(name)

        print("끝")

    return wrapper
```

---

하지만

매개변수가 계속 늘어나면

불편합니다.

그래서

실무에서는

```text
*args

**kwargs
```

를 사용합니다.

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("시작")

        result = func(*args, **kwargs)

        print("끝")

        return result

    return wrapper
```

이 형태가

실무에서 가장 많이 사용하는 Decorator 구조입니다.

---

#### 실행 순서

```python
@decorator
def hello():

    print("Hello")
```

실행

```text
hello()

↓

wrapper()

↓

시작

↓

원래 hello()

↓

끝
```

Decorator는

원래 함수의

앞뒤에

기능을 추가합니다.

---

#### AI 프로젝트에서는?

#### 실행 시간 측정

```python
@timer
def embedding():
    ...
```

---

#### 로그

```python
@logger
def OCR():
    ...
```

---

#### 인증

```python
@auth
def upload():
    ...
```

---

#### 캐시

```python
@cache
def search():
    ...
```

---

이런 기능은

실무에서 매우 흔합니다.

---

#### FastAPI에서는?

FastAPI에서

우리는

다음과 같은 코드를 작성하게 됩니다.

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

많은 사람들이

`@app.get`

을

특별한 문법이라고 생각합니다.

하지만

사실은

Decorator입니다.

즉

```text
@app.get("/")
```

는

> **"이 함수는 GET 요청이 오면 실행하세요."**

라는 정보를

FastAPI에게 등록하는 Decorator입니다.

---

예를 들어

```python
@app.post("/upload")
def upload():
    ...
```

는

FastAPI 내부에서

```text
upload 함수

↓

URL

↓

HTTP Method

↓

Routing Table 등록
```

을 수행합니다.

즉

Decorator가

함수를

웹 서버에 등록하는 역할을 합니다.

---

#### AI 서비스에서는 어떻게 사용할까?

```python
@app.post("/chat")
def chat():
    ...
```

↓

사용자 요청

↓

Decorator

↓

FastAPI Router

↓

chat()

---

```python
@app.post("/embedding")
def embedding():
    ...
```

↓

Embedding API 등록

---

```python
@app.post("/OCR")
def OCR():
    ...
```

↓

OCR API 등록

---

FastAPI의 모든 Endpoint는

Decorator를 사용합니다.

---

#### Decorator를 사용하는 이유

Decorator가 없다면

FastAPI는

```python
app.register(

    "/chat",

    chat

)
```

같은 코드를

직접 작성해야 합니다.

Decorator를 사용하면

코드가

훨씬 읽기 쉬워집니다.

---

#### Decorator와 고차 함수의 관계

지난 Unit에서

고차 함수를 배웠습니다.

Decorator도

고차 함수입니다.

왜냐하면

```text
def decorator(func):
```

처럼

함수를

매개변수로 받기 때문입니다.

그리고

새로운 함수를

반환합니다.

즉

Decorator는

고차 함수의 대표적인 활용 사례입니다.

---

#### 실무 Best Practice

#### ① 공통 기능은 Decorator로 분리한다.

로그, 인증, 실행 시간 측정, 예외 처리 등 여러 함수에서 반복되는 기능은 Decorator로 분리하면 코드 중복을 줄일 수 있습니다.

---

#### ② Decorator는 비즈니스 로직과 분리한다.

함수 안에는 핵심 기능만 작성하고,

부가 기능은 Decorator에 맡기는 것이 유지보수에 유리합니다.

---

#### ③ `*args`, `**kwargs`를 사용하는 형태를 익혀두자.

실무에서는 함수의 매개변수 개수가 다양하기 때문에 대부분 다음과 같은 형태를 사용합니다.

```python
def wrapper(*args, **kwargs):
    ...
```

---

#### 자주 발생하는 실수

#### 1. Decorator가 원래 함수를 수정한다고 생각

아닙니다.

원래 함수는 그대로 있고,

Wrapper 함수가 대신 호출됩니다.

---

#### 2. `@`가 새로운 문법이라고 생각

```text
@decorator
```

는

```python
hello = decorator(hello)
```

의 축약 문법입니다.

---

#### 3. Wrapper에서 원래 함수를 호출하지 않는 경우

```python
def wrapper():
    print("시작")
```

이렇게 작성하면 원래 함수는 실행되지 않습니다.

반드시

```python
func()
```

를 호출해야 합니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
HTTP Request

      │

      ▼

@app.post()

      │

      ▼

Decorator

      │

      ▼

Authentication

      │

      ▼

Logging

      │

      ▼

Original Function

      │

      ▼

Response
```

또는

```text
사용자 요청

      │

      ▼

FastAPI Router

      │

      ▼

Decorator

      │

      ▼

Chat Function

      │

      ▼

OpenAI API
```

Decorator는 **AI 서비스의 비즈니스 로직과 공통 기능을 분리하는 핵심 메커니즘**이며, FastAPI의 모든 API Endpoint 등록이 이 원리를 기반으로 동작합니다.

---

#### 핵심 내용 정리

이번 Unit에서는 **Decorator**를 학습했습니다.

핵심은 다음과 같습니다.

- Decorator는 **기존 함수를 수정하지 않고 기능을 추가하는 고차 함수**이다.
- 함수도 객체이므로 다른 함수의 인자로 전달하거나 새로운 함수로 감쌀 수 있다.
- `@decorator` 문법은 `function = decorator(function)`의 축약 표현이다.
- Decorator는 Wrapper 함수를 통해 원래 함수의 실행 전후에 기능을 추가한다.
- AI 서비스에서는 로그, 인증, 권한 검사, 실행 시간 측정, 캐싱 등에 활용되며, **FastAPI의 `@app.get`, `@app.post` 역시 Decorator**이다.

---

## Part 2-3. Class와 객체지향 설계

### Module 07. 객체지향 프로그래밍(OOP) ① - 왜 Class가 필요한가?

#### Module 실습 예제

- [예제 1: function_to_service.py](examples/module_07/function_to_service.py) — 관련 데이터와 동작을 Class로 묶는 이유를 확인합니다.
- [예제 2: chat_service_responsibility.py](examples/module_07/chat_service_responsibility.py) — ChatService가 하나의 Use Case를 담당하도록 설계합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- 객체지향 프로그래밍(OOP)은 왜 등장했는가?
- Class와 Object는 무엇인가?
- 변수와 함수만으로는 어떤 한계가 있는가?
- AI 서비스에서는 왜 대부분 Class를 사용하는가?
- 앞으로 FastAPI와 OpenAI SDK에서는 왜 Class가 계속 등장하는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 Python의 대부분의 문법을 배웠습니다.

- 변수
- 함수
- List
- Dictionary
- Generator
- Decorator
- Context Manager

이 정도면 프로그램을 만들 수 있습니다.

실제로 간단한 AI 프로그램도 만들 수 있습니다.

---

예를 들어 OCR 프로그램을 만든다고 해봅시다.

```python
ocr_language = "ko"

ocr_confidence = 0.8

def recognize(image):
    ...
```

처음에는 문제가 없습니다.

---

그런데 OCR 모델이 하나 더 추가됩니다.

```python
ocr1_language = "ko"
ocr1_confidence = 0.8

ocr2_language = "en"
ocr2_confidence = 0.9
```

변수가 계속 늘어납니다.

---

Embedding 모델도 추가합니다.

```python
embedding_dimension = 1536

embedding_model = "text-embedding"
```

---

LLM도 있습니다.

```python
llm_model = "gpt"

temperature = 0.7

max_tokens = 1000
```

---

프로젝트가 커질수록

변수는

```text
OCR

Embedding

LLM

Database

Config

User

PDF

...
```

계속 증가합니다.

---

이번에는 함수도 보겠습니다.

```python
def ocr():
    ...

def embedding():
    ...

def summarize():
    ...

def chat():
    ...

def search():
    ...
```

프로젝트가 커질수록

함수도 수백 개가 됩니다.

---

여기서 문제가 발생합니다.

> **"OCR와 관련된 변수는 어디 있지?"**

> **"Embedding 설정은 어디 있지?"**

> **"User 정보는 어디에 저장하지?"**

관련 있는 데이터가 흩어져 있기 때문입니다.

---

#### 현실 세계를 생각해 보자

학생 한 명을 생각해 봅시다.

학생에게는

```text
이름

학번

나이

학과
```

가 있습니다.

그리고

학생은

```text
공부한다

출석한다

시험본다
```

라는 행동도 합니다.

---

지금까지 배운 방식이라면

```python
name = "Kim"

age = 20

major = "AI"

def study():
    ...

def attend():
    ...
```

입니다.

---

그런데

학생이 두 명이면?

```python
name1 = "Kim"

age1 = 20

major1 = "AI"

name2 = "Lee"

age2 = 21

major2 = "Computer"
```

금방 복잡해집니다.

---

우리는 현실에서도

학생을

이렇게 관리하지 않습니다.

```text
학생

↓

이름

나이

학과

행동
```

하나의 객체로 생각합니다.

프로그래밍도 마찬가지입니다.

이것이 객체지향(Object-Oriented)의 출발점입니다.

---

#### 객체지향이 해결하려는 문제

기존 방식

```text
name

age

major

study()

attend()

exam()
```

모두 흩어져 있습니다.

---

객체지향

```text
Student

├── name

├── age

├── major

├── study()

├── attend()

└── exam()
```

관련 있는 데이터와 기능을 하나로 묶습니다.

---

이것을

> **객체(Object)**

라고 합니다.

---

#### AI 서비스에서는?

AI 서비스를 생각해 봅시다.

OCR 모델 하나에는

```text
Model Name

Language

Threshold

Device
```

가 있습니다.

그리고

행동도 있습니다.

```text
Load()

Recognize()

Save()
```

---

Embedding 모델도

```text
Model Name

Dimension

Provider
```

과

```text
Embed()

Batch Embed()
```

를 가집니다.

---

즉

현실에서는

```text
OCR

↓

데이터

+

기능
```

입니다.

이것이

객체지향입니다.

---

#### ② 개념 이해 (Concept)

#### 객체(Object)란?

우리는 Unit 4에서

Object를 배웠습니다.

그때의 Object는

메모리에 존재하는 객체였습니다.

예를 들어

```python
number = 10
```

에서

10도 Object였습니다.

---

객체지향에서 말하는 Object는

조금 더 큰 의미입니다.

> **현실 세계의 하나의 대상을 프로그램으로 표현한 것**

입니다.

예를 들어

학생

자동차

PDF

OCR

LLM

모두 Object가 될 수 있습니다.

---

#### Class란?

많은 사람들이

Class와 Object를 혼동합니다.

먼저 비유를 하나 해보겠습니다.

---

붕어빵 틀이 있습니다.

```text
붕어빵 틀
```

그리고

붕어빵을 만듭니다.

```text
붕어빵

붕어빵

붕어빵
```

붕어빵 틀은

하나입니다.

붕어빵은

여러 개입니다.

---

프로그래밍에서는

```text
Class

↓

Object

Object

Object
```

입니다.

---

즉

Class는

> **객체를 만들기 위한 설계도(Blueprint)**

입니다.

---

Object는

> **설계도로부터 만들어진 실제 객체(Instance)**

입니다.

---

#### 자동차 예제

자동차를 만든다고 생각해 봅시다.

Class

```text
Car

색상

속도

브레이크

주행
```

---

Object

```text
Sonata

↓

흰색

↓

80km
```

---

또 다른 Object

```text
Avante

↓

검정

↓

50km
```

---

Class는 하나입니다.

Object는 여러 개입니다.

---

#### AI에서는?

Class

```text
OCRModel
```

Object

```text
한국어 OCR

영어 OCR

일본어 OCR
```

---

Class

```text
ChatModel
```

Object

```text
GPT-4

GPT-5

Claude

Gemini
```

---

즉

Class는

종류입니다.

Object는

실제 대상입니다.

---

#### 객체지향의 핵심

객체는

항상 두 가지를 가집니다.

#### ① 데이터(State)

예를 들어

```text
Student

↓

name

↓

age

↓

major
```

---

#### ② 행동(Behavior)

```text
study()

exam()

attend()
```

---

즉

객체는

```text
데이터

+

기능
```

을 함께 가집니다.

---

#### 왜 같이 묶을까?

예를 들어

OCR 모델입니다.

```text
OCR

↓

Language

↓

Threshold
```

이 있습니다.

OCR와 관계없는 함수가

이 데이터를 수정하면 안 됩니다.

OCR와 관련된 기능만

접근하는 것이 자연스럽습니다.

그래서

데이터와 기능을 함께 묶습니다.

---

#### 객체지향을 사용하는 이유

프로그램이 커질수록

다음이 쉬워집니다.

```text
기능 추가

기능 수정

기능 재사용

유지보수
```

---

특히

AI 프로젝트는

수백 개의 파일

수천 개의 함수

수십 개의 모델을 사용합니다.

객체지향이 아니면

관리하기 매우 어렵습니다.

---

#### AI 프로젝트에서는?

예를 들어

Document AI 시스템

```text
PDF

OCR

Embedding

VectorDB

LLM
```

각각이

하나의 객체가 됩니다.

---

예를 들어

```text
PDFLoader

↓

load()
```

---

```text
OCRProcessor

↓

recognize()
```

---

```text
EmbeddingModel

↓

embed()
```

---

실무 프로젝트는

거의 이런 구조입니다.

---

#### AI 프레임워크도 모두 객체지향

앞으로 배우게 될

FastAPI

LangChain

OpenAI SDK

Pydantic

SQLAlchemy

거의 모두

Class 기반입니다.

예를 들어(OpenAI SDK의 개념적 예)

```python
client = OpenAI()
```

여기서

```text
OpenAI

↓

Class
```

---

```text
client

↓

Object
```

입니다.

---

FastAPI도

```python
app = FastAPI()
```

입니다.

역시

```text
FastAPI

↓

Class
```

---

```text
app

↓

Object
```

입니다.

---

#### 객체지향의 핵심 사고방식

절차지향

```text
함수 중심

↓

데이터 전달

↓

함수 실행
```

---

객체지향

```text
객체 중심

↓

객체가

자신의 데이터를 가지고

스스로 동작
```

---

이 차이가

객체지향의 핵심입니다.

---

#### 실무 Best Practice

#### ① 현실 세계를 먼저 모델링한다.

코드를 작성하기 전에 먼저 생각합니다.

> "이 프로젝트에는 어떤 객체들이 존재하는가?"

예를 들어 Document AI라면

- PDF
- OCR
- Embedding
- LLM
- User

와 같은 객체를 먼저 정의하는 것이 좋습니다.

---

#### ② 관련 있는 데이터와 기능을 함께 묶는다.

좋지 않은 예

```text
OCR 설정

↓

프로젝트 여기저기에 흩어짐
```

좋은 예

```text
OCRModel

├── language

├── threshold

└── recognize()
```

---

#### ③ Class는 설계도, Object는 실제 사용 대상이라는 관점을 유지한다.

이 구분이 명확해야 이후 생성자(`__init__`), 상속, 다형성도 쉽게 이해할 수 있습니다.

---

#### 자주 발생하는 실수

#### 1. Class와 Object를 같은 것으로 생각

아닙니다.

- Class → 설계도
- Object(Instance) → 설계도로부터 만들어진 실제 객체

입니다.

---

#### 2. 객체는 데이터만 가진다고 생각

객체는

```text
데이터

+

행동(메서드)
```

를 함께 가집니다.

---

#### 3. 모든 것을 Class로 만들려고 하는 경우

객체지향이 강력하다고 해서 모든 코드를 Class로 만들 필요는 없습니다.

간단한 유틸리티 함수나 일회성 스크립트는 함수만으로도 충분한 경우가 많습니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
AI Application

        │

        ▼

─────────────────────────

PDFLoader

    │

    └── load()

─────────────────────────

OCRProcessor

    │

    └── recognize()

─────────────────────────

EmbeddingModel

    │

    └── embed()

─────────────────────────

LLMClient

    │

    └── chat()

─────────────────────────
```

실제 AI 서비스는 **기능별 Class들이 협력하여 하나의 시스템을 구성**합니다.

---

#### 핵심 내용 정리

이번 Unit에서는 **객체지향 프로그래밍(OOP)의 필요성**을 학습했습니다.

핵심은 다음과 같습니다.

- 객체지향은 **관련 있는 데이터와 기능을 하나의 객체로 묶기 위해 등장한 프로그래밍 방식**이다.
- **Class는 객체를 만들기 위한 설계도**, **Object(Instance)는 설계도로부터 생성된 실제 객체**이다.
- 객체는 **데이터(State)** 와 **행동(Behavior)** 을 함께 가진다.
- 프로젝트가 커질수록 객체지향은 코드의 재사용성과 유지보수성을 크게 향상시킨다.
- FastAPI, OpenAI SDK, LangChain, Pydantic의 주요 API에는 클래스와 객체지향 개념이 자주 활용된다.

---

### Module 08. 객체지향 프로그래밍(OOP) ② - Class와 Object 생성

#### Module 실습 예제

- [예제 1: class_objects.py](examples/module_08/class_objects.py) — 생성자·인스턴스 변수·메서드를 연습합니다.
- [예제 2: document_service.py](examples/module_08/document_service.py) — 객체별 상태가 독립적으로 유지되는지 확인합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Class는 어떻게 만드는가?
- Object는 어떻게 생성되는가?
- `__init__()`는 왜 필요한가?
- `self`는 무엇인가?
- AI 프로젝트에서는 Class를 어떻게 사용하는가?

---

#### ① 문제 이해 (Why)

지난 Unit에서는

Class는 설계도,

Object는 실제 객체라고 배웠습니다.

하지만 아직 실제 Class를 만들어보지는 않았습니다.

---

학생을 예로 들어보겠습니다.

학생이 한 명 있습니다.

```text
Kim

20세

AI학과
```

학생이 두 명이 됩니다.

```text
Kim

20

AI
```

```text
Lee

21

Computer
```

학생이 백 명이 됩니다.

```text
Student1

Student2

...

Student100
```

---

이전 방식이라면

```python
name1 = "Kim"
age1 = 20

name2 = "Lee"
age2 = 21
```

처럼 작성해야 합니다.

관리하기 어렵습니다.

---

우리가 원하는 것은

```python
student1 = Student(...)

student2 = Student(...)
```

처럼 만드는 것입니다.

이것이 Class의 목적입니다.

---

#### AI 프로젝트에서는?

OCR 모델

```text
OCR1

OCR2

OCR3
```

모두

같은 기능을 합니다.

하지만

언어

Threshold

Device

등은 다릅니다.

---

Embedding 모델도

```text
OpenAI

BGE

E5

MiniLM
```

모두

Embedding이라는 공통 기능을 수행합니다.

이럴 때

Class 하나를 만들고

Object만 여러 개 생성합니다.

---

#### ② 개념 이해 (Concept)

#### Class 만들기

Python에서는

```text
class 클래스이름:
```

으로 시작합니다.

가장 간단한 Class입니다.

```python
class Student:
    pass
```

여기서

```python
pass
```

는

아직 아무 기능도 없다는 의미입니다.

---

Class는

메모리에서

```text
Student

↓

Class Object
```

입니다.

Class도

객체(Object)입니다.

이 점은 매우 중요합니다.

---

#### Object 생성

Object를 만드는 것을

> **Instantiation(인스턴스화)**

라고 합니다.

생성은

```python
student = Student()
```

입니다.

메모리에서는

```text
Student Class

↓

Student Object

↓

student
```

입니다.

---

Object를 여러 개 만들 수 있습니다.

```python
student1 = Student()

student2 = Student()

student3 = Student()
```

메모리

```text
Student Class

│

├── student1

├── student2

└── student3
```

설계도는 하나,

객체는 여러 개입니다.

---

#### 생성자(Constructor)

학생을 만들었습니다.

```python
student = Student()
```

그런데

이름은 어디 있을까요?

나이는?

학과는?

없습니다.

---

객체를 생성하면서

초기값도 같이 넣고 싶습니다.

이를 위해

생성자가 등장합니다.

Python에서는

```python
__init__()
```

을 사용합니다.

---

#### **init**()

가장 기본적인 형태입니다.

```python
class Student:

    def __init__(self):

        print("학생 생성")
```

객체 생성

```python
student = Student()
```

결과

```text
학생 생성
```

입니다.

---

여기서 중요한 점은

우리가

```python
student.__init__()
```

를 호출하지 않았다는 것입니다.

Python이

자동으로 호출합니다.

---

#### Object 생성 과정

```python
student = Student()
```

실제로는

```text
메모리 확보

↓

Student Object 생성

↓

__init__() 호출

↓

초기화 완료

↓

student 변수 연결
```

입니다.

---

#### 왜 이름이 init일까?

Initialize

↓

초기화

라는 의미입니다.

즉

객체를

사용할 준비를 하는 함수입니다.

---

#### self란?

가장 많이 헷갈리는 부분입니다.

먼저

다음 코드를 보겠습니다.

```python
class Student:

    def __init__(self):

        print(self)
```

객체 생성

```python
student = Student()
```

출력

```text
<__main__.Student object at ...>
```

입니다.

---

self는

바로

생성된 객체 자신입니다.

---

비유하면

학생이 자기 자신을 가리키는 것입니다.

```text
학생

↓

"나"
```

self는

객체 입장에서

> **"나 자신"**

입니다.

---

#### self가 필요한 이유

학생 두 명이 있습니다.

```python
student1 = Student()

student2 = Student()
```

Python은

```text
student1

↓

Student Object
```

```text
student2

↓

Student Object
```

를 만들어야 합니다.

---

그런데

어떤 객체를 초기화해야 하는지

어떻게 알까요?

바로

self가 알려줍니다.

---

즉

```text
def __init__(self):
```

의 self는

현재 생성 중인

객체를 의미합니다.

---

#### 인스턴스 변수

학생마다

이름이 다릅니다.

```python
class Student:

    def __init__(self):

        self.name = "Kim"
```

여기서

```python
self.name
```

이

객체 안에 저장됩니다.

메모리

```text
Student Object

│

└── name

↓

Kim
```

---

객체마다

다른 값을 가질 수 있습니다.

---

#### 매개변수 받기

실제로는

```python
class Student:

    def __init__(

        self,

        name,

        age

    ):

        self.name = name

        self.age = age
```

생성

```python
student = Student(

    "Kim",

    20

)
```

메모리

```text
Student Object

│

├── name

│      ↓

│     Kim

│

└── age

       ↓

      20
```

---

다른 학생

```python
student2 = Student(

    "Lee",

    21

)
```

메모리

```text
Student2

│

├── name

│      ↓

│     Lee

│

└── age

       ↓

      21
```

---

같은 Class

다른 데이터입니다.

---

#### 객체 접근

```python
print(student.name)
```

결과

```text
Kim
```

---

```python
print(student.age)
```

결과

```text
20
```

점(.)을 사용합니다.

---

#### 메서드(Method)

객체는

데이터뿐 아니라

행동도 가집니다.

```python
class Student:

    def __init__(

        self,

        name

    ):

        self.name = name

    def study(self):

        print(

            self.name,

            "공부중"

        )
```

사용

```python
student = Student("Kim")

student.study()
```

결과

```text
Kim 공부중
```

---

#### 메모리 구조

```text
Student Object

│

├── name

│      ↓

│     Kim

│

└── study()

       │

       └── Function
```

객체 안에는

데이터와 함수가

함께 존재합니다.

---

#### AI 프로젝트에서는?

OCR 모델

```python
class OCRModel:

    def __init__(

        self,

        language

    ):

        self.language = language

    def recognize(

        self,

        image

    ):

        ...
```

---

Embedding

```python
class EmbeddingModel:

    def __init__(

        self,

        model_name

    ):

        self.model_name = model_name

    def embed(

        self,

        text

    ):

        ...
```

---

LLM

```python
class ChatModel:

    def __init__(

        self,

        model

    ):

        self.model = model

    def chat(

        self,

        message

    ):

        ...
```

실무는

거의 이런 구조입니다.

---

#### FastAPI에서는?

```python
app = FastAPI()
```

여기서

```text
FastAPI

↓

Class
```

---

```text
app

↓

Object
```

입니다.

---

OpenAI SDK도

```python
client = OpenAI()
```

입니다.

역시

Class에서

Object를 생성합니다.

---

Pydantic도

```text
class User(...):
```

입니다.

---

AI 프레임워크 대부분이

Class 기반입니다.

---

#### 실무 Best Practice

#### ① 생성자에서 객체를 초기화한다.

객체를 생성한 직후 사용할 수 있도록 필요한 값을 `__init__()`에서 준비하는 것이 좋습니다.

---

#### ② 인스턴스 변수는 `self`를 사용한다.

```python
self.name

self.model

self.language
```

처럼 객체가 가진 데이터는 항상 `self`를 통해 저장합니다.

---

#### ③ 하나의 Class는 하나의 역할을 갖도록 설계한다.

좋은 예

```text
OCRModel

↓

OCR만 담당
```

좋은 설계는 객체의 책임이 명확합니다.

---

#### 자주 발생하는 실수

#### 1. `self`를 직접 전달하려는 경우

잘못된 예

```python
Student(self, "Kim")
```

입니다.

`self`는 Python이 자동으로 전달합니다.

올바른 코드는

```python
Student("Kim")
```

입니다.

---

#### 2. `self.name` 대신 `name`만 사용하는 경우

```python
class Student:

    def __init__(self, name):

        name = name
```

이 코드는 객체에 저장되지 않습니다.

반드시

```python
self.name = name
```

으로 작성해야 합니다.

---

#### 3. 모든 데이터를 생성 후 따로 저장

```python
student = Student()

student.name = "Kim"
```

가능은 하지만,

객체 생성 시 필요한 정보는 생성자를 통해 전달하는 것이 더 자연스럽고 안전합니다.

---

#### AI 서비스에서의 역할 (Architecture)

```text
FastAPI()

        │

        ▼

FastAPI Object

        │

        ▼

add_route()

        ▼

Server
```

또는

```text
OpenAI()

        │

        ▼

Client Object

        │

        ▼

chat()

        ▼

OpenAI API
```

또는

```text
OCRModel()

        │

        ▼

OCR Object

        │

        ▼

recognize()

        ▼

Text
```

객체는 **상태(데이터)를 유지하면서 필요한 기능(메서드)을 수행하는 실행 단위**입니다.

---

#### 핵심 내용 정리

이번 Unit에서는 **Class와 Object 생성**을 학습했습니다.

핵심은 다음과 같습니다.

- `class`는 객체를 만들기 위한 **설계도**이다.
- `Student()`처럼 Class를 호출하면 새로운 **Object(Instance)** 가 생성된다.
- `__init__()`는 객체 생성 시 자동으로 호출되는 **생성자(Constructor)** 이며 객체를 초기화한다.
- `self`는 **현재 객체 자신**을 의미하며, 객체의 데이터와 메서드에 접근할 때 사용한다.
- 객체는 **인스턴스 변수(`self.xxx`)** 와 **메서드**를 함께 가진다.
- FastAPI, OpenAI SDK, LangChain의 주요 API를 사용할 때 이러한 객체 생성 방식을 자주 접하게 된다.

---

### Module 09. 상속(Inheritance)

#### Module 실습 예제

- [예제 1: inheritance_basics.py](examples/module_09/inheritance_basics.py) — 부모 Class의 공통 기능을 자식 Class가 물려받습니다.
- [예제 2: base_model_analogy.py](examples/module_09/base_model_analogy.py) — 기반 Class를 상속해 공통 검증 규칙을 재사용합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- 상속(Inheritance)은 왜 필요한가?
- 상속은 단순히 코드를 복사하는 것과 무엇이 다른가?
- 부모 클래스와 자식 클래스는 어떤 관계인가?
- Python은 상속을 어떻게 구현하는가?
- AI 서비스에서는 상속을 언제 사용하는가?

---

#### ① 문제 이해 (Why)

#### Class만으로는 충분하지 않을까?

지금까지 우리는 Class를 이용해서 객체를 만들었습니다.

예를 들어 AI 서비스에는 다음과 같은 객체들이 존재할 수 있습니다.

```text
PDFDocument
WordDocument
ImageDocument
```

이 객체들은 서로 다른 문서입니다.

하지만 공통점도 있습니다.

- 파일 이름이 있다.
- 파일 크기가 있다.
- 저장 위치가 있다.
- 열 수 있다.
- 삭제할 수 있다.

각 클래스를 독립적으로 만든다면

```python
class PDFDocument:
    ...

class WordDocument:
    ...

class ImageDocument:
    ...
```

모든 클래스에서

```python
filename
size
path
open()
delete()
```

를 계속 작성해야 합니다.

즉,

> **중복 코드가 발생합니다.**

---

#### 중복은 유지보수를 어렵게 만든다.

예를 들어

```python
delete()
```

기능을 수정해야 한다고 가정해봅시다.

그렇다면

```text
PDFDocument 수정

↓

WordDocument 수정

↓

ImageDocument 수정

↓

ExcelDocument 수정

↓

PowerPointDocument 수정
```

모든 클래스를 수정해야 합니다.

하나라도 빠뜨리면

서비스의 동작이 달라질 수 있습니다.

---

#### 객체들은 사실 "종류"만 다르다.

우리가 현실에서 생각해보면

```text
동물

├── 강아지
├── 고양이
├── 토끼
└── 새
```

모두 동물입니다.

공통점

- 먹는다.
- 숨쉰다.
- 움직인다.

차이점

- 짖는다.
- 야옹한다.
- 난다.

즉,

공통 기능과

개별 기능이 함께 존재합니다.

프로그래밍도 동일합니다.

---

#### 그래서 등장한 것이 상속(Inheritance)이다.

상속은

> **공통 기능은 부모가 가지고, 필요한 부분만 자식이 추가하는 구조**입니다.

---

#### AI 서비스에서는 왜 필요한가?

AI 프로젝트를 생각해봅시다.

```text
Document
```

를 부모 클래스로 만든다면

```text
Document

├── PDFDocument
├── WordDocument
├── ImageDocument
└── HWPDocument
```

공통 기능

```text
save()

load()

delete()

metadata
```

는 부모가 가지고

각 문서만의 기능은

자식이 구현합니다.

예를 들어

```text
ImageDocument

↓

OCR()
```

```text
PDFDocument

↓

extract_text()
```

처럼 구현할 수 있습니다.

이렇게 하면

새로운 문서 형식이 추가되어도

공통 기능을 다시 작성할 필요가 없습니다.

---

#### ② 개념 이해 (Concept)

#### 상속(Inheritance)의 정의

상속은

> **기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 기능**입니다.

---

#### 부모 클래스

상속해주는 클래스

```text
Parent Class

또는

Base Class

또는

Super Class
```

---

#### 자식 클래스

상속받는 클래스

```text
Child Class

또는

Derived Class

또는

Sub Class
```

---

#### 구조

```text
Parent

↓

Child
```

Child는

Parent의 기능을 사용할 수 있습니다.

---

#### Python 문법

```python
class Parent:
    ...

class Child(Parent):
    ...
```

괄호 안에

부모 클래스를 적으면 됩니다.

---

#### ③ 구조 이해 (Architecture)

상속 구조는 다음과 같습니다.

```text
            Object
               │
               │
          Document
        ┌──────┴──────┐
        │             │
 PDFDocument    ImageDocument
        │             │
 extract()      run_ocr()
```

데이터는

```text
객체 생성

↓

자식 객체 생성

↓

부모 초기화

↓

자식 초기화

↓

객체 사용
```

순서로 동작합니다.

---

#### 상속은 메모리에서 어떻게 동작할까?

예를 들어

```python
pdf = PDFDocument()
```

객체를 만들면

메모리에서는

```text
PDFDocument Object

↓

PDFDocument Method

↓

Document Method

↓

object
```

순서대로 필요한 기능을 찾습니다.

이 과정을

**Method Resolution Order(MRO)** 라고 합니다.

(다중 상속에서 자세히 학습합니다.)

---

#### ④ 실습 준비

현재까지의 프로젝트 구조를 그대로 사용합니다.

```text
python-ai/

    oop/

        inheritance.py
```

추가 라이브러리는 필요 없습니다.

---

#### ⑤ 기본 사용법

#### 가장 단순한 상속

```python
class Animal:
    def eat(self):
        print("먹는다.")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()
```

출력

```text
먹는다.
```

---

#### 코드 분석

부모

```text
class Animal:
```

자식

```text
class Dog(Animal):
```

여기서

```python
pass
```

는

아무 기능도 추가하지 않았다는 의미입니다.

하지만

```python
Dog
```

는

```python
Animal
```

의 기능을 모두 사용할 수 있습니다.

---

#### 속성도 상속된다.

```python
class Animal:

    def __init__(self):
        self.alive = True


class Dog(Animal):
    pass


dog = Dog()

print(dog.alive)
```

출력

```text
True
```

부모가 만든

```python
alive
```

속성을

자식도 그대로 사용할 수 있습니다.

---

#### 새로운 기능 추가하기

```python
class Animal:

    def eat(self):
        print("먹는다.")


class Dog(Animal):

    def bark(self):
        print("멍멍!")


dog = Dog()

dog.eat()

dog.bark()
```

출력

```text
먹는다.

멍멍!
```

즉,

```text
부모 기능

+

자식 기능
```

을 동시에 사용할 수 있습니다.

---

#### AI 서비스 예제

```python
class Document:

    def save(self):
        print("파일 저장")


class PDFDocument(Document):

    def extract_text(self):
        print("PDF 텍스트 추출")


pdf = PDFDocument()

pdf.save()

pdf.extract_text()
```

출력

```text
파일 저장

PDF 텍스트 추출
```

이 구조는 실제 AI 문서 처리 시스템에서도 매우 자주 사용됩니다.

---

#### ⑥ 실무 활용

실무에서는 상속을 다음과 같이 활용합니다.

```text
Document

├── PDFDocument
├── WordDocument
├── ImageDocument
```

또는

```text
Model

├── OpenAIModel
├── OllamaModel
├── ClaudeModel
```

공통 인터페이스를 유지하면서 서비스별 기능을 추가할 수 있습니다.

---

#### 실무 Best Practice

상속은 강력하지만 **무조건 사용하는 것이 좋은 것은 아닙니다.**

다음과 같은 경우에 적합합니다.

- 진짜 부모-자식 관계가 존재한다.
- 공통 기능이 많다.
- 여러 클래스가 동일한 규칙을 따라야 한다.

반대로 단순히 코드 재사용만을 위해 억지로 상속을 만드는 것은 피해야 합니다.

---

#### ⑦ 자주 발생하는 실수

##### 1. 상속과 복사를 혼동

```text
class Dog(Animal):
```

은

Animal의 기능을 **복사하는 것**이 아니라

**확장하는 것**입니다.

---

##### 2. 부모를 수정하면 자식도 영향을 받는다.

부모 메서드를 변경하면

모든 자식 클래스의 동작도 바뀔 수 있습니다.

따라서 부모 클래스는 신중하게 설계해야 합니다.

---

##### 3. 아무 관계 없는 클래스도 상속

예를 들어

```text
Car

↓

Apple
```

처럼 의미 없는 상속은 설계 오류입니다.

상속은 **"~는 ~이다(is-a)"** 관계일 때 사용하는 것이 좋습니다.

예를 들어,

- `Dog`는 `Animal`이다. ✅
- `PDFDocument`는 `Document`이다. ✅

---

#### ⑧ 핵심 내용 정리

이번 Unit의 핵심은 다음과 같습니다.

- 상속은 **공통 기능을 재사용하기 위한 객체지향 기법**이다.
- 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는다.
- 자식은 부모의 기능을 그대로 사용하면서 자신의 기능을 추가할 수 있다.
- AI 서비스에서는 문서, 모델, 데이터 처리기 등 공통 기능이 많은 객체를 설계할 때 매우 자주 사용된다.
- 좋은 상속은 **명확한 부모-자식 관계**를 표현하며, 단순한 코드 재사용만을 위해 남용해서는 안 된다.

---

---

## Part 2-4. Type Hint와 Generic

### Module 10. Type Hint와 Generic - 더 안전하고 읽기 쉬운 Python 코드

#### Module 실습 예제

- [예제 1: type_hints.py](examples/module_10/type_hints.py) — 함수와 Collection에 Type Hint를 적용합니다.
- [예제 2: generic_result.py](examples/module_10/generic_result.py) — Generic Result로 여러 결과 타입을 안전하게 표현합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- Type Hint는 왜 등장했는가?
- Python은 동적 타입 언어인데 타입을 왜 적는가?
- Type Hint와 실제 타입 검사는 어떤 차이가 있는가?
- Generic은 왜 필요한가?
- AI 서비스에서는 어떻게 활용하는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 이런 함수를 많이 작성했습니다.

```python
def add(a, b):
    return a + b
```

이 함수를 사용하는 사람이 있습니다.

```python
result = add("10", "20")
```

문제가 있을까요?

없습니다.

Python은 문자열도

```text
+
```

연산이 가능하기 때문입니다.

결과는

```text
1020
```

입니다.

---

그런데 다른 사람은

이렇게 사용합니다.

```python
result = add(10, 20)
```

결과는

```text
30
```

입니다.

---

또 다른 사람은

```python
result = add([1], [2])
```

결과는

```text
[1, 2]
```

입니다.

---

#### 함수는 무엇을 위한 함수일까?

코드만 보면

```text
def add(a, b):
```

여기서

```text
a

b
```

가 무엇인지 알 수 없습니다.

- int?
- float?
- str?
- list?
- Document?
- Embedding?

모두 가능합니다.

---

#### 프로젝트가 커질수록 문제가 된다.

예를 들어

```text
def search(query):
```

여기서

```text
query
```

는

무엇일까요?

```python
str
```

일까요?

```python
Document
```

일까요?

```python
Embedding
```

일까요?

코드만 봐서는

전혀 알 수 없습니다.

---

#### AI 프로젝트에서는 더 심각하다.

예를 들어

```text
def embed(data):
```

여기서

```text
data
```

가

```text
Text

Document

Chunk

Image
```

중 무엇인지

모르면

함수를 사용할 때

계속 문서를 찾아봐야 합니다.

---

#### 그래서 등장한 것이 Type Hint이다.

> **"이 함수는 어떤 타입을 입력받고 어떤 타입을 반환하는지 명확하게 표현하는 방법"**

---

#### ② 개념 이해 (Concept)

Type Hint는

Python 3.5부터

도입되었습니다.

---

#### 정의

> **변수, 함수, 클래스에 타입 정보를 명시하는 문법**

---

중요한 점은 Type Hint 자체가 일반 함수 호출에서 인자와 반환값의 타입을
자동으로 강제하지는 않는다는 것입니다.

Annotation 정보는 함수의 `__annotations__` 등에 저장될 수 있으며,
IDE·정적 분석기뿐 아니라 FastAPI와 Pydantic 같은 Framework가
실행 중 읽어 검증이나 문서 생성에 활용할 수도 있습니다.

---

#### 예제

기존

```python
def add(a, b):
    return a + b
```

Type Hint

```python
def add(a: int, b: int) -> int:
    return a + b
```

읽는 순간

바로 이해됩니다.

```text
입력

↓

int

↓

출력

↓

int
```

---

#### Python은 Type Hint를 자동으로 강제할까?

아닙니다.

```python
def add(a: int, b: int):

    return a + b
```

실행

```python
print(add("A", "B"))
```

결과

```text
AB
```

입니다.

Python은

오류를 내지 않습니다.

---

기본 Python 함수 호출은 Annotation만 보고 타입 오류를 자동으로 발생시키지
않기 때문입니다. Type Hint는 문서화와 정적 분석의 기반이며,
별도 Runtime 도구가 읽어 동작에 활용할 수도 있습니다.

---

#### 실제 검사는 누가 할까?

실무에서는 IDE와 정적 분석기가 Type Hint를 이용합니다.

예를 들어

```text
VSCode

PyCharm

mypy

Pylance
```

이

미리 오류를 알려줍니다.

---

#### ③ 구조 이해 (Architecture)

함수는

다음과 같이 표현됩니다.

```text
입력

↓

Type Hint

↓

함수 실행

↓

반환 Type
```

예를 들어

```text
def square(x: int) -> int:
```

의 의미는

```text
int

↓

square()

↓

int
```

입니다.

---

#### AI 프로젝트에서는

```text
def embed(text: str) -> list[float]:
```

처럼 작성합니다.

또는

```text
def search(query: str) -> list[Document]:
```

처럼 작성합니다.

코드만 읽어도

데이터 흐름이 보입니다.

---

#### ④ 실습 준비

프로젝트

```text
python-ai/

    typing/

        type_hint.py
```

추가 라이브러리

없음

---

#### ⑤ 기본 사용법

#### 변수

```python
name: str = "Kim"

age: int = 20

score: float = 95.5
```

---

#### 리스트

```python
numbers: list[int] = [1, 2, 3]
```

---

#### 딕셔너리

```python
scores: dict[str, int] = {

    "Kim": 90,

    "Lee": 85

}
```

---

#### 함수

```python
def add(a: int, b: int) -> int:

    return a + b
```

---

#### 객체

```python
class User:

    ...
```

사용

```python
def print_user(user: User):

    print(user)
```

---

#### AI 서비스 예제

Document

```python
from dataclasses import dataclass


@dataclass
class Document:

    text: str
```

검색

```python
def search(query: str) -> list[Document]:

    ...
```

Embedding

```python
def embed(text: str) -> list[float]:

    ...
```

LLM

```python
def generate(prompt: str) -> str:

    ...
```

이렇게 작성하면

IDE에서

자동완성도

훨씬 좋아집니다.

---

#### Generic이란?

이제 새로운 문제가 생깁니다.

예를 들어

```python
list[int]
```

도 있고

```python
list[str]
```

도 있습니다.

그런데

둘 다

리스트입니다.

타입만

달라집니다.

---

#### Generic의 정의

> **타입을 나중에 결정할 수 있도록 일반화하는 방법**

---

예를 들어

```text
Box
```

가 있다고 생각해 봅시다.

박스 안에는

```text
사과

책

노트북
```

모두 들어갈 수 있습니다.

박스는

같은 박스입니다.

내용물만 달라집니다.

---

Generic도

같은 개념입니다.

---

#### Generic 사용

```python
from typing import TypeVar

T = TypeVar("T")
```

---

Generic 함수

```python
def first(items: list[T]) -> T:

    return items[0]
```

사용

```python
first([1, 2, 3])
```

결과

```text
int
```

사용

```python
first(["A", "B"])
```

결과

```text
str
```

같은 함수가

여러 타입을

안전하게 사용할 수 있습니다.

---

#### Generic Class

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):

    def __init__(self, value: T):

        self.value = value
```

사용

```python
Box[int](10)

Box[str]("Hello")
```

---

#### AI 서비스 예제

예를 들어

API 응답

```python
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class ApiResponse(Generic[T]):

    success: bool

    data: T
```

사용

```python
ApiResponse[Document]

ApiResponse[User]

ApiResponse[list[Document]]
```

하나의 클래스로

모든 응답을 표현할 수 있습니다.

---

#### ⑥ 실무 활용

실무에서는

Type Hint를

거의 항상 사용합니다.

예를 들어

FastAPI

```text
def create_user(user: UserCreate) -> User:
```

---

LangChain

```text
def invoke(input: str) -> str:
```

---

OpenAI SDK

```text
def responses(...) -> Response:
```

거의 모든 최신 라이브러리가

Type Hint를 사용합니다.

---

#### Generic은 어디서 사용할까?

예를 들어

```text
Repository

Response

Cache

Queue

Event
```

같은

범용 객체를 만들 때

많이 사용합니다.

---

#### 실무 Best Practice

#### ① Type Hint는 반드시 작성한다.

AI 프로젝트에서는

거의 필수입니다.

---

#### ② 반환 타입도 작성한다.

좋지 않은 예

```text
def embed(text):
```

좋은 예

```text
def embed(text: str) -> list[float]:
```

---

#### ③ Generic은 정말 일반화가 필요할 때만 사용한다.

무조건 사용하는 것은

오히려

가독성을 떨어뜨릴 수 있습니다.

---

#### ⑦ 자주 발생하는 실수

#### 1. Type Hint가 타입 검사를 한다고 생각한다.

아닙니다.

실행에는

영향이 없습니다.

---

#### 2. 반환 타입을 생략한다.

```text
def search(query: str):
```

보다는

```text
def search(query: str) -> list[Document]:
```

가 훨씬 좋습니다.

---

#### 3. Generic을 남용한다.

복잡한 Generic은

오히려

읽기 어려워집니다.

필요한 곳에서만 사용합니다.

---

#### Type Hint vs 일반 Python

| 일반 Python         | Type Hint             |
| ------------------- | --------------------- |
| 타입이 보이지 않음  | 타입이 명확함         |
| IDE 지원 적음       | 자동완성 향상         |
| 협업 어려움         | 협업 쉬움             |
| 문서를 따로 봐야 함 | 코드만 봐도 이해 가능 |

---

#### ⑧ 핵심 내용 정리

이번 Unit의 핵심은 다음과 같습니다.

- **Type Hint는 타입 정보를 코드에 명시하여 가독성과 유지보수성을 높이는 기능**이다.
- 일반 Python 함수 호출에서 Type Hint는 **타입을 자동으로 강제하지 않으며**, IDE·정적 분석 도구·FastAPI 같은 Runtime Framework가 Annotation 정보를 활용할 수 있다.
- AI 프로젝트에서는 함수의 입력과 출력 타입을 명확히 표현하기 위해 적극적으로 사용한다.
- **Generic은 타입을 일반화하여 하나의 함수나 클래스를 여러 타입에 재사용할 수 있게 하는 기능**이다.
- FastAPI, Pydantic, LangChain 등 현대 Python 생태계에서는 Type Hint를 기반으로 다양한 기능을 제공하므로, 실무에서는 사실상 필수 기술이다.

---

#### Day 1-2. HTTP와 FastAPI 실행 구조

Python 준비를 마쳤으므로 이제 사용자 요청이 어떤 계약으로 서버에 전달되는지 확인합니다. FastAPI의 역할을 먼저 살펴보고 HTTP·REST, 비동기 I/O, ASGI·Uvicorn을 하나의 실행 흐름으로 연결합니다.

## Part 2-5. Dataclass와 Composition

### Module 27. Python 데이터 클래스(Data Class) - `@dataclass`

#### Module 실습 예제

- [예제 1: dataclass_basic.py](examples/module_27/dataclass_basic.py) — Data Class가 생성자·표현·비교를 자동 생성하는지 확인합니다.
- [예제 2: dataclass_result.py](examples/module_27/dataclass_result.py) — Service 내부 결과를 불변 Data Class로 표현합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- `@dataclass`는 왜 등장했는가?
- 일반 Class와 무엇이 다른가?
- 어떤 경우에 사용하는 것이 좋은가?
- AI 서비스에서는 어떤 객체를 Data Class로 만드는가?
- 언제 Data Class를 사용하면 안 되는가?

---

#### ① 문제 이해 (Why)

지금까지 우리는 Class를 만들 때 항상 비슷한 코드를 작성했습니다.

예를 들어 사용자 정보를 저장하는 클래스를 만들어 봅시다.

```python
class User:

    def __init__(self, name, age):

        self.name = name

        self.age = age
```

객체 생성

```python
user = User("Kim", 30)
```

여기까지는 괜찮습니다.

---

하지만 출력해 보면

```python
print(user)
```

결과는

```text
<__main__.User object at 0x103abc...>
```

입니다.

사람이 보기에는 거의 의미가 없습니다.

---

#### 객체 비교도 이상하다.

예를 들어

```python
user1 = User("Kim", 30)

user2 = User("Kim", 30)
```

비교

```python
print(user1 == user2)
```

결과

```text
False
```

왜일까요?

일반 클래스가 `__eq__()`를 정의하지 않으면 기본적으로
객체의 값이 아니라 **객체 동일성(Identity)** 을 기준으로 비교하기 때문입니다.

이는 `user1`과 `user2`가 같은 내용을 가지더라도 서로 다른 객체라는 뜻입니다.
여기서 Identity를 단순히 실제 메모리 주소와 완전히 같은 개념으로
외울 필요는 없습니다.

---

#### 보기 좋게 출력하려면?

우리는

```text
def __repr__(self):
```

를 만들어야 합니다.

---

#### 값 비교하려면?

```text
def __eq__(self):
```

를 만들어야 합니다.

---

#### 정렬하려면?

```python
__lt__()

__gt__()

__le__()
```

등을 만들어야 합니다.

---

#### 생성자도 만들고

```python
__init__()
```

도 만들어야 합니다.

---

즉,

데이터 하나 저장하려고

엄청난 양의

반복 코드가 생깁니다.

---

#### AI 서비스에서도 동일한 문제가 발생한다.

AI 프로젝트에는

데이터 객체가 매우 많습니다.

예를 들어

```text
User

Document

Chunk

Embedding

Prompt

ChatMessage

ModelConfig

OCRResult
```

이 객체들은

대부분

데이터만 저장합니다.

복잡한 기능은 거의 없습니다.

그런데

모든 클래스에서

```python
__init__()

__repr__()

__eq__()
```

를 반복해서 작성하고 있습니다.

---

#### 이것을 해결하는 것이 Data Class이다.

> **"데이터를 저장하는 클래스를 매우 간단하게 만들기 위한 기능"**

---

#### ② 개념 이해 (Concept)

Data Class는

Python 3.7부터 추가된 기능입니다.

모듈

```python
dataclasses
```

를 사용합니다.

---

#### 정의

> **데이터 저장을 목적으로 하는 클래스를 자동으로 생성해 주는 기능**

---

#### 자동으로 만들어 주는 것

```text
__init__()

↓

__repr__()

↓

__eq__()
```

필요하면

```text
__hash__()

↓

정렬 메서드

↓

기타 기능
```

도 자동 생성됩니다.

---

#### 일반 클래스와 비교

일반 클래스

```python
class User:

    def __init__(self, name, age):

        self.name = name

        self.age = age
```

---

Data Class

```python
from dataclasses import dataclass


@dataclass
class User:

    name: str

    age: int
```

끝입니다.

---

#### ③ 구조 이해 (Architecture)

Data Class는

실제로는

다음 코드를

자동으로 생성해 줍니다.

```text
def __init__(...)

def __repr__(...)

def __eq__(...)
```

즉,

우리가

직접 작성하지 않아도 됩니다.

---

#### 내부 구조

```text
@dataclass

↓

클래스 분석

↓

필드 분석

↓

자동 메서드 생성

↓

일반 클래스처럼 사용
```

---

#### ④ 실습 준비

프로젝트

```text
python-ai/

    oop/

        dataclass_example.py
```

추가 라이브러리

```python
from dataclasses import dataclass
```

---

#### ⑤ 기본 사용법

#### 가장 간단한 Data Class

```python
from dataclasses import dataclass


@dataclass
class User:

    name: str

    age: int
```

객체 생성

```python
user = User("Kim", 30)
```

---

#### 출력

```python
print(user)
```

결과

```text
User(name='Kim', age=30)
```

일반 클래스보다

훨씬 보기 좋습니다.

---

#### 비교

```python
user1 = User("Kim", 30)

user2 = User("Kim", 30)

print(user1 == user2)
```

결과

```text
True
```

Data Class는

데이터를 비교합니다.

---

#### 속성 접근

```python
print(user.name)
```

결과

```text
Kim
```

기존 클래스와

완전히 동일하게 사용할 수 있습니다.

---

#### AI 서비스 예제

문서 정보

```python
from dataclasses import dataclass


@dataclass
class Document:

    filename: str

    path: str

    size: int
```

생성

```python
doc = Document(

    "report.pdf",

    "/data/report.pdf",

    1024

)
```

출력

```text
Document(filename='report.pdf', path='/data/report.pdf', size=1024)
```

---

#### Embedding 정보

```python
from dataclasses import dataclass


@dataclass
class Embedding:

    text: str

    vector: list[float]
```

실무에서도

이런 형태를

매우 많이 사용합니다.

---

#### 기본값 지정

```python
from dataclasses import dataclass


@dataclass
class User:

    name: str

    age: int = 20
```

생성

```python
user = User("Kim")
```

결과

```text
User(name='Kim', age=20)
```

---

#### Mutable 기본값은 `default_factory`를 사용한다

각 객체가 독립적인 List나 Dictionary를 가져야 할 때는
`field(default_factory=...)`를 사용합니다.

```python
from dataclasses import dataclass, field


@dataclass
class Conversation:
    messages: list[str] = field(default_factory=list)
```

```python
first = Conversation()
second = Conversation()

first.messages.append("Hello")

print(first.messages)   # ['Hello']
print(second.messages)  # []
```

`messages: list[str] = []`처럼 Mutable 객체를 기본값으로 직접 두면
객체 사이에서 상태가 공유될 위험이 있습니다. `dataclass`는 일반적인
Mutable 기본값을 감지하면 `ValueError`를 발생시키므로 각 인스턴스마다
새 객체를 만드는 `default_factory`를 사용합니다.

---

#### ⑥ 실무 활용

AI 프로젝트에서는

다음과 같은 객체를

Data Class로 만드는 경우가 많습니다.

```text
ChatMessage

Prompt

Document

Chunk

Embedding

OCRResult

APIResponse

Config
```

예를 들어

Prompt

```python
from dataclasses import dataclass


@dataclass
class Prompt:

    role: str

    content: str
```

---

또는

OCR 결과

```python
@dataclass
class OCRResult:

    text: str

    confidence: float
```

---

#### 언제 사용하지 않을까?

다음과 같은 경우에는

일반 Class가 더 적합합니다.

```text
Database

ChatService

LLM

Retriever

VectorStore
```

이 클래스들은

기능이 많기 때문입니다.

---

즉,

```text
데이터 중심

↓

Data Class

----------------

행동 중심

↓

일반 Class
```

---

#### Data Class와 OOP

Data Class도

Class입니다.

즉,

```text
상속 가능

↓

메서드 추가 가능

↓

Property 사용 가능
```

모두 가능합니다.

---

예를 들어

```python
from dataclasses import dataclass


@dataclass
class User:

    first_name: str

    last_name: str


    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"
```

처럼

메서드도

자유롭게 추가할 수 있습니다.

---

#### 실무 Best Practice

#### ① DTO에는 Data Class

DTO(Data Transfer Object)

```text
User

Document

Prompt

Response
```

처럼 데이터 전달이 중심인 객체에는 Data Class를 우선 고려할 수 있습니다.

---

#### ② Service는 일반 Class

```text
ChatService

Retriever

EmbeddingService

OCRService
```

처럼 동작과 의존성 관리가 중심인 객체는 일반 Class로 시작하는 경우가 많습니다.

---

#### ③ 기능이 많아지면 일반 Class

Data Class가

만능은 아닙니다.

행동과 생명주기 관리가 중심이라면 일반 Class를 우선 고려합니다.
이는 강제 규칙이 아니라 설계를 시작하기 위한 판단 기준입니다.

---

#### ⑦ 자주 발생하는 실수

#### 1. 모든 클래스를 Data Class로 만든다.

서비스 클래스를 관성적으로 Data Class로 만들지 않습니다.
Data Class가 줄여 주는 반복 코드가 실제로 필요한지 먼저 판단합니다.

---

#### 2. Data Class에는 데이터만 있어야 한다고 생각한다.

메서드를

추가할 수 있습니다.

다만

데이터 중심이어야 합니다.

---

#### 3. `@dataclass`를 빼먹는다.

```text
class User:
```

이렇게 작성하면

자동 생성 기능을 사용할 수 없습니다.

---

#### 4. Mutable 객체를 기본값으로 직접 사용한다.

```python
from dataclasses import dataclass


@dataclass
class Conversation:
    messages: list[str] = []
```

List나 Dictionary처럼 변경 가능한 기본값은 `field(default_factory=list)`처럼
Factory를 사용하여 인스턴스마다 새 객체를 생성해야 합니다.

---

#### 일반 Class vs Data Class

| 일반 Class를 우선 고려 | Data Class를 우선 고려 |
| ---------------------- | ---------------------- |
| 기능 중심              | 데이터 중심            |
| 메서드가 많음          | 속성이 많음            |
| 직접 `__init__()` 작성 | 자동 생성              |
| 직접 `__repr__()` 작성 | 자동 생성              |
| 직접 `__eq__()` 작성   | 자동 생성              |

---

#### ⑧ 핵심 내용 정리

이번 Unit의 핵심은 다음과 같습니다.

- **`@dataclass`는 데이터 저장을 위한 클래스를 간결하게 작성하기 위한 기능**이다.
- `__init__()`, `__repr__()`, `__eq__()` 등을 자동으로 생성하여 반복 코드를 크게 줄여 준다.

- List나 Dictionary 같은 Mutable 기본값에는 `field(default_factory=...)`를 사용한다.
- Data Class는 **데이터 중심 객체(DTO, 설정 객체, 응답 객체 등)** 의 반복 코드를 줄이는 데 특히 유용하다.
- 서비스처럼 **행동(Behavior)과 생명주기 관리가 중심인 객체**는 일반 클래스로 시작하는 경우가 많다. 이는 강제 규칙이 아니라 설계 기준이다.
- AI 프로젝트에서는 `Document`, `Prompt`, `Embedding`, `ChatMessage`, `OCRResult`, `Config` 등의 객체에 매우 자주 활용된다.

---

### Module 28. Composition(합성) vs Inheritance(상속)

#### Module 실습 예제

- [예제 1: composition_basic.py](examples/module_28/composition_basic.py) — 상속 대신 필요한 객체를 속성으로 전달합니다.
- [예제 2: provider_injection.py](examples/module_28/provider_injection.py) — Service에 AI Client를 합성하여 구현을 교체합니다.

#### 이번 학습 목표

이번 Unit이 끝나면 다음 질문에 자신의 언어로 답할 수 있어야 합니다.

- 상속(Inheritance)과 합성(Composition)은 무엇이 다른가?
- 언제 상속을 사용하고 언제 합성을 사용하는가?
- 실무에서는 왜 "Composition over Inheritance"라는 말을 많이 하는가?
- AI 서비스에서는 어떤 설계가 더 많이 사용되는가?

---

#### ① 문제 이해 (Why)

이 과정에서는 Class와 Object, 그리고 기본 상속 관계를 학습했습니다.

이제 FastAPI의 Service가 AI Client와 같은 협력 객체를 사용하는 구조로 넘어가기 전에,
상속과 합성의 차이를 비교합니다.

상속은 기존 Class의 기능을 물려받는 관계이고,
합성은 필요한 객체를 속성으로 전달받아 사용하는 관계입니다.

AI Backend에서는 Provider와 Service를 쉽게 교체하고 테스트하기 위해
상속보다 합성을 사용하는 경우가 많습니다.

---

#### 상속은 정말 모든 문제를 해결할까?

예를 들어

자동차를 만들어 봅시다.

자동차에는

```text
Engine

Wheel

Brake
```

가 있습니다.

그러면

다음처럼 만들까요?

```python
class Engine:
    ...

class Car(Engine):
    ...
```

이상합니다.

자동차는

엔진이 아닙니다.

자동차는

엔진을

**가지고 있습니다.**

---

#### 현실에서는

```text
Car

↓

Engine
```

가 아니라

```text
Car

↓

has Engine
```

입니다.

이것이

Composition입니다.

---

#### AI 서비스에서도 마찬가지이다.

예를 들어

RAG 서비스를 생각해봅시다.

```text
ChatService
```

안에는

```text
LLM

Embedding

VectorDB

Retriever

PromptBuilder
```

가 존재합니다.

그러면

```text
class ChatService(LLM):
```

일까요?

아닙니다.

ChatService는

LLM이 아닙니다.

LLM을

사용하는 것입니다.

---

#### 이것이 Composition이다.

```text
ChatService

has

LLM

Embedding

VectorDB
```

---

#### 객체 사이에는 두 가지 관계가 있다.

객체지향에서는

가장 중요한 관계가 두 개 있습니다.

#### is-a 관계

```text
Dog

↓

Animal
```

강아지는

동물입니다.

이럴 때는

상속을 사용합니다.

---

#### has-a 관계

```text
Car

↓

Engine
```

자동차는

엔진을 가지고 있습니다.

이럴 때는

Composition을 사용합니다.

---

#### ② 개념 이해 (Concept)

#### 상속(Inheritance)

> **객체가 다른 객체의 종류일 때 사용하는 관계**

예를 들어

```text
Cat

↓

Animal
```

Cat은

Animal입니다.

---

#### Composition

> **객체가 다른 객체를 포함하여 사용하는 관계**

예를 들어

```text
Car

↓

Engine
```

Car는

Engine이 아닙니다.

Engine을

사용합니다.

---

#### 비교

```text
Inheritance

is-a

"~이다"

--------------------

Composition

has-a

"~을 가지고 있다"
```

---

#### ③ 구조 이해 (Architecture)

#### 상속

```text
Animal

├── Dog

├── Cat

└── Bird
```

---

#### Composition

```text
Car

├── Engine

├── Wheel

├── Brake

└── Navigation
```

---

#### AI 서비스 구조

실제 AI 서비스는

거의 항상

다음과 같습니다.

```text
ChatService

├── LLM

├── Embedding

├── VectorStore

├── Retriever

└── PromptBuilder
```

이들은

상속 관계가 아니라

Composition 관계입니다.

---

#### 데이터 흐름

```text
User

↓

ChatService

↓

Retriever

↓

VectorDB

↓

LLM

↓

Response
```

ChatService는

각 객체를

조합하여

서비스를 만듭니다.

---

#### ④ 실습 준비

프로젝트

```text
python-ai/

    oop/

        composition.py
```

---

#### ⑤ 기본 사용법

#### 상속 예제

```python
class Animal:

    def eat(self):

        print("먹는다.")


class Dog(Animal):

    pass
```

Dog는

Animal입니다.

---

#### Composition 예제

먼저

Engine

```python
class Engine:

    def start(self):

        print("엔진 시작")
```

자동차

```python
class Car:

    def __init__(self):

        self.engine = Engine()
```

사용

```python
car = Car()

car.engine.start()
```

출력

```text
엔진 시작
```

여기서

Car는

Engine을

상속받지 않았습니다.

객체를

가지고 있을 뿐입니다.

---

#### AI 서비스 예제

LLM

```python
class LLM:

    def generate(self):

        print("답변 생성")
```

VectorDB

```python
class VectorDB:

    def search(self):

        print("문서 검색")
```

ChatService

```python
class ChatService:

    def __init__(self):

        self.llm = LLM()

        self.vector_db = VectorDB()
```

사용

```python
service = ChatService()

service.vector_db.search()

service.llm.generate()
```

---

#### 조금 더 실무답게 작성하면

```python
class ChatService:

    def __init__(self):

        self.vector_db = VectorDB()

        self.llm = LLM()


    def chat(self):

        self.vector_db.search()

        self.llm.generate()
```

서비스 사용자는

```python
service.chat()
```

만 호출합니다.

내부에서는

여러 객체가

협력하여

동작합니다.

---

#### ⑥ 실무 활용

실무에서는

Composition이 훨씬 많이 등장합니다.

예를 들어

```text
FastAPI App

↓

Router

↓

Service

↓

Repository

↓

Database
```

모두

Composition입니다.

---

또는

```text
RAGService

↓

Retriever

↓

Embedding

↓

VectorStore

↓

LLM
```

역시

Composition입니다.

---

또는

```text
DocumentPipeline

↓

OCR

↓

Parser

↓

Chunker

↓

Embedding

↓

VectorDB
```

모두

Composition입니다.

---

#### 왜 Composition을 더 많이 사용할까?

예를 들어

LLM을

GPT에서

Claude로

교체한다고 생각해봅시다.

Composition이라면

```python
self.llm = ClaudeModel()
```

만 바꾸면 됩니다.

상속 구조보다

훨씬 유연합니다.

---

#### 의존성 주입(DI)과도 잘 어울린다.

나중에 FastAPI에서 배우겠지만

```python
class ChatService:

    def __init__(self, llm):

        self.llm = llm
```

이처럼

외부에서 객체를 전달받는

**의존성 주입(Dependency Injection)** 도

Composition을 기반으로 합니다.

---

#### 실무 Best Practice

#### ① is-a 관계라면 상속

예를 들어

```text
PDFDocument

↓

Document
```

---

#### ② has-a 관계라면 Composition

예를 들어

```text
ChatService

↓

LLM
```

---

#### ③ 억지 상속은 피한다.

예를 들어

```text
class ChatService(LLM):
```

는

잘못된 설계입니다.

---

#### ④ 여러 기능을 조합하여 서비스를 만든다.

AI 서비스는

대부분

여러 객체가

협력하여 동작합니다.

즉,

Composition이

자연스럽습니다.

---

#### Composition over Inheritance

실무에서 자주 듣는 말입니다.

> **"가능하면 상속보다 합성을 우선하라."**

왜냐하면

Composition은

- 결합도가 낮고
- 교체가 쉽고
- 테스트가 쉽고
- 유지보수가 쉽기 때문입니다.

물론

상속이 나쁘다는 뜻은 아닙니다.

진짜

부모-자식 관계라면

상속이 가장 좋은 선택입니다.

---

#### ⑦ 자주 발생하는 실수

#### 1. 코드 재사용만을 위해 상속을 사용한다.

상속은

코드 재사용 도구가 아니라

**관계를 표현하는 도구**입니다.

---

#### 2. has-a 관계인데 상속을 사용한다.

예를 들어

```text
class ChatService(LLM):
```

는

좋지 않은 설계입니다.

---

#### 3. Composition인데 객체를 직접 생성한다.

```python
self.llm = GPTModel()
```

이렇게 하면

나중에 교체가 어렵습니다.

실무에서는

외부에서 주입받는 경우가 많습니다.

(다음 Phase에서 자세히 배웁니다.)

---

#### ⑧ 핵심 내용 정리

이번 Unit의 핵심은 다음과 같습니다.

- **상속(Inheritance)은 "is-a(~이다)" 관계를 표현**할 때 사용한다.
- **Composition(합성)은 "has-a(~을 가지고 있다)" 관계를 표현**할 때 사용한다.
- AI 서비스는 여러 컴포넌트가 협력하는 구조이므로 Composition을 훨씬 많이 사용한다.
- Composition은 객체를 쉽게 교체할 수 있어 확장성과 유지보수성이 뛰어나다.
- 객체지향 설계에서는 **"Composition over Inheritance"** 가 널리 권장되는 원칙이다.

---

#### Day 2-2. AI Backend Architecture

Request Pipeline 안에 Business Logic을 계속 작성하면 Router가 비대해집니다. 이제 Service Layer로 책임을 이동하고, APIRouter·Layered Architecture·Dependency Injection·Settings·Exception Handling을 연결합니다.

---

# Part 3. FastAPI로 넘어가기 전 연결 정리

## Python 코드가 Backend 코드로 바뀌는 과정

다음 Python 코드는 단순 함수이다.

```python
def summarize(text: str) -> str:
    return text[:100]
```

FastAPI에서는 이 함수가 사라지는 것이 아니다. HTTP 요청을 받는 Endpoint 뒤에서 그대로 호출되는 **업무 로직**이 된다.

```text
HTTP Request
    ↓
FastAPI Endpoint
    ↓
Python Function / Service
    ↓
Python Object / Collection
    ↓
JSON Response
```

따라서 다음 과목에서 새로운 언어를 배우는 것이 아니다. **Python 코드 앞에 HTTP 입구를 붙이고, 데이터 계약과 서버 실행 구조를 추가하는 것**이 FastAPI 학습의 핵심이다.

## 중간 확인

다음 질문을 자신의 말로 설명할 수 있는지 확인한다.

1. `a = [1, 2]`, `b = a`에서 `a`와 `b`는 왜 같은 List를 바라보는가?
2. List와 Tuple은 어떤 기준으로 선택하는가?
3. Dictionary가 JSON과 비슷해 보이지만 같은 개념은 아닌 이유는 무엇인가?
4. 함수의 Type Hint는 Python이 항상 Runtime에서 강제하는가?
5. Class와 Object의 차이는 무엇인가?
6. Inheritance와 Composition 중 Composition이 더 적절한 경우는 언제인가?
7. Decorator는 원래 함수를 직접 수정하지 않고 어떻게 기능을 추가하는가?
8. `try/except`는 모든 예외를 숨기기 위해 사용하는가?
9. 파일을 열 때 `with`를 사용하는 이유는 무엇인가?
10. Backend 개발에서 Python의 Collection과 함수가 어떤 위치에서 사용되는가?

## 실무 팁

- Python 문법을 짧게 쓰는 것보다 **다른 사람이 바로 이해할 수 있는 코드**를 우선한다.
- Dictionary의 Key 문자열을 프로젝트 전체에서 제각각 만들기 시작하면 오류가 늘어난다. 이후 FastAPI에서는 Pydantic Model로 데이터 계약을 명확히 만든다.
- Mutable 객체를 함수 인자로 전달할 때 원본이 변경되는지 항상 의식한다.
- 예외는 무조건 잡는 것이 아니라 **처리할 수 있는 계층에서만 처리**한다.
- Type Hint는 문서 역할뿐 아니라 IDE, 정적 분석, FastAPI/Pydantic과 연결되는 중요한 계약 정보다.
- AI 서비스의 Prompt, Request, Response도 결국 문자열·List·Dictionary·객체의 조합이라는 점을 기억한다.

## 주의사항

- `=`를 "복사"라고 단정하지 않는다. Python에서 이름은 객체를 참조한다.
- `{}`는 빈 Set이 아니라 빈 Dictionary다. 빈 Set은 `set()`으로 만든다.
- `except Exception:`으로 모든 오류를 조용히 삼키는 코드는 피한다.
- 전역 Mutable 객체에 애플리케이션 상태를 무분별하게 저장하지 않는다.
- API Key와 Secret을 Python 소스 코드에 직접 작성하지 않는다. 환경 설정은 FastAPI 과정에서 별도로 다룬다.

## 참고자료

- Python 공식 문서: https://docs.python.org/3/
- Python Downloads: https://www.python.org/downloads/
- PyTorch macOS 설치: https://pytorch.org/get-started/locally/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Data Model: https://docs.python.org/3/reference/datamodel.html
- `typing`: https://docs.python.org/3/library/typing.html
- `dataclasses`: https://docs.python.org/3/library/dataclasses.html

## 관련 Wiki Link

[[AI 애플리케이션 아키텍처]]  
[[React]]  
[[Python]]  
[[Object]]  
[[Collection]]  
[[Type Hint]]  
[[JSON]]  
[[Decorator]]  
[[OOP]]  
[[FastAPI]]  
[[Pydantic]]

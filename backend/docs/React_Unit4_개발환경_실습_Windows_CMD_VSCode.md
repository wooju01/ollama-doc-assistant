# React Unit 4 실습 — Windows React 개발환경 구성
## Node.js · npm · Vite · VS Code

> 대상: React 개발환경을 처음 구성하는 학습자  
> 운영체제: Windows 10 / Windows 11  
> 기준 강의: `React_강의용` — `Unit 4. React 개발환경 (Node.js, npm, Vite)`

---

# 1. 실습 목표

이 실습을 완료하면 다음 작업을 직접 수행할 수 있어야 한다.

- Node.js를 Windows에 설치할 수 있다.
- `node`와 `npm`이 정상적으로 설치되었는지 확인할 수 있다.
- Windows PowerShell의 실행 정책을 설정할 수 있다.
- Vite를 이용해 React 프로젝트를 생성할 수 있다.
- React 개발 서버를 실행할 수 있다.
- Browser에서 React 기본 화면을 확인할 수 있다.
- VS Code에서 React 프로젝트를 열고 Terminal을 사용할 수 있다.
- `npm run build`를 실행해 Production Build가 가능한지 확인할 수 있다.

---

# 2. 실습 기준 환경

이번 실습은 다음 환경을 기준으로 한다.

```text
Windows 10 / Windows 11
Node.js 24 LTS 계열
npm
Vite 8 계열
React 19 계열
VS Code
```

정확한 Patch Version은 설치 시점에 따라 달라질 수 있다.

설치가 끝난 뒤 다음 명령으로 실제 Version을 확인한다.

```bash
node --version
npm --version
```

React와 Vite의 정확한 Version은 프로젝트 생성 후 `package.json`과 `package-lock.json`에서 확인한다.

---

# 3. 먼저 알아둘 관계

이번 실습에서 사용하는 도구의 관계는 다음과 같다.

```text
Windows
  ↓
Node.js
  ↓
npm
  ↓
Vite
  ↓
React Project
  ↓
Browser
```

각 도구의 역할은 다음과 같다.

### Node.js

브라우저 밖에서 JavaScript를 실행할 수 있는 Runtime이다.

이번 수업에서는 다음 작업의 기반으로 사용한다.

```text
npm 실행
Vite 실행
Package 설치
개발 서버 실행
Production Build
```

### npm

Node.js 생태계의 Package Manager다.

다음과 같은 작업을 수행한다.

```text
Package 설치
Project Script 실행
Dependency 관리
```

### Vite

React 프로젝트의 개발 환경을 제공하는 Frontend 개발 도구다.

이번 실습에서는 다음 작업에 사용한다.

```text
React Project 생성
개발 Server 실행
빠른 개발 중 갱신
Production Build
```

### VS Code

Source Code를 작성하고 Terminal을 함께 사용할 수 있는 Code Editor다.

---

# 4. 매우 중요 — Windows PowerShell 실행 정책

Windows에서 React 실습을 진행할 때 다음과 같은 오류를 만날 수 있다.

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system
```

또는 비슷한 형태의 PowerShell Script 실행 오류가 발생할 수 있다.

이 경우 현재 사용자 계정의 PowerShell 실행 정책을 설정한다.

> **이 단계는 이번 Windows 개발환경 실습에서 반드시 수행한다.**

PowerShell에서 다음 명령을 실행한다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

확인 질문이 나오면 다음과 같이 입력한다.

```text
Y
```

또는 환경에 따라:

```text
A
```

를 선택할 수 있다.

설정 결과를 확인한다.

```powershell
Get-ExecutionPolicy -Scope CurrentUser
```

예상 결과:

```text
RemoteSigned
```

## 왜 `CurrentUser`를 사용하는가?

```text
CurrentUser
→ 현재 Windows 사용자 계정에만 적용
```

되기 때문이다.

따라서 일반적으로:

```text
관리자 권한으로 전체 PC 정책 변경
```

보다 교육용 개인 개발환경에서는 범위를 작게 유지할 수 있다.

## 주의

회사·학교 PC에서 Group Policy가 적용되어 있다면 위 명령이 다른 정책에 의해 제한될 수 있다.

그 경우 다음 명령으로 전체 정책을 확인한다.

```powershell
Get-ExecutionPolicy -List
```

회사나 학교가 관리하는 PC에서는 보안 정책을 임의로 우회하지 말고 관리자에게 문의한다.

---

# Part 1. Windows CMD에서 React 프로젝트 생성

---

# 5. 실습 1 — Windows CMD 방식

이 방법에서는 다음 순서로 진행한다.

```text
Node.js Download
↓
Node.js 설치
↓
PowerShell 실행 정책 설정
↓
CMD 실행
↓
Node.js / npm 확인
↓
작업 Folder 이동
↓
Vite React Project 생성
↓
Package 설치
↓
개발 Server 실행
↓
Browser 확인
↓
Production Build 확인
```

---

# 6. Step 1 — Node.js 다운로드

Browser를 실행한다.

Node.js 공식 Download 페이지에 접속한다.

```text
https://nodejs.org/en/download
```

이번 강의에서는 **Node.js 24 LTS 계열**을 사용한다.

Windows PC가 일반적인 Intel/AMD 64-bit 환경이라면 Windows x64 Installer를 사용한다.

예:

```text
Windows
x64
Installer (.msi)
```

Windows on ARM 장비라면 자신의 PC Architecture에 맞는 Installer를 선택한다.

---

# 7. Step 2 — Node.js 설치

다운로드한 `.msi` Installer를 실행한다.

기본적으로 다음 순서로 진행한다.

```text
Next
↓
License 확인
↓
설치 경로 확인
↓
Node.js Runtime
npm Package Manager
PATH 등록
↓
Install
↓
Finish
```

초보자는 특별한 이유가 없다면 기본 설치 옵션을 유지한다.

Node.js를 설치하면 npm도 함께 설치된다.

설치가 끝난 뒤 **기존 CMD가 열려 있었다면 닫고 새로 실행한다.**

환경변수 `PATH` 변경이 기존 Terminal에 바로 반영되지 않을 수 있기 때문이다.

---

# 8. Step 3 — PowerShell 실행 정책 설정

> **중요: 이 명령은 CMD 명령이 아니라 PowerShell 명령이다.**

CMD 방식으로 React 프로젝트를 생성하더라도 앞으로 VS Code의 PowerShell Terminal을 사용할 수 있으므로 이 단계에서 설정한다.

Windows 시작 메뉴를 연다.

```text
PowerShell
```

을 검색해 **Windows PowerShell 또는 PowerShell을 일반 사용자 권한으로 실행**한다.

다음 명령을 그대로 입력한다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

확인 메시지가 나오면:

```text
Y
```

를 입력한다.

그다음 확인한다.

```powershell
Get-ExecutionPolicy -Scope CurrentUser
```

예상 결과:

```text
RemoteSigned
```

설정이 끝났으면 PowerShell을 닫아도 된다.

---

# 9. Step 4 — Windows CMD 실행

다음 방법 중 하나로 CMD를 실행한다.

### 방법 A

```text
Windows 키
↓
cmd 입력
↓
명령 프롬프트 실행
```

### 방법 B

```text
Windows + R
↓
cmd
↓
Enter
```

CMD가 열리면 다음과 비슷한 Prompt가 보인다.

```text
C:\Users\student>
```

---

# 10. Step 5 — Node.js 설치 확인

CMD에서 실행한다.

```cmd
node --version
```

예상 형태:

```text
v24.x.x
```

다음으로 npm을 확인한다.

```cmd
npm --version
```

숫자가 출력되면 Node.js와 npm이 정상적으로 설치된 것이다.

예:

```text
11.x.x
```

> Version 숫자는 설치 시점에 따라 달라질 수 있다.

---

# 11. Step 6 — 실습 Project를 저장할 Folder 만들기

이번 실습에서는 Windows 사용자 Folder 아래에 `projects` Folder를 만든다.

CMD에서 실행한다.

```cmd
cd /d %USERPROFILE%
```

현재 위치 확인:

```cmd
cd
```

예:

```text
C:\Users\student
```

`projects` Folder를 생성한다.

```cmd
mkdir projects
```

이미 Folder가 있다면 생성 명령은 생략한다.

Folder로 이동한다.

```cmd
cd projects
```

현재 위치를 다시 확인한다.

```cmd
cd
```

예상:

```text
C:\Users\student\projects
```

---

# 12. Step 7 — Vite React 프로젝트 생성

다음 명령을 실행한다.

```cmd
npm create vite@latest react-ai-app -- --template react
```

명령을 나누어 보면 다음과 같다.

```text
npm
└─ npm 실행

create vite@latest
└─ Vite Project 생성 Tool 실행

react-ai-app
└─ 생성할 Project Folder 이름

--template react
└─ React JavaScript Template 사용
```

처음 실행할 때 npm이 `create-vite` Package 설치 여부를 묻는 경우가 있다.

예:

```text
Need to install the following packages:
create-vite@...
Ok to proceed? (y)
```

이 경우:

```text
y
```

를 입력하고 Enter를 누른다.

프로젝트 생성이 완료되면 현재 Folder 아래에 다음 Folder가 만들어진다.

```text
react-ai-app
```

---

# 13. Step 8 — 생성된 Project Folder로 이동

```cmd
cd react-ai-app
```

현재 위치를 확인한다.

```cmd
cd
```

예상:

```text
C:\Users\student\projects\react-ai-app
```

---

# 14. Step 9 — 프로젝트 파일 확인

다음 명령을 실행한다.

```cmd
dir
```

대략 다음 파일과 Folder를 확인할 수 있다.

```text
src
public
index.html
package.json
vite.config.js
```

Vite Version이나 Template 변경에 따라 일부 파일 구성은 달라질 수 있다.

---

# 15. Step 10 — Package 설치

다음 명령을 실행한다.

```cmd
npm install
```

이 명령은 `package.json`에 정의된 Dependency를 설치한다.

설치가 완료되면 다음 Folder가 생성된다.

```text
node_modules
```

그리고 일반적으로 다음 파일도 확인할 수 있다.

```text
package-lock.json
```

`package-lock.json`은 실제로 설치된 Package Version을 재현하는 데 중요한 파일이다.

---

# 16. Step 11 — React 개발 Server 실행

다음 명령을 실행한다.

```cmd
npm run dev
```

정상적으로 실행되면 Vite가 Local 주소를 출력한다.

예:

```text
Local: http://localhost:5173/
```

Port가 이미 사용 중이면 다음과 같이 다른 Port가 사용될 수 있다.

```text
http://localhost:5174/
```

따라서 **항상 Terminal에 실제로 출력된 주소를 확인한다.**

---

# 17. Step 12 — Browser에서 확인

Browser를 열고 Terminal에 출력된 주소로 이동한다.

예:

```text
http://localhost:5173/
```

Vite + React 기본 화면이 나타나면 성공이다.

---

# 18. Step 13 — 개발 Server 종료

CMD에서:

```text
Ctrl + C
```

를 누른다.

환경에 따라 종료 확인이 나타나면:

```text
Y
```

를 입력한다.

---

# 19. Step 14 — Production Build 확인

개발 Server를 종료한 뒤 다음 명령을 실행한다.

```cmd
npm run build
```

정상적으로 Build되면 일반적으로:

```text
dist
```

Folder가 생성된다.

즉:

```text
Source Code
↓
Vite Build
↓
dist
```

흐름을 확인할 수 있다.

---

# 20. CMD 방식 전체 명령 요약

PowerShell에서 한 번 실행:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

확인:

```powershell
Get-ExecutionPolicy -Scope CurrentUser
```

CMD:

```cmd
node --version
npm --version

cd /d %USERPROFILE%
mkdir projects
cd projects

npm create vite@latest react-ai-app -- --template react

cd react-ai-app

npm install
npm run dev
```

Build:

```cmd
npm run build
```

---

# Part 2. VS Code에서 React 프로젝트 생성

---

# 21. 실습 2 — VS Code 방식

이 방법에서는 다음 순서로 진행한다.

```text
Node.js Download
↓
Node.js 설치
↓
VS Code Download
↓
VS Code 설치
↓
VS Code 실행
↓
PowerShell Terminal 실행
↓
PowerShell 실행 정책 설정
↓
Node.js / npm 확인
↓
작업 Folder 준비
↓
Vite React Project 생성
↓
Project Open
↓
Package 설치
↓
개발 Server 실행
↓
Source 수정
↓
Browser 확인
↓
Production Build 확인
```

---

# 22. Step 1 — Node.js 다운로드

Node.js 공식 Download 페이지에 접속한다.

```text
https://nodejs.org/en/download
```

이번 강의에서는:

```text
Node.js 24 LTS 계열
```

을 사용한다.

Windows x64 PC라면 일반적으로 Windows x64 Installer `.msi`를 사용한다.

---

# 23. Step 2 — Node.js 설치

Installer를 실행하고 기본 설정으로 설치한다.

설치 항목에서 다음이 포함되어 있는지 확인한다.

```text
Node.js Runtime
npm Package Manager
PATH 등록
```

설치 완료 후 이미 VS Code가 실행 중이었다면 **VS Code를 완전히 종료했다가 다시 실행하는 것을 권장한다.**

Node.js 설치 전에 실행된 VS Code가 변경된 PATH를 아직 인식하지 못할 수 있기 때문이다.

---

# 24. Step 3 — VS Code 다운로드

VS Code 공식 Download 페이지에 접속한다.

```text
https://code.visualstudio.com/Download
```

Windows에서 일반적인 개인 실습 PC라면:

```text
Windows
User Installer
x64
```

를 사용할 수 있다.

Microsoft 공식 문서에서도 대부분의 개인 사용자는 `User setup`을 사용할 수 있으며 관리자 권한 없이 설치할 수 있다고 안내한다.

ARM Windows 장비라면 자신의 Architecture에 맞는 Version을 선택한다.

---

# 25. Step 4 — VS Code 설치

다운로드한 VS Code Installer를 실행한다.

설치 과정에서 다음 항목이 보이면 사용하는 것을 권장한다.

```text
PATH에 추가
Explorer Context Menu에 Code로 열기 추가
지원되는 파일 형식의 Editor로 등록
```

설치 옵션의 표현은 Version에 따라 조금 달라질 수 있다.

설치 완료 후 VS Code를 실행한다.

---

# 26. Step 5 — VS Code Terminal 열기

VS Code 상단 Menu:

```text
Terminal
↓
New Terminal
```

을 선택한다.

단축키를 사용할 수도 있다.

```text
Ctrl + `
```

Windows의 VS Code에서는 기본 Terminal Profile이 PowerShell인 경우가 많다.

Terminal Prompt 예:

```text
PS C:\Users\student>
```

앞에:

```text
PS
```

가 보이면 PowerShell이다.

---

# 27. Step 6 — PowerShell 실행 정책 설정

> **이 단계를 생략하지 않는다.**

VS Code Terminal이 PowerShell인 상태에서 다음 명령을 그대로 실행한다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

확인 질문이 나오면:

```text
Y
```

를 입력한다.

설정을 확인한다.

```powershell
Get-ExecutionPolicy -Scope CurrentUser
```

예상 결과:

```text
RemoteSigned
```

이 설정은 현재 Windows 사용자 계정에 대해 저장되므로 일반적으로 매번 다시 실행할 필요는 없다.

---

# 28. Step 7 — Node.js와 npm 확인

VS Code Terminal에서:

```powershell
node --version
```

실행.

예:

```text
v24.x.x
```

다음:

```powershell
npm --version
```

숫자가 출력되면 정상이다.

---

# 29. Step 8 — 작업 Folder 준비

VS Code Terminal에서 Windows 사용자 Home으로 이동한다.

```powershell
cd $HOME
```

`projects` Folder가 없다면 생성한다.

```powershell
mkdir projects
```

이미 Folder가 존재한다면 다음과 같은 메시지가 나올 수 있다.

이 경우 새로 만들 필요가 없으므로 이동만 한다.

```powershell
cd projects
```

현재 위치를 확인한다.

```powershell
Get-Location
```

예:

```text
C:\Users\student\projects
```

---

# 30. Step 9 — Vite React 프로젝트 생성

VS Code Terminal에서 실행한다.

```powershell
npm create vite@latest react-ai-app -- --template react
```

처음 실행 시 `create-vite` 설치 여부를 묻는 경우:

```text
Ok to proceed? (y)
```

다음 입력:

```text
y
```

프로젝트가 생성될 때까지 기다린다.

---

# 31. Step 10 — React Project를 VS Code에서 열기

현재 VS Code가 `projects` 상위 Folder를 열고 있다면 왼쪽 Explorer에 다음 Folder가 나타날 수 있다.

```text
react-ai-app
```

프로젝트 자체를 VS Code Workspace Root로 여는 것을 권장한다.

VS Code Menu:

```text
File
↓
Open Folder...
↓
react-ai-app 선택
```

또는 Terminal에서 다음 명령을 사용할 수도 있다.

```powershell
code react-ai-app
```

`code` 명령이 바로 실행되지 않는다면 VS Code를 종료한 뒤 다시 실행하거나 `File → Open Folder` 방식을 사용한다.

---

# 32. Step 11 — Project Folder 확인

프로젝트를 열면 왼쪽 Explorer에서 다음과 비슷한 구조를 확인한다.

```text
react-ai-app
├─ public
├─ src
├─ index.html
├─ package.json
└─ vite.config.js
```

Version에 따라 일부 파일 구성은 달라질 수 있다.

---

# 33. Step 12 — VS Code Terminal 위치 확인

새 Terminal을 연다.

```text
Terminal
↓
New Terminal
```

현재 Prompt가 Project Root인지 확인한다.

예:

```text
PS C:\Users\student\projects\react-ai-app>
```

다른 위치라면 이동한다.

```powershell
cd $HOME\projects\react-ai-app
```

---

# 34. Step 13 — Package 설치

```powershell
npm install
```

설치가 끝나면:

```text
node_modules
package-lock.json
```

을 확인한다.

---

# 35. Step 14 — React 개발 Server 실행

```powershell
npm run dev
```

정상 실행 예:

```text
Local: http://localhost:5173/
```

VS Code Terminal에 출력된 실제 URL을 `Ctrl`을 누른 상태에서 Click하면 Browser로 열 수 있는 경우도 있다.

또는 Browser 주소창에 직접 입력한다.

---

# 36. Step 15 — Browser에서 기본 화면 확인

예:

```text
http://localhost:5173/
```

Vite + React 기본 화면이 보이는지 확인한다.

---

# 37. Step 16 — React 화면 직접 수정

VS Code Explorer에서 다음 파일을 연다.

```text
src/App.jsx
```

기존 내용을 지우고 다음과 같이 작성한다.

```jsx
function App() {
  return (
    <main>
      <h1>React 개발환경 구성 완료</h1>
      <p>Vite 개발 서버가 정상적으로 실행되고 있습니다.</p>
    </main>
  )
}

export default App
```

파일을 저장한다.

```text
Ctrl + S
```

Browser 화면이 자동으로 변경되는지 확인한다.

이것이 Vite 개발환경의 빠른 갱신 기능을 직접 확인하는 단계다.

---

# 38. Step 17 — 개발 Server 종료

VS Code Terminal을 선택한다.

```text
Ctrl + C
```

를 누른다.

---

# 39. Step 18 — Production Build 확인

Terminal에서 실행한다.

```powershell
npm run build
```

정상적으로 Build되면 Explorer에서:

```text
dist
```

Folder를 확인한다.

---

# 40. VS Code 방식 전체 명령 요약

VS Code PowerShell Terminal:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Get-ExecutionPolicy -Scope CurrentUser

node --version
npm --version

cd $HOME
mkdir projects
cd projects

npm create vite@latest react-ai-app -- --template react
```

Project Folder를 연 뒤:

```powershell
npm install
npm run dev
```

Build 확인:

```powershell
npm run build
```

---

# 41. CMD와 VS Code 방식의 차이

두 방법 모두 최종적으로 같은 React 프로젝트를 만든다.

차이는 **명령을 어디에서 실행하고 Code를 어디에서 편집하는가**이다.

| 구분 | CMD 방식 | VS Code 방식 |
|---|---|---|
| 명령 실행 | Windows CMD | VS Code Integrated Terminal |
| 기본 Shell | cmd.exe | Windows에서는 보통 PowerShell |
| Source 편집 | 별도 Editor 필요 | VS Code에서 바로 편집 |
| Folder 확인 | `dir` | Explorer |
| 개발 Server | `npm run dev` | `npm run dev` |
| React Project 결과 | 동일 | 동일 |
| 추천 | Terminal 기본 원리 확인 | 실제 수업·개발 작업 |

수업에서는 둘 다 경험해보는 것이 좋다.

CMD 방식에서는:

```text
Folder 이동
Command
Process
```

개념을 익히고,

VS Code 방식에서는:

```text
Code Editor
+
Terminal
+
Project Explorer
```

를 한 환경에서 사용하는 실제 개발 방식을 익힐 수 있다.

---

# 42. 오류 해결

## 오류 1 — `node`를 찾을 수 없음

예:

```text
'node' is not recognized as an internal or external command
```

확인:

```text
Node.js 설치 여부
PATH 등록 여부
Terminal 재시작 여부
```

Node.js 설치 후 열려 있던 CMD나 VS Code를 완전히 종료한 뒤 다시 실행한다.

---

## 오류 2 — `npm.ps1` 실행 불가

예:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system
```

PowerShell에서 반드시 다음 명령을 실행한다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

확인:

```powershell
Get-ExecutionPolicy -Scope CurrentUser
```

결과:

```text
RemoteSigned
```

이어야 한다.

회사나 학교 Group Policy가 적용된 PC라면:

```powershell
Get-ExecutionPolicy -List
```

로 확인하고 관리자에게 문의한다.

---

## 오류 3 — `package.json`을 찾을 수 없음

예:

```text
npm ERR! enoent
package.json
```

현재 Terminal 위치를 확인한다.

CMD:

```cmd
cd
```

PowerShell:

```powershell
Get-Location
```

반드시 Project Root에 있어야 한다.

예:

```text
C:\Users\student\projects\react-ai-app
```

---

## 오류 4 — `npm run dev`가 실행되지 않음

먼저:

```bash
npm install
```

이 완료되었는지 확인한다.

그리고 현재 Folder에:

```text
package.json
```

이 있는지 확인한다.

---

## 오류 5 — `localhost:5173`이 열리지 않음

Terminal 출력을 확인한다.

Vite가 다른 Port를 사용할 수 있다.

예:

```text
http://localhost:5174/
```

Terminal에 출력된 실제 주소를 사용한다.

---

## 오류 6 — Port가 이미 사용 중

Vite가 자동으로 다른 Port를 배정할 수 있다.

예:

```text
5173 사용 중
↓
5174 사용
```

오류가 아니라 정상적인 동작일 수 있다.

---

## 오류 7 — Browser 화면이 바뀌지 않음

확인:

```text
파일 저장했는가?
현재 실행 중인 Project를 수정하고 있는가?
Vite Server가 실행 중인가?
Browser Console에 오류가 있는가?
```

---

# 43. 실습 확인 Checklist

다음 항목을 모두 확인한다.

```text
[ ] Node.js를 공식 Site에서 Download했다.
[ ] Node.js 24 LTS 계열을 설치했다.
[ ] node --version이 실행된다.
[ ] npm --version이 실행된다.

[ ] PowerShell에서 다음 명령을 실행했다.
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

[ ] Get-ExecutionPolicy -Scope CurrentUser 결과를 확인했다.

[ ] projects Folder를 만들었다.
[ ] Vite React Project를 생성했다.
[ ] react-ai-app Folder가 생성되었다.
[ ] npm install을 실행했다.
[ ] npm run dev를 실행했다.
[ ] Browser에서 React 화면을 확인했다.
[ ] src/App.jsx를 수정해 화면 변경을 확인했다.
[ ] npm run build가 성공했다.
[ ] dist Folder가 생성되었다.
```

---

# 44. 예상 결과

실습이 정상적으로 끝나면 다음 구조가 준비된다.

```text
Windows
↓
Node.js
↓
npm
↓
Vite
↓
react-ai-app
├─ src
├─ public
├─ package.json
├─ package-lock.json
└─ vite.config.js
↓
npm run dev
↓
Browser
```

그리고 VS Code에서는:

```text
Explorer
+
Editor
+
Terminal
```

을 이용해 React 개발을 진행할 수 있다.

---

# 45. 학생이 설명해야 할 내용

실습 후 다음 질문에 답할 수 있어야 한다.

### 1.

Node.js는 왜 설치했는가?

```text
React 화면 자체를 실행하기 위해서가 아니라
npm과 Vite 같은 개발 도구를 실행하기 위한 기반 Runtime이다.
```

### 2.

npm은 무엇인가?

```text
Node.js 생태계의 Package Manager이며
Package 설치와 Project Script 실행을 담당한다.
```

### 3.

Vite는 무엇인가?

```text
React Project 생성,
개발 Server,
빠른 개발 중 갱신,
Production Build 등을 제공하는 개발 도구다.
```

### 4.

`npm run dev`는 무엇을 하는가?

```text
package.json에 정의된 dev Script를 실행해
Vite 개발 Server를 시작한다.
```

### 5.

PowerShell에서 왜 다음 명령을 실행했는가?

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Windows PowerShell에서 npm 관련 Script 실행이 정책에 의해 차단되는 문제를 방지하고 현재 사용자 범위에서 개발 Script를 실행할 수 있도록 하기 위해서다.

---

# 46. 응용 과제

## 과제 1

프로젝트 이름을 다음으로 변경해 새로 생성한다.

```text
react-practice
```

명령:

```bash
npm create vite@latest react-practice -- --template react
```

---

## 과제 2

`src/App.jsx`를 수정해 다음 내용을 화면에 출력한다.

```text
이름
수업명
오늘 날짜
```

---

## 과제 3

개발 Server 실행 후 Terminal에서 실제 Port를 확인한다.

```text
5173인지
다른 Port인지
```

기록한다.

---

## 과제 4

다음 명령을 실행하고 각각의 차이를 설명한다.

```bash
npm run dev
npm run build
```

---

# 47. 공식 참고자료

## Node.js

Node.js Download:

```text
https://nodejs.org/en/download
```

이번 강의는 Node.js 24 LTS 계열을 기준으로 한다.

---

## Vite

Vite Getting Started:

```text
https://vite.dev/guide/
```

Vite 8은 Node.js `20.19+` 또는 `22.12+`를 요구한다.

Node.js 24 LTS는 이 조건을 만족한다.

---

## VS Code

VS Code Download:

```text
https://code.visualstudio.com/Download
```

Windows 설치 안내:

```text
https://code.visualstudio.com/docs/setup/windows
```

---

## PowerShell Execution Policy

Microsoft PowerShell 공식 문서:

```text
https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-executionpolicy
```

이번 실습에서 사용하는 명령:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

# 48. 관련 Wiki Link

```text
[[React]]
[[Node.js]]
[[npm]]
[[Vite]]
[[VS Code]]
[[PowerShell]]
[[개발환경]]
[[Frontend]]
[[localhost]]
[[Port]]
```

---

# 49. 저장 위치 제안

```text
Academy/
└── 03. 실습/
    └── 00. Phase1_Theoretical/
        └── 02. React/
            └── React_Unit4_개발환경_실습_Windows_CMD_VSCode.md
```

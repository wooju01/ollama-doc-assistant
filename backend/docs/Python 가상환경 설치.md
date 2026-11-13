## Windows에서 Python 3.12 설치

1. [Python 3.12.10 공식 다운로드 페이지](https://www.python.org/downloads/release/python-31210/?utm_source=chatgpt.com)에 접속한다.
    
2. 페이지 아래의 Files 항목에서 `Windows installer (64-bit)`를 다운로드한다.
    
3. 설치 파일을 실행한다.
    
4. 설치 화면에서 Add python.exe to PATH를 체크한다.
    
5. Install Now를 클릭한다.
    
6. 설치 완료 후 CMD를 새로 실행한다.
    

## 설치 확인

```
python --version
```

정상 결과:

```
Python 3.12.10
```

pip도 확인한다.

```
python -m pip --version
```

마지막으로 Python을 실행한다.

```
python
```

```
print("Hello Python!")
```

정상적으로 출력되면 설치가 완료된 거야.

참고: Python 3.12.10은 Python 3.12 계열에서 Windows용 공식 설치 파일이 제공되는 마지막 버전이야. 수업에서 3.12를 사용하는 경우 설치하기 적합해.
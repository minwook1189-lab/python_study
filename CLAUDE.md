# CLAUDE.md

Python 데이터분석 학습 프로젝트 가이드

## Project Overview

데이터분석을 위한 Python 학습 프로젝트. 순차적으로 day01, day02... 형태로 학습 진행.

## Git 자동 동기화 설정

`.vscode/` 폴더에 자동화 설정이 되어 있음:

| 타이밍 | 동작 |
|--------|------|
| 폴더 열 때 | `git pull origin main` (다른 컴퓨터에서 학습한 내용 가져오기) |
| .py 파일 저장 시 | `git commit & push` (학습 내용 GitHub에 자동 업로드) |

**필요 확장 프로그램:** Trigger Task on Save (`Gruntfuggly.triggertaskonsave`)

## Commands

```powershell
# 가상환경 활성화
.\.venv\Scripts\Activate.ps1

# 패키지 설치
pip install -r requirements.txt

# Python 파일 실행
python .\day01_basics.py

# Jupyter Lab 실행
jupyter lab
```

## 가상환경 설정 (최초 1회)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 주요 패키지

- **numpy** - 수치 연산
- **pandas** - 데이터 처리/분석
- **matplotlib** - 시각화
- **seaborn** - 통계 시각화
- **jupyterlab** - 대화형 노트북

## 학습 파일 구조

```
day01_basics.py     - Python 기초
day02_if.py         - 조건문
day03_score.py      - 점수 처리
day04_score_loop.py - 반복문
day05_list.py       - 리스트
day06_list_filter.py - 리스트 필터
day07_dict.py       - 딕셔너리
day08_function.py   - 함수
```

## Cursor 권장 설정

### 1. Python 인터프리터 선택
- `Ctrl+Shift+P` → "Python: Select Interpreter" → `.venv` 선택

### 2. 권장 확장 프로그램
- **Python** (Microsoft)
- **Pylance** (Microsoft) - 코드 자동완성, 타입 체크
- **Jupyter** (Microsoft) - 노트북 지원
- **Trigger Task on Save** - 자동 git 저장

### 3. 코드 실행 단축키
- `Ctrl+F5` - 현재 파일 실행 (디버그 없이)
- `F5` - 디버그 모드 실행
- `Shift+Enter` - 선택한 코드만 실행 (Interactive Window)

## Language

콘텐츠는 한국어(Korean)로 작성.

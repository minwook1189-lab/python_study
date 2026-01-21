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

## 학습 커리큘럼

### Part 1: Python 기초 (Day 01-10)

| Day | 주제 | 파일명 | 상태 |
|-----|------|--------|------|
| 01 | 변수와 자료형 | day01_basics.py | ✅ |
| 02 | 조건문 | day02_if.py | ✅ |
| 03 | 조건문 실습 | day03_score.py | ✅ |
| 04 | 반복문 | day04_score_loop.py | ✅ |
| 05 | 리스트 | day05_list.py | ✅ |
| 06 | 리스트 활용 | day06_list_filter.py | ✅ |
| 07 | 딕셔너리 | day07_dict.py | ✅ |
| 08 | 함수 | day08_function.py | ✅ |
| 09 | 파일 입출력 | day09_file_io.py | ✅ |
| 10 | 에러 처리 | day10_error.py | 📍 |

### Part 2: 데이터분석 라이브러리 (Day 11-20)

| Day | 주제 | 파일명 | 상태 |
|-----|------|--------|------|
| 11 | NumPy 기초 | day11_numpy_basic.py | ⬜ |
| 12 | NumPy 활용 | day12_numpy_adv.py | ⬜ |
| 13 | Pandas 기초 | day13_pandas_basic.py | ⬜ |
| 14 | 데이터 읽기 | day14_pandas_read.py | ⬜ |
| 15 | 데이터 탐색 | day15_pandas_explore.py | ⬜ |
| 16 | 데이터 선택 | day16_pandas_select.py | ⬜ |
| 17 | 데이터 정제 | day17_pandas_clean.py | ⬜ |
| 18 | 데이터 변환 | day18_pandas_transform.py | ⬜ |
| 19 | 그룹 연산 | day19_pandas_groupby.py | ⬜ |
| 20 | 데이터 병합 | day20_pandas_merge.py | ⬜ |

### Part 3: 데이터 시각화 (Day 21-25)

| Day | 주제 | 파일명 | 상태 |
|-----|------|--------|------|
| 21 | Matplotlib 기초 | day21_matplotlib_basic.py | ⬜ |
| 22 | 다양한 차트 | day22_matplotlib_charts.py | ⬜ |
| 23 | Seaborn 기초 | day23_seaborn_basic.py | ⬜ |
| 24 | Seaborn 활용 | day24_seaborn_adv.py | ⬜ |
| 25 | 시각화 실습 | day25_visualization.py | ⬜ |

### Part 4: 실전 프로젝트 (Day 26-30)

| Day | 주제 | 파일명 | 상태 |
|-----|------|--------|------|
| 26-27 | 프로젝트 1: 공공데이터 분석 | project1_public_data.py | ⬜ |
| 28-29 | 프로젝트 2: 판매/매출 분석 | project2_sales.py | ⬜ |
| 30 | 정리 및 복습 | - | ⬜ |

### 상태 표시
- ✅ 완료
- 📍 현재 진행 중
- ⬜ 미진행

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

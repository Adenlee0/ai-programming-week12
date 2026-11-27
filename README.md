# \# ai-programming-week12

# 

# \## 1. What

# CSV 파일에서 학생들의 성적 데이터를 읽어 유효한 데이터와 건너뛴 데이터를 구분하는 프로그램입니다.

# 

# \## 2. Why

# CSV 파일의 잘못된 형식이나 점수 범위를 벗어난 데이터를 구분하여 안전하게 처리하기 위해 만들었습니다.

# 

# \## 3. How

# `load\_scores(path)` 함수를 사용하여 CSV 파일을 읽습니다.

# 

# \- `kept`: 유효한 이름과 점수 목록

# \- `skipped`: 건너뛴 데이터의 줄 번호, 원본 내용, 제외 이유

# 

# 실행 방법:

# ```bash

# python week12/load\_scores.py week12/scores.csv


# ai-programming-week12

# 성적 CSV 데이터 읽기 프로그램 (load_scores)

## 1. What

CSV 파일에 저장된 학생들의 성적 데이터를 읽고, 유효한 데이터와 잘못된 데이터를 구분하는 프로그램입니다.

- 유효한 데이터는 이름과 점수를 저장합니다.
- 잘못된 데이터는 제외하고 해당 줄의 번호와 제외 이유를 기록합니다.
- 중복된 이름도 별도로 삭제하지 않고 유지합니다.

## 2. Why

CSV 파일에는 이름이나 점수가 비어 있거나, 점수가 정수가 아닌 경우, 점수 범위를 벗어난 경우 등 다양한 오류가 포함될 수 있습니다.

이러한 데이터를 그대로 사용하면 잘못된 결과가 발생하거나 프로그램 실행 중 오류가 생길 수 있습니다.

따라서 CSV 파일을 읽는 과정에서 데이터의 유효성을 검사하고, 정상적인 데이터와 잘못된 데이터를 구분하여 안전하게 처리할 수 있도록 만들었습니다.

## 3. Requirements

프로그램 실행에 필요한 환경은 다음과 같습니다.

- Python 3
- Python 기본 라이브러리 `csv`
- 테스트 실행을 위한 `pytest`

`pytest`가 설치되어 있지 않다면 다음 명령어로 설치할 수 있습니다.

```bash
python -m pip install pytest
```

## 4. Input Format

프로그램은 이름과 점수 두 개의 열로 구성된 CSV 파일을 입력받습니다.

**입력 파일 예시**

```csv
이름,점수
김철수,90
이영희,85
박민수,105
최유진,결석
```

**데이터 처리 기준**

| 검사 항목 | 처리 기준 |
|---|---|
| 열 개수 | 두 개가 아니면 제외 |
| 이름 | 비어 있으면 제외 |
| 점수 | 비어 있으면 제외 |
| 자료형 | 정수가 아니면 제외 |
| 점수 범위 | 0~100을 벗어나면 제외 |
| 중복 이름 | 중복을 허용하고 유지 |

첫 번째 행은 열 제목으로 처리합니다.

## 5. How to Run

프로젝트 최상위 폴더에서 터미널을 열고 다음 명령어를 실행합니다.

**① 기본 성적 데이터 읽기**

```bash
python week12/load_scores.py week12/scores.csv
```

**② 다른 CSV 파일 읽기**

```bash
python week12/load_scores.py week12/weird.csv
```

명령어 마지막에 입력 파일의 경로를 지정하면 원하는 CSV 파일을 읽을 수 있습니다.

## 6. Output

`load_scores(path)` 함수는 두 가지 결과를 반환합니다.

- `kept`: 유효한 데이터 목록. `(이름, 점수)` 형태로 저장됩니다.
- `skipped`: 제외된 데이터 목록. `(줄 번호, 원본 내용, 제외 이유)` 형태로 저장됩니다.

이를 통해 정상적인 성적 데이터뿐만 아니라 제외된 데이터와 그 이유도 확인할 수 있습니다.

## 7. Testing

`pytest`를 사용하여 프로그램의 정상 작동 여부와 예외 상황을 테스트합니다.

프로젝트 최상위 폴더에서 다음 명령어를 실행합니다.

```bash
cd week12
python -m pytest test_load_scores.py -v
```

**주요 테스트 항목**

- 정상적인 CSV 파일 읽기
- 존재하지 않는 파일에 대한 예외 처리
- 헤더만 존재하는 빈 CSV 파일 처리
- 점수 최솟값과 최댓값 확인
- 점수 범위를 벗어난 데이터 처리
- 잘못된 점수 형식 처리

※ 테스트 코드에는 의도적으로 실패하도록 작성된 테스트가 포함되어 있으므로, 전체 테스트 결과를 확인할 때 이를 고려해야 합니다.

## 8. File Structure

```text
ai-programming-week12/
│
├── README.md
├── LICENSE
├── .gitignore
│
└── week12/
    ├── README_양식.md
    ├── load_scores.py
    ├── test_load_scores.py
    ├── test_ai_A.py
    ├── test_ai_B.py
    ├── test_fixed.py
    ├── bug3_logic.py
    ├── scores.csv
    ├── empty.csv
    ├── weird.csv
    ├── prompts.txt
    └── .gitignore
```

| 파일 | 설명 |
|---|---|
| `load_scores.py` | CSV 파일 읽기 및 데이터 검증 프로그램 |
| `test_load_scores.py` | 직접 작성한 테스트 코드 |
| `test_ai_A.py` | AI가 작성한 테스트 코드 A |
| `test_ai_B.py` | AI가 작성한 테스트 코드 B |
| `test_fixed.py` | 수정된 코드의 테스트 |
| `bug3_logic.py` | 오류가 포함된 비교용 코드 |
| `scores.csv` | 기본 성적 데이터 |
| `empty.csv` | 헤더만 포함된 CSV 파일 |
| `weird.csv` | 예외 상황 확인용 CSV 파일 |
| `prompts.txt` | AI에 입력한 프롬프트 기록 |
| `README_양식.md` | README 작성 양식 |

## 9. Author & AI Usage

- Author: 본인 이름 / 본인 학번
- AI Usage: AI를 활용하여 코드와 테스트 코드를 검토하고, 오류 분석 및 README 문서 작성을 진행했습니다.
- 직접 수행한 작업: 프로그램 실행 및 테스트 결과 확인, 코드 수정, Git과 GitHub를 이용한 버전 관리 및 저장소 관리

## License

MIT License (LICENSE 파일 참고)

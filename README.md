# 🎵 K-pop 퀴즈 게임

터미널에서 실행하는 Python 기반 K-pop 상식 퀴즈 게임입니다.  
등록된 문제를 풀고, 새로운 퀴즈를 추가하고, 최고 점수를 `state.json`에 저장할 수 있습니다.

## 1. 프로젝트 개요

이 프로젝트는 Python 기본 문법과 객체 지향 프로그래밍, JSON 파일 입출력, 예외 처리, Git 브랜치 작업을 연습하기 위해 만든 콘솔 퀴즈 게임입니다.

프로그램을 실행하면 다음 메뉴를 사용할 수 있습니다.

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료

프로그램을 종료한 뒤 다시 실행해도 추가한 퀴즈와 최고 점수가 유지됩니다.

## 2. 퀴즈 주제와 선정 이유

주제는 **K-pop**입니다.

K-pop은 BTS, BLACKPINK, IVE, SEVENTEEN, TWICE 등 친숙한 아티스트를 활용해 문제를 만들기 쉽고, 사용자도 부담 없이 참여할 수 있는 주제라고 생각해 선택했습니다.

기본 퀴즈는 직접 작성한 K-pop 문제 5개로 구성되어 있습니다.

## 3. 개발 환경

- Python 3.10 이상
- 외부 라이브러리 사용 없음
- Python 표준 라이브러리 사용
  - `json`
  - `pathlib`

Python 버전 확인:

```bash
python3 --version
```

## 4. 실행 방법

저장소를 복제합니다.

```bash
git clone https://github.com/greenable-7/Repository-name-kpop-quiz-game-Public-.git
```

프로젝트 폴더로 이동합니다.

```bash
cd Repository-name-kpop-quiz-game-Public-
```

프로그램을 실행합니다.

```bash
python3 main.py
```

## 5. 주요 기능

### 퀴즈 풀기

- 저장된 모든 퀴즈를 순서대로 출제합니다.
- 각 문제의 정답 번호를 `1~4` 사이에서 입력합니다.
- 정답과 오답 여부를 바로 확인할 수 있습니다.
- 모든 문제를 풀면 정답 수와 100점 기준 점수를 출력합니다.
- 기존 최고 점수보다 높은 경우 최고 점수를 갱신하고 저장합니다.
- 등록된 퀴즈가 없을 경우 안내 메시지를 출력합니다.

### 퀴즈 추가

- 새로운 문제를 입력할 수 있습니다.
- 선택지 4개를 입력합니다.
- 정답 번호를 `1~4` 사이에서 입력합니다.
- 추가한 퀴즈는 즉시 `state.json`에 저장됩니다.
- 빈 문자열 입력을 방지합니다.

### 퀴즈 목록

- 현재 저장된 퀴즈의 문제를 번호와 함께 확인할 수 있습니다.
- 퀴즈가 없는 경우 별도 안내 메시지를 출력합니다.

### 점수 확인

- 지금까지 기록된 최고 점수를 확인할 수 있습니다.
- 아직 퀴즈를 한 번도 풀지 않았다면 기록이 없다는 메시지를 출력합니다.

### 입력 및 예외 처리

숫자 입력 시 다음 경우를 처리합니다.

- 빈 입력
- 숫자가 아닌 문자 입력
- 허용 범위를 벗어난 숫자
- 입력 앞뒤 공백
- `Ctrl+C` (`KeyboardInterrupt`)
- 입력 스트림 종료 (`EOFError`)

또한 `state.json` 파일이 없거나 읽을 수 없는 경우 기본 퀴즈 데이터로 복구하도록 구현했습니다.

## 6. 클래스 구조

### `Quiz`

개별 퀴즈 한 문제를 표현하는 클래스입니다.

주요 속성:

- `question`: 문제
- `choices`: 선택지 4개
- `answer`: 정답 번호

주요 메서드:

- `display()`: 문제와 선택지 출력
- `is_correct()`: 사용자의 답이 정답인지 확인
- `to_dict()`: Quiz 객체를 JSON 저장용 딕셔너리로 변환
- `from_dict()`: 딕셔너리를 Quiz 객체로 변환

### `QuizGame`

퀴즈 게임 전체 흐름을 관리하는 클래스입니다.

주요 속성:

- `quizzes`: 퀴즈 목록
- `best_score`: 최고 점수
- `state_path`: `state.json` 경로

주요 메서드:

- `show_menu()`
- `read_number()`
- `read_text()`
- `play_quiz()`
- `add_quiz()`
- `list_quizzes()`
- `show_best_score()`
- `load_state()`
- `save_state()`

## 7. 파일 구조

```text
Repository-name-kpop-quiz-game-Public-/
├── main.py
├── game.py
├── quiz.py
├── default_data.py
├── state.json
├── README.md
├── STUDY_CONTEXT.md
├── .gitignore
└── screenshots/
    ├── 깃로그.png
    ├── 깃클론.png
    ├── 깃풀.png
    ├── 점수확인.png
    ├── 퀴즈목록.png
    ├── 퀴즈추가.png
    ├── 퀴즈풀기1.png
    └── 퀴즈풀기2.png
```

각 파일의 역할은 다음과 같습니다.

| 파일 | 역할 |
|---|---|
| `main.py` | 프로그램 시작, 메뉴 선택, 종료 흐름 |
| `game.py` | `QuizGame` 클래스와 게임 전체 기능 |
| `quiz.py` | 개별 문제를 표현하는 `Quiz` 클래스 |
| `default_data.py` | 첫 실행에 사용할 기본 K-pop 퀴즈 5개 |
| `state.json` | 퀴즈 목록과 최고 점수 저장 |
| `screenshots/` | 프로그램 실행 및 Git 실습 증빙 이미지 |
| `STUDY_CONTEXT.md` | 프로젝트 학습 내용을 정리한 개인 학습 문서 |

## 8. 데이터 파일 설명

프로젝트 루트의 `state.json`에 퀴즈 목록과 최고 점수를 UTF-8 JSON 형식으로 저장합니다.

기본 구조:

```json
{
  "quizzes": [
    {
      "question": "문제 내용",
      "choices": [
        "선택지 1",
        "선택지 2",
        "선택지 3",
        "선택지 4"
      ],
      "answer": 1
    }
  ],
  "best_score": 80
}
```

필드 의미:

- `quizzes`: 퀴즈 객체들의 목록
- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호 (`1~4`)
- `best_score`: 지금까지의 최고 점수 (`0~100`)

`state.json`이 존재하지 않으면 기본 K-pop 퀴즈 5개로 시작합니다.  
파일을 읽는 과정에서 오류가 발생하면 안내 메시지를 출력하고 기본 데이터로 복구합니다.

## 9. Git 작업 기록

이 프로젝트에서는 기능 단위로 커밋하고, 별도 브랜치에서 퀴즈 출제 기능을 구현한 뒤 `main` 브랜치에 병합했습니다.

현재 저장소에서 확인되는 내용:

- 의미 있는 커밋 17개
- 기능 브랜치: `feature/play-quiz`
- 퀴즈 출제 기능을 브랜치에서 작업 후 `main`에 merge
- 원격 GitHub 저장소에 push
- 저장소 clone 실습
- 기존 작업 디렉터리에서 pull 실습

주요 커밋 예시:

```text
Feat: Quiz 클래스와 정답 확인 기능 추가
Feat: K-pop 기본 퀴즈 5개 추가
Feat: QuizGame 메뉴 화면 추가
Feat: state.json 저장과 복구 처리 추가
Feat: 퀴즈 출제와 점수 계산 기능 구현
Merge: 퀴즈 출제 기능 병합
Feat: 퀴즈 추가와 목록 조회 기능 구현
Docs: 실행 방법과 데이터 구조 문서화
Docs: git clone 및 pull 실습 스크린샷 추가
```

## 10. 실행 및 Git 증빙 화면

### 퀴즈 추가

![퀴즈 추가](screenshots/퀴즈추가.png)

### 퀴즈 목록

![퀴즈 목록](screenshots/퀴즈목록.png)

### 퀴즈 풀기

![퀴즈 풀기 1](screenshots/퀴즈풀기1.png)

![퀴즈 풀기 2](screenshots/퀴즈풀기2.png)

### 최고 점수 확인

![점수 확인](screenshots/점수확인.png)

### Git 로그 및 브랜치 병합

![Git 로그](screenshots/깃로그.png)

### Git clone

![Git clone](screenshots/깃클론.png)

### Git pull

![Git pull](screenshots/깃풀.png)

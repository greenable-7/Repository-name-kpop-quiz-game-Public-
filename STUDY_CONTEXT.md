# M2 퀴즈 게임 학습 이어가기

## 다음 대화에서 사용할 요청

새 대화를 시작할 때 아래처럼 말한다.

> `STUDY_CONTEXT.md`와 `main.py`를 읽고, K-pop 퀴즈 게임 공부를 Day 1부터 이어가자.

## 프로젝트 현재 상태

- 프로젝트: 터미널 기반 K-pop 퀴즈 게임
- 실행: `cd ~/Desktop/kpop-quiz-game` 후 `python3 main.py`
- GitHub 저장소: `greenable-7/Repository-name-kpop-quiz-game-Public-`
- 기본 브랜치: `main`
- 기능 브랜치: `feature/play-quiz` (GitHub에 업로드됨)
- GitHub 업로드, 브랜치 병합, `clone`, `push`, `pull` 실습을 완료함
- 원본 폴더: `~/Desktop/kpop-quiz-game`
- 복제 실습 폴더: `~/Desktop/kpop-quiz-game-clone`

## 구현된 기능

- 메뉴: 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인, 종료
- `Quiz` 클래스: 문제, 선택지 4개, 정답 번호 관리
- `QuizGame` 클래스: 메뉴와 게임 전체 흐름 관리
- `state.json`: 퀴즈와 최고 점수를 UTF-8 JSON으로 저장
- 빈 입력, 문자 입력, 범위 밖 입력, Ctrl+C, EOF, 손상된 저장 파일 처리

## 제출 전 남은 일

실행 화면을 캡처하여 USB와 GitHub에 보관한다.

- `m2-environment-python-git.png`
- `m2-quiz-add.png`
- `m2-quiz-list.png`
- `m2-quiz-play.png`
- `m2-score.png`
- `m2-github-branches.png`
- `m2-git-log-branch-merge.png`

Git 로그 화면과 GitHub 브랜치 화면은 이미 캡처했다. 스크린샷은 추후 `docs/screenshots/`에도 추가할 수 있다.

## 시험 대비 학습 방식

실제 코드 이해 50%와 코드 없이 푸는 문법 문제 50%로 공부한다.

코드를 볼 때 매번 아래 질문에 답한다.

1. 이 코드가 없으면 어떻게 되는가?
2. 이 줄 직전 변수에는 어떤 값이 들어 있는가?
3. 조건이 참·거짓일 때 어디로 이동하는가?
4. 잘못된 입력에는 어떻게 대응하는가?
5. 같은 기능을 짧게 직접 작성할 수 있는가?

## 추천 순서

1. `main.py`: `main()`, `while True`, `if/elif`, `break`, 안전한 종료
2. `quiz.py`: 클래스, `__init__`, `self`, 속성과 메서드
3. `game.py`: `QuizGame`, 함수 분리, 리스트와 반복문
4. `state.json`과 저장 로직: JSON, 파일 입출력, `try/except`
5. Git: `add`, `commit`, `push`, `pull`, `clone`, `branch`, `merge`
6. 출력 예측, 빈칸 작성, 오류 수정, 짧은 코드 직접 작성 문제

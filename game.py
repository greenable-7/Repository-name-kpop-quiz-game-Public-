"""게임 전체 흐름을 관리하는 클래스."""

import json
from pathlib import Path

from default_data import create_default_quizzes
from quiz import Quiz


class QuizGame:
    """퀴즈 목록과 최고 점수를 관리한다."""

    def __init__(self, state_path=None):
        self.state_path = Path(state_path) if state_path else Path(__file__).with_name("state.json")
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        """state.json을 불러오고, 문제가 있으면 기본 데이터로 복구한다."""
        if not self.state_path.exists():
            self.quizzes = create_default_quizzes()
            print("📂 저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return

        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            quizzes = data.get("quizzes", [])
            best_score = data.get("best_score")
            if not isinstance(quizzes, list) or not (
                isinstance(best_score, int) or best_score is None
            ):
                raise ValueError("저장 데이터 형식이 올바르지 않습니다.")

            self.quizzes = [Quiz.from_dict(quiz) for quiz in quizzes]
            self.best_score = best_score
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개)")
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"⚠️ 저장 데이터를 읽을 수 없어 기본 퀴즈로 복구합니다. ({error})")
            self.quizzes = create_default_quizzes()
            self.best_score = None

    def save_state(self):
        """현재 퀴즈와 최고 점수를 UTF-8 JSON 파일로 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with self.state_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except OSError as error:
            print(f"⚠️ 데이터를 저장하지 못했습니다. ({error})")
            return False

    def show_menu(self):
        print("\n" + "=" * 40)
        print("        🎵 나만의 K-pop 퀴즈 게임 🎵")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

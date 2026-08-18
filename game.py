"""게임 전체 흐름을 관리하는 클래스."""

import json
from pathlib import Path

from default_data import create_default_quizzes
from quiz import Quiz


class QuizGame:
    """퀴즈 목록과 최고 점수를 관리한다."""

    def __init__(self, state_path=None):
        self.state_path = (
            Path(state_path)
            if state_path
            else Path(__file__).with_name("state.json")
        )
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        """state.json을 불러오고, 문제가 있으면 기본 데이터로 복구한다."""
        if not self.state_path.exists():
            self.quizzes = create_default_quizzes()
            self.best_score = None
            print("📂 저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return

        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            # JSON 문법이 맞더라도 최상위 구조가 딕셔너리가 아니면
            # 정상적인 저장 데이터가 아니므로 기본 데이터로 복구한다.
            if not isinstance(data, dict):
                raise ValueError("저장 데이터 형식이 올바르지 않습니다.")

            quizzes_data = data.get("quizzes", [])
            best_score = data.get("best_score")

            if not isinstance(quizzes_data, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            if best_score is not None and (
                type(best_score) is not int or not 0 <= best_score <= 100
            ):
                raise ValueError("최고 점수 형식이 올바르지 않습니다.")

            loaded_quizzes = []

            for quiz_data in quizzes_data:
                if not isinstance(quiz_data, dict):
                    raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")
                loaded_quizzes.append(Quiz.from_dict(quiz_data))

            self.quizzes = loaded_quizzes
            self.best_score = best_score

            print(
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개)"
            )

        except (
            OSError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
        ) as error:
            print(
                "⚠️ 저장 데이터를 읽을 수 없어 기본 퀴즈로 복구합니다. "
                f"({error})"
            )
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
        """메인 메뉴를 출력한다."""
        print("\n" + "=" * 40)
        print("        🎵 나만의 K-pop 퀴즈 게임 🎵")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def read_number(self, prompt, minimum, maximum):
        """빈 값, 문자, 범위 밖 값을 안내하며 정수 입력을 받는다."""
        while True:
            value = input(prompt).strip()

            if not value:
                print(
                    f"⚠️ 입력이 비어 있습니다. "
                    f"{minimum}-{maximum} 사이의 숫자를 입력하세요."
                )
                continue

            try:
                number = int(value)
            except ValueError:
                print(
                    f"⚠️ 잘못된 입력입니다. "
                    f"{minimum}-{maximum} 사이의 숫자를 입력하세요."
                )
                continue

            if not minimum <= number <= maximum:
                print(
                    f"⚠️ 잘못된 입력입니다. "
                    f"{minimum}-{maximum} 사이의 숫자를 입력하세요."
                )
                continue

            return number

    def play_quiz(self):
        """모든 퀴즈를 출제하고 이번 점수와 최고 점수를 갱신한다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        correct_count = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print("\n" + "-" * 40)
            quiz.display(number)

            selected_answer = self.read_number(
                "정답 입력 (1-4): ",
                1,
                4,
            )

            if quiz.is_correct(selected_answer):
                correct_count += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct_count / len(self.quizzes) * 100)

        print("\n" + "=" * 40)
        print(
            f"🏆 결과: {len(self.quizzes)}문제 중 "
            f"{correct_count}문제 정답! ({score}점)"
        )

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

        print("=" * 40)

    def read_text(self, prompt):
        """공백만 입력한 경우를 막고 텍스트를 입력받는다."""
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("⚠️ 입력이 비어 있습니다. 내용을 입력하세요.")

    def add_quiz(self):
        """사용자가 입력한 문제를 퀴즈 목록과 state.json에 추가한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = self.read_text("문제를 입력하세요: ")

        choices = [
            self.read_text(f"선택지 {number}: ")
            for number in range(1, 5)
        ]

        answer = self.read_number(
            "정답 번호 (1-4): ",
            1,
            4,
        )

        self.quizzes.append(
            Quiz(question, choices, answer)
        )

        if self.save_state():
            print("✅ 퀴즈가 추가되고 저장되었습니다!")
        else:
            print("⚠️ 퀴즈는 추가되었지만 파일 저장에는 실패했습니다.")

    def list_quizzes(self):
        """등록된 모든 퀴즈의 문제를 번호와 함께 출력한다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("-" * 40)

    def show_best_score(self):
        """최고 점수를 출력한다."""
        if self.best_score is None:
            print("🏆 아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"🏆 최고 점수: {self.best_score}점")

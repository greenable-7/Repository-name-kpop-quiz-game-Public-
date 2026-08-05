"""게임 전체 흐름을 관리하는 클래스."""

from default_data import create_default_quizzes


class QuizGame:
    """퀴즈 목록과 최고 점수를 관리한다."""

    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

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

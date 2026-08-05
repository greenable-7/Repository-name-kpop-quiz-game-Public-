"""K-pop 퀴즈 게임의 실행 파일."""

from game import QuizGame


def main():
    game = QuizGame()
    game.show_menu()
    print("게임 기능을 준비하고 있습니다.")


if __name__ == "__main__":
    main()

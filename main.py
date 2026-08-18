"""K-pop 퀴즈 게임의 실행 파일."""

from game import QuizGame


def main():
    game = QuizGame()

    try:
        while True:
            game.show_menu()
            choice = game.read_number("선택: ", 1, 5)

            if choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                game.list_quizzes()
            elif choice == 4:
                game.show_best_score()
            else:
                game.save_state()
                print("👋 게임을 종료합니다. 즐거운 하루 되세요!")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되었습니다. 현재 데이터를 저장하고 안전하게 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()

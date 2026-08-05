"""개별 퀴즈를 표현하는 클래스."""


class Quiz:
    """문제, 4개의 선택지, 정답 번호를 가진 K-pop 퀴즈."""

    def __init__(self, question, choices, answer):
        if len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")
        if answer not in range(1, 5):
            raise ValueError("정답 번호는 1~4 사이여야 합니다.")

        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number=None):
        """퀴즈 문제와 선택지를 화면에 출력한다."""
        if number is not None:
            print(f"\n[문제 {number}]")
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, selected_answer):
        """입력한 번호가 정답인지 반환한다."""
        return selected_answer == self.answer

    def to_dict(self):
        """JSON에 저장할 수 있는 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """저장된 딕셔너리에서 Quiz 객체를 생성한다."""
        return cls(data["question"], data["choices"], data["answer"])

"""첫 실행에 사용하는 기본 K-pop 퀴즈 데이터."""

from quiz import Quiz


def create_default_quizzes():
    """직접 작성한 K-pop 기본 퀴즈 5개를 반환한다."""
    return [
        Quiz(
            "BTS의 팬덤 이름은 무엇일까요?",
            ["BLINK", "ARMY", "ONCE", "CARAT"],
            2,
        ),
        Quiz(
            "BLACKPINK의 멤버가 아닌 사람은 누구일까요?",
            ["지수", "제니", "로제", "윈터"],
            4,
        ),
        Quiz(
            "아이브(IVE)의 대표곡으로 알려진 곡은 무엇일까요?",
            ["LOVE DIVE", "Dynamite", "God's Menu", "Very Nice"],
            1,
        ),
        Quiz(
            "세븐틴의 멤버 수는 몇 명일까요?",
            ["7명", "9명", "11명", "13명"],
            4,
        ),
        Quiz(
            "트와이스의 팬덤 이름은 무엇일까요?",
            ["MOA", "ONCE", "MIDZY", "FEARNOT"],
            2,
        ),
    ]

from _pytest.capture import CaptureFixture
from typing import Generator

from housepaint import (
    BG,
    FG,
    paint,
    Style
)
from housepaint.premixed import wild


SUCCESS_EXPECTED = """This
Should
All
Be
Green
\033[0m"""

WILD_EXPECTED = """William Blake
Pablo Picasso
Ivan Albright
Henrique Medina
\x1b[0m"""


class TestHousePaint:
    def test_paint(self, capsys: Generator[CaptureFixture[str], None, None]) -> None:
        @paint(foreground=FG.GREEN, background=BG.BLACK, styles=Style.BOLD)
        def success_example() -> None:
            print("This")
            print("Should")
            print("All")
            print("Be")
            print("Green")

        success_example()
        captured = capsys.readouterr()
        assert captured.out == SUCCESS_EXPECTED

    def test_premixed(self, capsys: Generator[CaptureFixture[str], None, None]) -> None:
        @wild()
        def wild_example() -> None:
            print("William Blake")
            print("Pablo Picasso")
            print("Ivan Albright")
            print("Henrique Medina")

        wild_example()
        captured = capsys.readouterr()
        assert captured.out == WILD_EXPECTED

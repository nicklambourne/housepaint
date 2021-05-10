from sys import stdout
from typing import Callable, List, Optional, TextIO, Union

from housepaint.pigments import BG, FG, Style


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def paint(
    func: Callable,
    foreground: FG = FG.DEFAULT,
    background: BG = BG.DEFAULT,
    styles: Optional[Union[Style, List[Style]]] = None,
    target: TextIO = stdout
) -> Callable:
    styles = [styles] if type(styles) == Style else styles

    def wrapper():
        style = ''.join(map(str, styles)) if styles else ''
        print(f"{foreground}{background}{style}", end="", file=target)
        func()
        print(f"{Style.RESET}", end="")
    return wrapper

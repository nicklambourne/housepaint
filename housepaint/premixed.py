from functools import partial

from housepaint.paint import paint
from housepaint.pigments import BG, FG, Style


success = partial(paint, foreground=FG.GREEN, styles=Style.BOLD)
warning = partial(paint, foreground=FG.YELLOW, styles=Style.BOLD)
error = partial(paint, foreground=FG.RED, styles=Style.BOLD)
wild = partial(
    paint,
    foreground=FG.MAGENTA,
    background=BG.CYAN,
    styles=[Style.BOLD, Style.BLINK]
)

from enum import Enum


class Format(Enum):
    def __str__(self):
        return self.value


class FG(Format):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    DEFAULT = "\033[39m"


class BG(Format):
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    BLUE = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN = "\033[46m"
    WHITE = "\033[47m"
    DEFAULT = "\033[49m"


class Style(Format):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    STANDOUT = "\033[3m"
    UNDERSCORE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"

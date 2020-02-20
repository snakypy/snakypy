NONE = '\x1b[0m'
""""""


class FG:
    BLACK = '\x1b[30m'
    MAGENTA = '\x1b[95m'
    BLUE = '\x1b[94m'
    GREEN = '\x1b[92m'
    RED = '\x1b[91m'
    YELLOW = '\x1b[93m'
    CYAN = '\x1b[96m'
    WHITE = '\x1b[97m'

    WARNING = f'{YELLOW}⚠ '
    ERROR = f'{RED}✖ '
    FINISH = f'{GREEN}✔ '
    QUESTION = f'{CYAN}➜ '


class BG:
    BLACK = '\x1b[40m'
    MAGENTA = '\x1b[105m'
    BLUE = '\x1b[104m'
    GREEN = '\x1b[102m'
    RED = '\x1b[101m'
    YELLOW = '\x1b[103m'
    CYAN = '\x1b[106m'
    WHITE = '\x1b[107m'

    WARNING = f'{YELLOW}⚠ '
    ERROR = f'{RED}✖ '
    FINISH = f'{GREEN}✔ '
    QUESTION = f'{CYAN}➜ '


__all__ = ['NONE', 'FG', 'BG']

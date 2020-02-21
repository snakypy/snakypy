"""Module to store Ansi configurations.
In certain functions of the snakypy package, functions with named
parameters "fg" and "bg" are found, in which you can receive a
certain foreground or background color in Ansi.
"""
import sys


def return_ansi(value):
    if sys.platform.startswith('win'):
        return ''
    return value


NONE = return_ansi('\x1b[0m')
"""Variable to reset Ansi color settings."""


class FG:
    """
    Class FG (foreground) that receives colors and ANSI settings in each of
    the global variables below to be applied in texts.
    """

    BLACK = return_ansi('\x1b[30m')
    MAGENTA = return_ansi('\x1b[95m')
    BLUE = return_ansi('\x1b[94m')
    GREEN = return_ansi('\x1b[92m')
    RED = return_ansi('\x1b[91m')
    YELLOW = return_ansi('\x1b[93m')
    CYAN = return_ansi('\x1b[96m')
    WHITE = return_ansi('\x1b[97m')

    WARNING = return_ansi(f'{YELLOW}⚠ ')
    ERROR = return_ansi(f'{RED}✖ ')
    FINISH = return_ansi(f'{GREEN}✔ ')
    QUESTION = return_ansi(f'{CYAN}➜ ')


class BG:
    """
    Class BG (background) that receives colors and ANSI settings in each
    of the global variables below to be applied in texts.
    """

    BLACK = return_ansi('\x1b[40m')
    MAGENTA = return_ansi('\x1b[105m')
    BLUE = return_ansi('\x1b[104m')
    GREEN = return_ansi('\x1b[102m')
    RED = return_ansi('\x1b[101m')
    YELLOW = return_ansi('\x1b[103m')
    CYAN = return_ansi('\x1b[106m')
    WHITE = return_ansi('\x1b[107m')

    WARNING = return_ansi(f'{YELLOW}⚠ ')
    ERROR = return_ansi(f'{RED}✖ ')
    FINISH = return_ansi(f'{GREEN}✔ ')
    QUESTION = return_ansi(f'{CYAN}➜ ')


class SGR:
    """

    """

    BOLD = return_ansi('\x1b[1m')
    ITALIC = return_ansi('\x1b[3m')
    UNDERLINE = return_ansi('\x1b[4m')
    SLOW_BLINK = return_ansi('\x1b[5m')
    RAPID_BLINK = return_ansi('\x1b[6m')
    REVERSE_COLOR = return_ansi('\x1b[7m')


__all__ = ['NONE', 'FG', 'BG', 'SGR']

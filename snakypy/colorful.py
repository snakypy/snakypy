from snakypy.decorators import use_unix_system


BLACK_COLOR = '\x1b[0;30m'
MAGENTA_COLOR = '\x1b[0;95m'
BLUE_COLOR = '\x1b[0;94m'
GREEN_COLOR = '\x1b[0;92m'
RED_COLOR = '\x1b[0;91m'
YELLOW_COLOR = '\x1b[0;93m'
CYAN_COLOR = '\x1b[0;96m'
WHITE_COLOR = '\x1b[0;37m'
NONE_SCOPE_ANSI = '\x1b[0m'

WARNING_ALERT = f'{YELLOW_COLOR}⚠ '
ERROR_ALERT = f'{RED_COLOR}✖ '
FINISH_ALERT = f'{GREEN_COLOR}✔ '
QUESTION_ALERT = f'{CYAN_COLOR}➜ '


@use_unix_system
def printer(*args, style=NONE_SCOPE_ANSI, sep=' ', end='\n', file=None, flush=False):
    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    text = ' '.join(map(str, lst))

    return print(f'{style}{text}{NONE_SCOPE_ANSI}', sep=sep, end=end, file=file, flush=flush)


@use_unix_system
def entry(text, *, style='', jump_line='\n> '):
    try:
        return input(f'{style}{text}{jump_line}{NONE_SCOPE_ANSI}')
    except KeyboardInterrupt:
        print(f'\n{WARNING_ALERT} Aborted by user.{NONE_SCOPE_ANSI}')


__all__ = ['BLACK_COLOR', 'MAGENTA_COLOR', 'BLUE_COLOR', 'GREEN_COLOR',
           'RED_COLOR', 'YELLOW_COLOR', 'CYAN_COLOR', 'WHITE_COLOR',
           'WARNING_ALERT', 'ERROR_ALERT', 'FINISH_ALERT', 'QUESTION_ALERT',
           'NONE_SCOPE_ANSI', 'printer', 'entry']

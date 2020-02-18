from snakypy.tools.decorators import use_unix_system
from snakypy.tools.ansi import NONE_SCOPE_ANSI, WARNING_ALERT


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

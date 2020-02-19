from snakypy.tools import use_unix_system
from snakypy.ansi import NONE_SCOPE_ANSI, WARNING_ALERT
from snakypy.ansi import (QUESTION_ALERT,
                          GREEN_COLOR,
                          MAGENTA_COLOR,
                          NONE_SCOPE_ANSI,
                          WARNING_ALERT,
                          ERROR_ALERT)

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
        

def list_options(title_, options_, answer, colorful, index):
    if colorful:
        printer(title_, '(Ctrl+C to Cancel)', style=QUESTION_ALERT)
    else:
        print(title_, '(Ctrl+C to Cancel)')
    count = 1
    for option in options_:
        if colorful:
            print(f'{GREEN_COLOR}[{count}] {MAGENTA_COLOR}{option}{NONE_SCOPE_ANSI}')
        else:
            print(f'[{count}] {option}')
        count += 1
    try:
        if colorful:
            pos = int(entry(answer, style=QUESTION_ALERT)) - 1
        else:
            pos = int(input(answer)) - 1
        assert pos > -1
        if index:
            return pos, options_[pos].lower()
        return options_[pos].lower()
    except Exception:
        if colorful:
            printer('Option invalid!', style=ERROR_ALERT)
        else:
            print('Option invalid!')
        return False
    except KeyboardInterrupt:
        if colorful:
            printer('Canceled by user.', style=WARNING_ALERT)
        else:
            print('Canceled by user.')
        return


def pick(title_, options_, *,
         answer='Answer:',
         index=False,
         colorful=False):
    try:
        while True:
            option = list_options(title_,
                                  options_,
                                  answer=answer,
                                  index=index,
                                  colorful=colorful)
            if option or option is None:
                break
        return option
    except Exception:
        raise Exception('An unexpected error occurs when using pick')


def billboard(text, ansicolor=None):
    import pyfiglet
    import snakypy
    from sys import platform

    ascii_banner = pyfiglet.figlet_format(text)
    if ansicolor and platform.startswith('win'):
        raise Exception('>>> You cannot activate the color using Windows OS.')
    if ansicolor:
        return snakypy.printer(ascii_banner, style=ansicolor)
    return print(ascii_banner)

# --------------------------------------------
# Function that does not use pyfliglet package
# --------------------------------------------
# def billboard2(text):
#     from snakypy.utilities.utilities import is_tool
#     from snakypy.console.commands import cmd_verbose
#
#     if is_tool('figlet'):
#         return cmd_verbose(f'figlet {text}', ret=False)
#     return print(text)


def cmd(command, shell=True, universal_newlines=True, ret=False, verbose=False):
    """
    Function that uses the subprocess library with Popen.
    The function receives a command as an argument and shows
    execution in real time.
    """
    from subprocess import Popen, PIPE

    process = Popen(command, shell=shell, stdout=PIPE,
                    universal_newlines=universal_newlines)
    if verbose:
        for line in iter(process.stdout.readline, ''):
            print(line.rstrip())
    if ret:
        r = process.poll()
        return r


def credence(app_name, app_version, app_url, data: dict, ansicolor=''):
    """
    Print project development credits. Example:
    data = {
        "credits": [{
            "full_name": "William da Costa Canin",
            "email": "william.costa.canin@gmail.com",
            "website": "http://williamcanin.me",
            "locale": "Brazil - SP"
        }]
    }
    """

    from datetime import date
    from snakypy.console import printer

    try:
        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" '\
                'must take a dictionary as an argument.'
            raise Exception(msg)

        # print(CYAN_COLOR, f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
        # print(f'{app_name} - Version {app_version}'.center(70))
        printer(f'{app_name} - Version {app_version}'.center(70), style=ansicolor)
        # print(f'{57 * "-"}\n'.center(75))
        printer(f'{57 * "-"}\n'.center(75), style=ansicolor)
        printer(f'Credence:\n'.center(70), style=ansicolor)
        for item in data['credence']:
            for key, value in item.items():
                # print(f'{key.title().replace("_", " ")}: {value}'.center(70))
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70), style=ansicolor)
        print()
        # print(f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
        # print(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70))
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70), style=ansicolor)
        # print(f'Home: {app_url}'.center(70))
        printer(f'Home: {app_url}'.center(70), style=ansicolor)
        # print(f'{57 * "-"}'.center(75), NONE_SCOPE_ANSI)
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
    except KeyError:
        msg = "The 'credence' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)


def loading(set_time=0.030, bar=False, header='[Loading]', colorful=False):
    """[summary]

    Keyword Arguments:
        set_time {float} -- [description] (default: {0.030})
        bar {bool} -- [description] (default: {False})
        header {str} -- [description] (default: {'[Loading]'})

    Returns:
        [type] -- [description]
    """

    import time
    import sys
    from snakypy.console.colorful import printer
    from snakypy.ansi import CYAN_COLOR, WARNING_ALERT

    if colorful:
        printer(header, style=CYAN_COLOR)
    else:
        print(header)
    try:
        if bar:
            for i in range(0, 100):
                time.sleep(set_time)  # 5 seconds
                width = (i + 1) / 4
                bar = f"[{'#' * int(width)} {' ' * (25 - int(width))}]"
                sys.stdout.write(u"\u001b[1000D" + bar)
                sys.stdout.flush()
            # return 'bar'
        for i in range(0, 100):
            time.sleep(set_time)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            # time.sleep(0.1)
            sys.stdout.write(f'{str(i + 1)}%')
            sys.stdout.flush()
        print()
        # return 'percent'
    except KeyboardInterrupt:
        if colorful:
            printer('\nCanceled by user.', style=WARNING_ALERT)
        else:
            print('\nCanceled by user.')
        return


__all__ = ['pick', 'entry', 'printer', 'billboard', 'cmd', 'credence', 'loading']


if __name__ == '__main__':
    title = 'What is your favorite programming language?'
    options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
    print(pick(title, options, colorful=True))

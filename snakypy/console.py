from snakypy.tools import use_unix_system
from snakypy.ansi import NONE, FG, BG, SGR


def verify_attr(*args):
    if args[0] and args[0] not in FG.__dict__.values():
        msg = 'Attribute invalid in parameter "foreground". Must receive from FG class.'
        raise AttributeError(msg)
    if args[1] and args[1] not in BG.__dict__.values():
        msg = 'Attribute invalid in parameter "background". Must receive from BG class.'
        raise AttributeError(msg)
    if args[2] and args[2] not in SGR.__dict__.values():
        msg = 'Attribute invalid in parameter "sgr". Must receive from SGR class.'
        raise AttributeError(msg)


@use_unix_system
def printer(*args, foreground='', background='', sgr='',
            sep=' ', end='\n', file=None, flush=False):

    verify_attr(foreground, background, sgr)

    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    text = ' '.join(map(str, lst))

    return print(f'{NONE}{sgr}{foreground}{background}{text}{NONE}',
                 sep=sep, end=end, file=file, flush=flush)


@use_unix_system
def entry(text, *, foreground='', background='', sgr='', jump_line='\n> '):

    verify_attr(foreground, background, sgr)

    try:
        return input(f'{NONE}{sgr}{foreground}{background}{text}{jump_line}{NONE}')
    except KeyboardInterrupt:
        print(f'\n{FG.WARNING} Aborted by user.{NONE}')


def pick_options(title_, options, answer, colorful=False, index=False):
    if not colorful:
        FG.QUESTION = ''
        FG.GREEN = ''
        FG.MAGENTA = ''
        FG.CYAN = ''
        FG.ERROR = ''
        FG.WARNING = ''

    printer(title_, '(Ctrl+C to Cancel)', foreground=FG.QUESTION)
    count = 1
    for option in options:
        print(f'{FG.GREEN}[{count}] {FG.MAGENTA}{option}{NONE}')
        count += 1
    try:
        pos = int(input(f'{FG.CYAN}{answer} {NONE}')) - 1
        assert pos > -1
        if index:
            return pos, options[pos].lower()
        return options[pos].lower()
    except Exception:
        printer('Option invalid!', foreground=FG.ERROR)
        return False
    except KeyboardInterrupt:
        printer('Canceled by user.', foreground=FG.WARNING)
        return


def pick(title, options, *,
         answer='Answer:',
         index=False,
         colorful=False):

    from sys import platform

    # DEPRECATED!
    # if colorful is True and platform.startswith('win'):
    #     raise Exception('>>> You cannot activate the color using Windows OS.')

    try:
        while True:
            option = pick_options(title,
                                  options,
                                  answer=answer,
                                  index=index,
                                  colorful=colorful)
            if option or option is None:
                break
        return option
    except Exception:
        raise Exception('An unexpected error occurs when using pick')


def billboard(text, foreground='', background=''):
    import pyfiglet
    import snakypy

    banner = pyfiglet.figlet_format(text)
    return snakypy.printer(banner, foreground=foreground, background=background)


# --------------------------------------------
# Function that does not use pyfliglet package
# --------------------------------------------
# def billboard(text, foreground='', background=''):
#     from snakypy.utilities.utilities import is_tool
#     from shutil import which
#     from snakypy.console import cmd
#
#     if which('figlet') is not None:
#         return cmd(f'figlet {text}', verbose=True)
#     return print(text)


def cmd(command, *args, shell=True, universal_newlines=True, ret=False, verbose=False):
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
            print(NONE, *args, line.rstrip(), NONE)
    if ret:
        r = process.poll()
        return r


def credence(app_name, app_version, app_url, data: dict, foreground=''):
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

    try:
        # denying_win(foreground)

        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" ' \
                  'must take a dictionary as an argument.'
            raise Exception(msg)

        # print(CYAN_COLOR, f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        # print(f'{app_name} - Version {app_version}'.center(70))
        printer(f'{app_name} - Version {app_version}'.center(70),
                foreground=foreground)
        # print(f'{57 * "-"}\n'.center(75))
        printer(f'{57 * "-"}\n'.center(75), foreground=foreground)
        printer(f'Credence:\n'.center(70), foreground=foreground)
        for item in data['credence']:
            for key, value in item.items():
                # print(f'{key.title().replace("_", " ")}: {value}'.center(70))
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70),
                        foreground=foreground)
        print()
        # print(f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        # print(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70))
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70),
                foreground=foreground)
        # print(f'Home: {app_url}'.center(70))
        printer(f'Home: {app_url}'.center(70), foreground=foreground)
        # print(f'{57 * "-"}'.center(75), NONE_SCOPE_ANSI)
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
    except KeyError:
        msg = "The 'credence' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)


def loading(set_time=0.030, bar=False, header='[Loading]', foreground=''):
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

    # denying_win(foreground)
    printer(header, foreground=foreground)
    try:
        if bar:
            for i in range(0, 100):
                time.sleep(set_time)  # 5 seconds
                width = (i + 1) / 4
                bar = f"[{'#' * int(width)}{' ' * (25 - int(width))}]"
                sys.stdout.write(u"\u001b[1000D" + bar)
                sys.stdout.flush()
            print()
            return
        for i in range(0, 100):
            time.sleep(set_time)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            # time.sleep(0.1)
            sys.stdout.write(f'{str(i + 1)}%')
            sys.stdout.flush()
        print()
        return
    except KeyboardInterrupt:
        printer('\nCanceled by user.', foreground=FG.WARNING)
        return


__all__ = ['pick', 'entry', 'printer', 'billboard', 'cmd', 'credence', 'loading']

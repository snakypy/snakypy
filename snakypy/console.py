from snakypy.tools import use_unix_system, denying_win
from snakypy.ansi import NONE, FG


@use_unix_system
def printer(*args, fg='', bg='', sep=' ', end='\n', file=None, flush: bool = False):
    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    text = ' '.join(map(str, lst))

    return print(f'{NONE}{fg}{bg}{text}{NONE}', sep=sep, end=end, file=file, flush=flush)


@use_unix_system
def entry(text, *, fg='', bg='', jump_line: str = '\n> '):
    try:
        return input(f'{NONE}{fg}{bg}{text}{jump_line}{NONE}')
    except KeyboardInterrupt:
        print(f'\n{FG.WARNING} Aborted by user.{NONE}')


def pick_options(title_, options_, answer, colorful=False, index=False):
    if colorful:
        printer(title_, '(Ctrl+C to Cancel)', fg=FG.QUESTION)
    else:
        print(title_, '(Ctrl+C to Cancel)')
    count = 1
    for option in options_:
        if colorful:
            print(f'{FG.GREEN}[{count}] {FG.MAGENTA}{option}{NONE}')
        else:
            print(f'[{count}] {option}')
        count += 1
    try:
        if colorful:
            pos = int(input(f'{FG.QUESTION}{answer} {NONE}')) - 1
        else:
            pos = int(input(answer)) - 1
        assert pos > -1
        if index:
            return pos, options_[pos].lower()
        return options_[pos].lower()
    except Exception:
        if colorful:
            printer('Option invalid!', fg=FG.ERROR)
        else:
            print('Option invalid!')
        return False
    except KeyboardInterrupt:
        if colorful:
            printer('Canceled by user.', fg=FG.WARNING)
        else:
            print('Canceled by user.')
        return


def pick(title_, options_, *,
         answer='Answer:',
         index=False,
         colorful=False):
    try:
        while True:
            option = pick_options(title_,
                                  options_,
                                  answer=answer,
                                  index=index,
                                  colorful=colorful)
            if option or option is None:
                break
        return option
    except Exception:
        raise Exception('An unexpected error occurs when using pick')


def billboard(text, fg='', bg=''):
    import pyfiglet
    import snakypy

    ascii_banner = pyfiglet.figlet_format(text)
    denying_win(fg, bg)
    if not fg == '' or not bg == '':
        return snakypy.printer(ascii_banner, fg=fg, bg=bg)
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


def credence(app_name, app_version, app_url, data: dict, fg=''):
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
        denying_win(fg)

        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" ' \
                  'must take a dictionary as an argument.'
            raise Exception(msg)

        # print(CYAN_COLOR, f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), fg=fg)
        # print(f'{app_name} - Version {app_version}'.center(70))
        printer(f'{app_name} - Version {app_version}'.center(70), fg=fg)
        # print(f'{57 * "-"}\n'.center(75))
        printer(f'{57 * "-"}\n'.center(75), fg=fg)
        printer(f'Credence:\n'.center(70), fg=fg)
        for item in data['credence']:
            for key, value in item.items():
                # print(f'{key.title().replace("_", " ")}: {value}'.center(70))
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70), fg=fg)
        print()
        # print(f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), fg=fg)
        # print(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70))
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70), fg=fg)
        # print(f'Home: {app_url}'.center(70))
        printer(f'Home: {app_url}'.center(70), fg=fg)
        # print(f'{57 * "-"}'.center(75), NONE_SCOPE_ANSI)
        printer(f'{57 * "-"}'.center(75), fg=fg)
    except KeyError:
        msg = "The 'credence' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)


def loading(set_time=0.030, bar=False, header='[Loading]', fg=''):
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

    denying_win(fg)
    printer(header, fg=fg)
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
        printer('\nCanceled by user.', fg=fg)
        return


__all__ = ['pick', 'entry', 'printer', 'billboard', 'cmd', 'credence', 'loading']

if __name__ == '__main__':
    title = 'What is your favorite programming language?'
    options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']

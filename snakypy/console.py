from snakypy.utils import decorators
from snakypy.ansi import NONE, FG, BG, SGR


def attr_foreground_background_sgr(*args):
    """
    Checks if the attributes of the functions that the foreground
    and background parameters are in accordance with their respective class.

    Arguments:
        args {str} -- It receives a certain number of arguments with an ansi code value.
    """
    if args[0] and args[0] not in FG.__dict__.values():
        msg = 'Attribute invalid in parameter "foreground". Must receive from FG class.'
        raise AttributeError(msg)
    if args[1] and args[1] not in BG.__dict__.values():
        msg = 'Attribute invalid in parameter "background". Must receive from BG class.'
        raise AttributeError(msg)
    if args[2] and args[2] not in SGR.__dict__.values():
        msg = 'Attribute invalid in parameter "sgr". Must receive from SGR class.'
        raise AttributeError(msg)


@decorators.use_unix_system
def printer(*args, foreground='', background='', sgr='',
            sep=' ', end='\n', file=None, flush=False):
    """A function that allows you to print colored text on the terminal.

    Keyword Arguments:
        foreground {str} -- This named argument should optionally receive
                            an object of class "snakypy.ansi.FG" for the foreground
                            color of the text. This object will be text with ansi code.
                            (default: {''})
        background {str} -- This named argument should optionally receive
                            an object of class "snakypy.ansi.BG" for the background
                            color of the text. This object will be text with ansi code.
                            (default: {''})
        sgr {str} -- This named argument should optionally receive
                     an object of class "snakypy.ansi.SGR" for the effect
                     of the text. This object will be text with ansi code.
                     (default: {''})
        sep {str} -- Separator between printer function objects. (default: {' '})

        end {str} -- Responsible for skipping a line after printing is finished. (default: {'\n'})
    """

    attr_foreground_background_sgr(foreground, background, sgr)

    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    text = ' '.join(map(str, lst))

    return print(f'{NONE}{sgr}{foreground}{background}{text}{NONE}',
                 sep=sep, end=end, file=file, flush=flush)


@decorators.use_unix_system
def entry(text, *, foreground='', background='', sgr='', jump_line='\n> '):
    """
    This function is derived from the input, but with the option of
    coloring it and some different formatting.
    Note: If you use Windows, the coloring option will not work.

    Arguments:
        text {object} -- Argument must receive an object

    Keyword Arguments:
        foreground {str} -- This named argument should optionally receive
                            an object of class "snakypy.ansi.FG" for the foreground
                            color of the text. This object will be text with ansi code.
                            (default: {''})
        background {str} -- This named argument should optionally receive
                            an object of class "snakypy.ansi.BG" for the background
                            color of the text. This object will be text with ansi code.
                            (default: {''})
        sgr {str} -- This named argument should optionally receive
                     an object of class "snakypy.ansi.SGR" for the effect
                     of the text. This object will be text with ansi code.
                     (default: {''})
        jump_line {str} -- Named argument that makes the action of skipping a line
                           and adding a greater sign to represent an arrow. You change
                           that argument to your liking. (default: {'\n> '})

    """

    attr_foreground_background_sgr(foreground, background, sgr)

    try:
        return input(f'{NONE}{sgr}{foreground}{background}{text}{jump_line}{NONE}')
    except KeyboardInterrupt:
        print(f'\n{FG.WARNING} Aborted by user.{NONE}')


def pick_options(title, options, answer, *, colorful=False, index=False):
    if not colorful:
        FG.QUESTION = ''
        FG.GREEN = ''
        FG.MAGENTA = ''
        FG.CYAN = ''
        FG.ERROR = ''
        FG.WARNING = ''

    printer(title, '(Ctrl+C to Cancel)', foreground=FG.QUESTION)
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


def pick(title, options: list, *,
         answer='Answer:',
         index=False,
         colorful=False):
    """Function that creates a menu of options in the terminal.

    Arguments:
        title {str} -- You should receive a text that will be the
                       title or the question with meaning in the alternatives.
        options {list} -- You should receive a list with certain elements
                          that will be part of the menu options.

    Keyword Arguments:
        answer {str} -- The text that will be shown before entering the answer.
                        You can change to your language. (default: {'Answer:'})
        index {bool} -- This argument for True, will return a tuple, where element 0,
                        will be the index of the option that the user chose, and
                        element 1 of the tuple, will be the name of the choice option.
                        Remember that the indexing of the menu is not the same as the
                        list of options because it starts with zero (0).
                        (default: {False})
        colorful {bool} -- If it has True, the menu color will be active, but it only
                           works if it is on a UNIX system, as the color uses Ansi Color.
                           If have Windows, no effect will appear.
                           (default: {False})
    """

    if not type(options) is list:
        raise TypeError('You must enter a list in the argument: options')

    if len(title) == 0:
        raise TypeError('The title cannot contain an empty element. Approached.')

    for option in options:
        if len(option) == 0:
            raise TypeError('The list cannot contain an empty element. Approached.')

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
    """[summary]

    Arguments:
        text {[type]} -- [description]

    Keyword Arguments:
        foreground {str} -- [description] (default: {''})
        background {str} -- [description] (default: {''})

    Returns:
        [type] -- [description]
    """
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

        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" ' \
                  'must take a dictionary as an argument.'
            raise Exception(msg)

        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        printer(f'{app_name} - Version {app_version}'.center(70),
                foreground=foreground)
        printer(f'{57 * "-"}\n'.center(75), foreground=foreground)
        printer(f'Credence:\n'.center(70), foreground=foreground)
        for item in data['credence']:
            for key, value in item.items():
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70),
                        foreground=foreground)
            print()
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70),
                foreground=foreground)
        printer(f'Home: {app_url}'.center(70), foreground=foreground)
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

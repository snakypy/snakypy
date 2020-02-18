import time
import sys
from snakypy.console.colorful import printer
from snakypy.tools.ansi import CYAN_COLOR, WARNING_ALERT
from subprocess import check_output
from subprocess import Popen, PIPE
from shutil import which
from snakypy.tools.decorators import use_unix_system


# ----------------------------------------
# You need the: $ pip install PyGObject
# ----------------------------------------
# @use_unix_system
# def notify(message, description, *, dialog="dialog-information"):
#     """Linux notification, a popup will appear.
#
#     Arguments:
#         message {[type]} -- [description]
#         description {[type]} -- [description]
#     """
#     import gi
#     gi.require_version('Notify', '0.7')
#     from gi.repository import Notify
#     Notify.init(message)
#     Notify.Notification.new(message, description, dialog).show()


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable.
    :param name: Enter the name of the program to check if it exists on the machine.

    Arguments:
        name {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    return which(name) is not None


def loading(set_time=0.030, bar=False, header='[Loading]', colorful=False):
    """[summary]

    Keyword Arguments:
        set_time {float} -- [description] (default: {0.030})
        bar {bool} -- [description] (default: {False})
        header {str} -- [description] (default: {'[Loading]'})

    Returns:
        [type] -- [description]
    """

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


@use_unix_system
def get_shell():
    """Function to get the currently activated shell.
    :return: Returns the name of the current shell.

    Returns:
        [type] -- [description]
    """

    s = check_output('echo $SHELL', shell=True, universal_newlines=True)
    lst = s.strip('\n').strip('').split('/')
    return lst[2]


def command_real_time(command, shell=True, universal_newlines=True):
    """
    Function that uses the subprocess library with Popen.
    The function receives a command as an argument and shows
    execution in real time.
    Returns:
        int - It will return either 1 or 0. Since 1 is an error
                return at the output of the command, zero is a
                success return.
    """

    process = Popen(command, shell=shell, stdout=PIPE,
                    universal_newlines=universal_newlines)
    for line in iter(process.stdout.readline, ''):
        print(line.rstrip())
    r = process.poll()
    return r


__all__ = ['get_shell', 'is_tool', 'loading', 'command_real_time']

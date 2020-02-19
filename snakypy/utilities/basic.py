import time
import sys
from snakypy.console.colorful import printer
from snakypy.ansi import CYAN_COLOR, WARNING_ALERT
from subprocess import check_output
from shutil import which
from snakypy.tools.system import use_unix_system


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


def dot_file_extension(filename):
    """[summary]

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    import re
    m = re.search(r'(?<=[^/\\]\.).*$', filename)
    if not m:
        return None

    return m.group(0)


__all__ = ['get_shell', 'is_tool', 'loading', 'dot_file_extension']

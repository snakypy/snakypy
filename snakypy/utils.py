from subprocess import check_output
from snakypy.tools import use_unix_system
from os.path import join


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


# @use_unix_system
def get_shell():
    """Function to get the currently activated shell.
    :return: Returns the name of the current shell.

    Returns:
        [type] -- [description]
    """

    from sys import platform

    if not platform.startswith('win'):
        s = check_output('echo $SHELL', shell=True, universal_newlines=True)
        lst = s.strip('\n').strip('').split('/')
        return lst[2]


def file_extension(filename):
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


def cleaner(directory, *file, level=None):
    """[summary]

    Arguments:
        directory {str} -- [description]

    Keyword Arguments:
        level {int} -- [description] (default: {False})

    Raises:
        FileNotFoundError: [description]
    """

    from shutil import rmtree
    from os import walk, remove
    from threading import Thread

    data = next(walk(directory))

    #: DANGER!
    if level == 0:
        for f in data[2]:
            remove(join(data[0], f))
        return 0

    #: DANGER!
    if level == 1:
        # r: root, r: directory, f: files
        for r, d, f in walk(directory, topdown=False):
            for item in d:
                t = Thread(target=rmtree(join(r, item)), args=())
                t.start()
        return 1

    try:
        if file:
            for f in file:
                remove(join(data[0], f))
            return
    except FileNotFoundError as err:
        msg = '>>> There was an error removing the files'
        raise FileNotFoundError(msg, err)


__all__ = ['get_shell', 'file_extension', 'cleaner']

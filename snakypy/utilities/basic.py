from subprocess import check_output
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


__all__ = ['get_shell', 'file_extension']

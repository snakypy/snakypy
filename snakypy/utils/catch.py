from subprocess import check_output
from snakypy.utils import decorators


@decorators.use_unix_system
def shell():
    """Function to get the currently activated shell.
    :return: Returns the name of the current shell.

    Returns:
        [type] -- [description]
    """

    from sys import platform

    if not platform.startswith('win'):
        s = check_output("echo $0", shell=True, universal_newlines=True)
        lst = s.strip('\n').strip('').split('/')
        return lst[2]


def extension(filename):
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


__all__ = ['shell', 'extension']

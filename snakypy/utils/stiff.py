from os import walk, remove
from os.path import join
from shutil import rmtree
from threading import Thread


def cleaner(directory, *file, level=None):
    """[summary]

    Arguments:
        directory {str} -- [description]

    Keyword Arguments:
        level {int} -- [description] (default: {False})

    Raises:
        FileNotFoundError: [description]
    """

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


__all__ = ['cleaner']

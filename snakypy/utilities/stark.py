def cleaner(dir_path, *args, remove_all=False, recursive=False):
    """[summary]

    Arguments:
        dir_path {[type]} -- [description]

    Keyword Arguments:
        remove_all {bool} -- [description] (default: {False})
        recursive {bool} -- In development. Not use. (default: {False})

    Raises:
        FileNotFoundError: [description]
    """

    from os import walk, remove
    from os.path import join

    try:
        data = next(walk(dir_path))

        # TODO: In development
        if recursive:
            # from glob import glob
            return

        if remove_all:
            for file in data[2]:
                remove(join(data[0], file))
                return
        for i in args:
            remove(join(data[0], i))
        return
    except FileNotFoundError as err:
        raise FileNotFoundError('>>> There was an error removing the files', err)

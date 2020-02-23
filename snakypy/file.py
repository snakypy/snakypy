from os.path import exists


def read(file_path, split=False):
    """Reads a text file.

    >>> import snakypy
    >>> file = '/tmp/my_file.txt'
    >>> snakypy.file.read(file)

    Arguments:
        **file_path {str}** -- You must receive the full/absolute file path.

    Keyword Arguments:
        **split {bool}** -- If this option is True, a list will be returned where \
        the breaks will be made using line skips. (default: {False})

    Returns:
        **[str|list]** -- By default it returns a string. If the option \
        split=True, a list of line breaks will be returned.
    """
    try:
        with open(file_path) as f:
            if split:
                return f.read().split('\n')
            return f.read()
    except FileNotFoundError as err:
        raise FileNotFoundError(f'>>> File "{file_path}" does not exist. {err}')


def create(content, file_path, force=False):
    """[summary]

    Arguments:
        content {[type]} -- [description]
        file_path {[type]} -- [description]

    Keyword Arguments:
        force {bool} -- [description] (default: {False})

    Raises:
        Exception: [description]

    Returns:
        [type] -- [description]
    """

    if not force and exists(file_path):
        raise FileExistsError(f'>>> The file {file_path} already exists, use force=True.')
    else:
        try:
            with open(file_path, 'w') as f:
                f.write(content)
                return True
        except Exception as err:
            raise Exception(f'>>> There was an error creating the file: {err}')


__all__ = ['read', 'create']

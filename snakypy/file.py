from os.path import exists


def read(file_path, split=False):
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
        raise FileExistsError(f'>>> The file {file_path} already exists, use Force=True.')
    else:
        try:
            with open(file_path, 'w') as f:
                f.write(content)
                return True
        except Exception as err:
            raise Exception(f'>>> There was an error creating the file: {err}')

import json
from os.path import exists


def read(file_path):
    """Function that reads JSON configuration file and returns data.

    Arguments:
        file_path {[type]} -- [description]

    Raises:
        FileNotFoundError: [description]
        Exception: [description]

    Returns:
        [type] -- [description]
    """

    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError as err:
        raise FileNotFoundError(f'>>> File not found {err}')
    except Exception:
        raise Exception(f'>>> There was an error reading the file: {file_path}')


def create(dictionary, file_path, force=False):
    """[summary]

    Arguments:
        dictionary {[type]} -- [description]
        file_path {[type]} -- [description]

    Keyword Arguments:
        force {bool} -- [description] (default: {False})

    Raises:
        Exception: [description]
        Exception: [description]

    Returns:
        [type] -- [description]
    """
    from os.path import splitext

    if splitext(file_path)[1] != '.json':
        raise Exception('The JSON file extension was not explicit.')
    if not force and exists(file_path):
        raise FileExistsError(f'>>> The file {file_path} already exists, use force=True.')
    else:
        try:
            if type(dictionary) is dict:
                with open(file_path, 'w') as f:
                    json.dump(dictionary, f, indent=4, separators=(',', ': '))
                    return True
            return False
        except Exception as err:
            raise Exception(f'>>> There was an error creating the file. {err}')


def update(file_path, content: dict):
    """Function to update json file. Receives two parameters,
    one (file_path) is the absolute path of the JSON file to
    be read, and the other (data) is the modified value.

    Arguments:
        file_path {[type]} -- [description]
        content {[type]} -- [description]

    Raises:
        Exception: [description]

    Returns:
        [type] -- [description]
    """
    try:
        if type(content) is dict:
            with open(file_path, 'w') as f:
                json.dump(content, f, indent=2, separators=(',', ': '))
            return True
        return False
    except Exception as err:
        msg = f'>>> Something unexpected happened while updating {file_path}'
        raise Exception(msg, err)

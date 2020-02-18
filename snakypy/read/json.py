import json


def json2(file_path):
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

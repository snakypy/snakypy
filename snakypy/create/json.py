import json
from os.path import exists


def json2(dictionary, file_path, force=False):
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
        raise FileExistsError(f'>>> The file {file_path} already exists, use Force=True.')
    else:
        try:
            if type(dictionary) is dict:
                with open(file_path, 'w') as f:
                    json.dump(dictionary, f, indent=4, separators=(',', ': '))
                    return True
            return False
        except Exception as err:
            raise Exception(f'>>> There was an error creating the file. {err}')

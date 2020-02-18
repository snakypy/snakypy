import json


def json2(file_path, content: dict):
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

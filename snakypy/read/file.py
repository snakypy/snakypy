def file(file_path, split=False):
    try:
        with open(file_path) as f:
            if split:
                return f.read().split('\n')
            return f.read()
    except FileNotFoundError as err:
        raise FileNotFoundError(f'>>> File "{file_path}" does not exist. {err}')

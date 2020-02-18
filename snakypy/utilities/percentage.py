def percentage(per, whole, *, operation=None, log=False):
    """[summary]

    Arguments:
        per {[type]} -- [description]
        whole {[type]} -- [description]

    Keyword Arguments:
        operation {[type]} -- [description] (default: {None})
        log {bool} -- [description] (default: {False})

    Returns:
        [type] -- [description]
    """
    option = {
        '+': lambda: whole + (whole * (per / 100)),
        '-': lambda: whole - (whole * (per / 100))
    }.get(operation, lambda: whole * (per / 100))()
    if log:
        if operation == '+':
            return f'>> {whole} + {per}% = {option:.2f}'
        elif operation == '-':
            return f'>> {whole} - {per}% = {option:.2f}'
        return f'>> {per}% of {whole} = {option:.2f}'
    return option

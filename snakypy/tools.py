def use_unix_system(func):
    """[summary]

    Arguments:
        func {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    from sys import platform

    def wrapper(*args, **kwargs):
        # Linux: startswith('linux')
        # OS X: startswith('darwin')
        # Windows: startswith('win')
        if platform.startswith('win'):
            msg = 'Invalid operating system (Windows). ' \
                  f'This function "{func.__name__}" is compatible with ' \
                  '"Linux" and "Mac OS X" systems only.'
            print(msg)
            exit(1)
        return func(*args, **kwargs)
    return wrapper


# DEPRECATED!
# def denying_win(*args, os='win'):
#     from sys import platform
#
#     # Linux: 'linux'
#     # OS X: 'darwin'
#     # Windows: 'win'
#
#     if args:
#         if (args != '') and platform.startswith(os):
#             raise Exception('>>> You cannot activate the color using Windows OS.')
#     else:
#         if platform.startswith(os):
#             msg = 'Invalid operating system (Windows). ' \
#                   f'This function "{__name__}" is compatible with ' \
#                   '"Linux" and "Mac OS X" systems only.'
#             raise Exception(msg)


__all__ = ['use_unix_system']

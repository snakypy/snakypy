def billboard(text, ansicolor=None):
    import pyfiglet
    import snakypy
    from sys import platform

    ascii_banner = pyfiglet.figlet_format(text)
    if ansicolor and platform.startswith('win'):
        raise Exception('>>> You cannot activate the color using Windows OS.')
    if ansicolor:
        return snakypy.printer(ascii_banner, style=ansicolor)
    return print(ascii_banner)

# --------------------------------------------
# Function that does not use pyfliglet package
# --------------------------------------------
# def billboard2(text):
#     from snakypy.utilities.utilities import is_tool
#     from snakypy.console.commands import cmd_verbose
#
#     if is_tool('figlet'):
#         return cmd_verbose(f'figlet {text}', ret=False)
#     return print(text)

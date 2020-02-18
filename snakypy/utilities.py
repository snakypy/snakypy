import json
from subprocess import check_output, Popen, PIPE
from os.path import exists, join
from snakypy.colorful import printer, CYAN_COLOR, WARNING_ALERT, NONE_SCOPE_ANSI
from snakypy.decorators import use_unix_system


def create_file(content, file_path, force=False):
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


def create_json(dictionary, file_path, force=False):
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


def read_json(file_path):
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


def update_json(file_path, content):
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


@use_unix_system
def get_shell():
    """Function to get the currently activated shell.
    :return: Returns the name of the current shell.

    Returns:
        [type] -- [description]
    """

    s = check_output('echo $SHELL', shell=True, universal_newlines=True)
    lst = s.strip('\n').strip('').split('/')
    return lst[2]


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable.
    :param name: Enter the name of the program to check if it exists on the machine.

    Arguments:
        name {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    from shutil import which

    return which(name) is not None


def cmd_popen(cmd, shell=True, bufsize=0):
    """Method for executing commands through "subprocess.Popen".

    Arguments:
        cmd {[type]} -- [description]

    Keyword Arguments:
        shell {bool} -- [description] (default: {True})
        bufsize {int} -- [description] (default: {0})
    """
    p = Popen(cmd, shell=shell, bufsize=bufsize, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    p.communicate()
    p.stdout.close()


def loading(set_time=0.030, bar=False, header='[Loading]', colorful=False):
    """[summary]

    Keyword Arguments:
        set_time {float} -- [description] (default: {0.030})
        bar {bool} -- [description] (default: {False})
        header {str} -- [description] (default: {'[Loading]'})

    Returns:
        [type] -- [description]
    """
    import time
    import sys

    if colorful:
        printer(header, style=CYAN_COLOR)
    else:
        print(header)
    try:
        if bar:
            for i in range(0, 100):
                time.sleep(set_time)  # 5 seconds
                width = (i + 1) / 4
                bar = f"[{'#' * int(width)} {' ' * (25 - int(width))}]"
                sys.stdout.write(u"\u001b[1000D" + bar)
                sys.stdout.flush()
            # return 'bar'
        for i in range(0, 100):
            time.sleep(set_time)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            # time.sleep(0.1)
            sys.stdout.write(f'{str(i + 1)}%')
            sys.stdout.flush()
        print()
        # return 'percent'
    except KeyboardInterrupt:
        if colorful:
            printer('\nCanceled by user.', style=WARNING_ALERT)
        else:
            print('\nCanceled by user.')
        return


@use_unix_system
def notify(message, description, *, dialog="dialog-information"):
    """Linux notification, a popup will appear.

    Arguments:
        message {[type]} -- [description]
        description {[type]} -- [description]
    """
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    Notify.init(message)
    Notify.Notification.new(message, description, dialog).show()


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


def command_real_time(command, shell=True, universal_newlines=True):
    """
    Function that uses the subprocess library with Popen.
    The function receives a command as an argument and shows
    execution in real time.
    Returns:
        int - It will return either 1 or 0. Since 1 is an error
                return at the output of the command, zero is a
                success return.
    """
    from subprocess import Popen, PIPE

    process = Popen(command, shell=shell, stdout=PIPE,
                    universal_newlines=universal_newlines)
    for line in iter(process.stdout.readline, ''):
        print(line.rstrip())
    r = process.poll()
    return r


def dot_file_extension(filename):
    """[summary]

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    import re
    m = re.search(r'(?<=[^/\\]\.).*$', filename)
    if not m:
        return None

    return m.group(0)


def cleaner(dir_path, *args, remove_all=False, recursive=False):
    """[summary]

    Arguments:
        dir_path {[type]} -- [description]

    Keyword Arguments:
        remove_all {bool} -- [description] (default: {False})
        recursive {bool} -- In development. Not use. (default: {False})

    Raises:
        FileNotFoundError: [description]
    """

    from os import walk, remove

    try:
        data = next(walk(dir_path))

        # TODO: In development
        if recursive:
            # from glob import glob
            return

        if remove_all:
            for file in data[2]:
                remove(join(data[0], file))
                return
        for i in args:
            remove(join(data[0], i))
        return
    except FileNotFoundError as err:
        raise FileNotFoundError('>>> There was an error removing the files', err)


def the_credits(app_name, app_version, app_url, data: dict):
    """
    Print project development credits. Example:
    data = {
        "credits": [{
            "full_name": "William da Costa Canin",
            "email": "william.costa.canin@gmail.com",
            "website": "http://williamcanin.me",
            "locale": "Brazil - SP"
        }]
    }
    """

    from datetime import date

    try:
        if type(data) is not dict:
            msg = f'>>> The function "{the_credits.__name__}" '\
                'must take a dictionary as an argument.'
            raise Exception(msg)

        print(CYAN_COLOR, f'{57 * "-"}'.center(75))
        print(f'{app_name} - Version {app_version}'.center(70))
        print(f'{57 * "-"}\n'.center(75))
        for item in data['credits']:
            for key, value in item.items():
                print(f'{key.title().replace("_", " ")}: {value}'.center(70))

        print()
        print(f'{57 * "-"}'.center(75))
        print(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70))
        print(f'Home: {app_url}'.center(70))
        print(f'{57 * "-"}'.center(75), NONE_SCOPE_ANSI)
    except KeyError:
        msg = "The 'credits' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)


__all__ = ['create_file', 'create_json', 'read_json', 'update_json',
           'get_shell', 'is_tool', 'dot_file_extension', 'cmd_popen', 'loading',
           'notify', 'percentage', 'command_real_time', 'cleaner',
           'the_credits']

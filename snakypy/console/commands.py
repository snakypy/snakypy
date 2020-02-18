def cmd_verbose(command, shell=True, universal_newlines=True, ret=False):
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
    if ret:
        r = process.poll()
        return r


__all__ = ['cmd_verbose']

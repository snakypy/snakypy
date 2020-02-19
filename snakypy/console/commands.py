def cmd(command, shell=True, universal_newlines=True, ret=False, verbose=False):
    """
    Function that uses the subprocess library with Popen.
    The function receives a command as an argument and shows
    execution in real time.
    """
    from subprocess import Popen, PIPE, check_call

    if verbose:
        process = Popen(command, shell=shell, stdin=PIPE, stdout=PIPE,
                        universal_newlines=universal_newlines)
        for line in iter(process.stdout.readline, ''):
            print(line.rstrip())
        if ret:
            r = process.poll()
            return r
    else:
        from subprocess import DEVNULL
        if ret:
            msg = 'You can only use the "ret=True" option with verbose mode. ' \
                  'Use verbose=True'
            raise Exception(msg)
        Popen(command, shell=shell, stdin=DEVNULL, stdout=DEVNULL,
              stderr=DEVNULL, universal_newlines=universal_newlines)


__all__ = ['cmd']

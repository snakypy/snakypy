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
    from snakypy.console.colorful import printer
    from snakypy.ansi import CYAN_COLOR, WARNING_ALERT

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

def credence(app_name, app_version, app_url, data: dict, ansicolor=''):
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
    from snakypy.console import printer

    try:
        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" '\
                'must take a dictionary as an argument.'
            raise Exception(msg)

        # print(CYAN_COLOR, f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
        # print(f'{app_name} - Version {app_version}'.center(70))
        printer(f'{app_name} - Version {app_version}'.center(70), style=ansicolor)
        # print(f'{57 * "-"}\n'.center(75))
        printer(f'{57 * "-"}\n'.center(75), style=ansicolor)
        printer(f'Credence:\n'.center(70), style=ansicolor)
        for item in data['credence']:
            for key, value in item.items():
                # print(f'{key.title().replace("_", " ")}: {value}'.center(70))
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70), style=ansicolor)
        print()
        # print(f'{57 * "-"}'.center(75))
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
        # print(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70))
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70), style=ansicolor)
        # print(f'Home: {app_url}'.center(70))
        printer(f'Home: {app_url}'.center(70), style=ansicolor)
        # print(f'{57 * "-"}'.center(75), NONE_SCOPE_ANSI)
        printer(f'{57 * "-"}'.center(75), style=ansicolor)
    except KeyError:
        msg = "The 'credence' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)

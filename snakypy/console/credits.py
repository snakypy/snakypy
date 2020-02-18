from snakypy.tools.system import use_unix_system


@use_unix_system
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
    from snakypy.tools.ansicolor import CYAN_COLOR, NONE_SCOPE_ANSI

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

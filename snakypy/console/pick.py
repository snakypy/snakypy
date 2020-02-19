from snakypy.console.colorful import printer, entry
from snakypy.ansi import (QUESTION_ALERT,
                          GREEN_COLOR,
                          MAGENTA_COLOR,
                          NONE_SCOPE_ANSI,
                          WARNING_ALERT,
                          ERROR_ALERT)


def list_options(title_, options_, answer, colorful, index):
    if colorful:
        printer(title_, '(Ctrl+C to Cancel)', style=QUESTION_ALERT)
    else:
        print(title_, '(Ctrl+C to Cancel)')
    count = 1
    for option in options_:
        if colorful:
            print(f'{GREEN_COLOR}[{count}] {MAGENTA_COLOR}{option}{NONE_SCOPE_ANSI}')
        else:
            print(f'[{count}] {option}')
        count += 1
    try:
        if colorful:
            pos = int(entry(answer, style=QUESTION_ALERT)) - 1
        else:
            pos = int(input(answer)) - 1
        assert pos > -1
        if index:
            return pos, options_[pos].lower()
        return options_[pos].lower()
    except Exception:
        if colorful:
            printer('Option invalid!', style=ERROR_ALERT)
        else:
            print('Option invalid!')
        return False
    except KeyboardInterrupt:
        if colorful:
            printer('Canceled by user.', style=WARNING_ALERT)
        else:
            print('Canceled by user.')
        return


def pick(title_, options_, *,
         answer='Answer:',
         index=False,
         colorful=False):
    try:
        while True:
            option = list_options(title_,
                                  options_,
                                  answer=answer,
                                  index=index,
                                  colorful=colorful)
            if option or option is None:
                break
        return option
    except Exception:
        raise Exception('An unexpected error occurs when using pick')


__all__ = ['pick']


if __name__ == '__main__':
    title = 'What is your favorite programming language?'
    options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
    print(pick(title, options, colorful=True))

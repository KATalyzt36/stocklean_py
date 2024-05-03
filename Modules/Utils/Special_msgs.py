from Modules.Utils import Color


def red(input: str):
    return print(f'{Color.RED}{input}{Color.RESET}')


def yellow(input: str):
    return print(f'{Color.YELLOW}{input}{Color.RESET}')


def green(input: str):
    return print(f'{Color.GREEN}{input}{Color.RESET}')


def cyan(input: str):
    return print(f'{Color.CYAN}{input}{Color.RESET}')
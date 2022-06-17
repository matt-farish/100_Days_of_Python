from os import system, name


def clear():
    """Clears the screen."""
    if name == 'nt':
        system('cls')

    else:
        system('clear')
def colorize(color):
    colors = {
        'black': '\033[1;30',
        'red': '\033[1;31',
        'green': '\033[1;32',
        'yellow': '\033[1;33',
        'blue': '\033[1;34',
        'purple': '\033[1;35',
        'cyan': '\033[1;36',
        'white': '\033[1;37',
    }

    try:
        return colors[color]
    except KeyboardInterrupt:
        return f'\033[1;31ERROR! THE USER DID NOT TYPE ANYTHING\033[m'


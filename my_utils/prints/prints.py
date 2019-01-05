import my_utils.prints.colors as cl


def color(color, name, value=''):
    print(color + str(name) + cl.ENDC, value)


def red(name, value=''):
    color(cl.FAIL, name, value=value)


def green(name, value=''):
    color(cl.OKGREEN, name, value=value)


def blue(name, value=''):
    color(cl.OKBLUE, name, value=value)


if __name__ == '__main__':
    red('ciao', 5)
    green('ciao', 5)
    blue('ciao', 5)

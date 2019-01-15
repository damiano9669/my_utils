import my_utils.prints.colors as cl


def color(color, text):
    return input(color + str(text) + cl.ENDC)


def red(text):
    return color(cl.FAIL, text)


def green(text):
    return color(cl.OKGREEN, text)


def blue(text):
    return color(cl.OKBLUE, text)


if __name__ == '__main__':
    ans = red('test\n')
    print(ans)

    ans = green('test\n')
    print(ans)

    ans = blue('test\n')
    print(ans)

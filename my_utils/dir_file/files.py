import os
from os import listdir
from os.path import isfile, join


def write(path, text):
    """
    :param path: file path
    :param text: text to write
    :return:
    """
    file = open(path, 'r+')
    file.write(text)
    file.close()
    return True


def read(path):
    """
    :param path: file path
    :return:
    """
    file = open(path, 'r+')
    text = file.read()
    file.close()
    return text


def add_line(path, line):
    """
    :param path: file path
    :param line: line to add
    :return:
    """
    values = get_lines(path)
    values.append(line)
    with open(path, 'w') as file:
        file.writelines('\n'.join(values))
    return True


def erase(path):
    """
    :param path: file path
    :return:
    """
    open(path, 'w').close()
    return True


def erase_line(path, n_line):
    """
    :param path: file path
    :param n_line: line to erase in the file
    :return:
    """
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    file = open(path, 'w')
    for i, line in enumerate(lines):
        if i != n_line:
            file.write(line)
    file.close()
    return True


def get_num_lines(path):
    """
    :param path: file path
    :return: number lines
    """
    file = open(path, 'r')
    num_lines = len(file.readlines())
    file.close()
    return num_lines


def get_files_in_dir(path):
    """
    :param path: file path
    :return: list of files in the directory
    """
    return [file for file in listdir(path) if isfile(join(path, file))]


def get_lines(path):
    """
    :param path: file path
    :return: list list of lines
    """
    file = open(path, 'r', encoding = "ISO-8859-1")
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line) > 0]
    file.close()
    return lines


def check_if_file_exists(path, create=False):
    """
    :param path: file path
    :param create: create file if does not exist?
    :return:
    """
    if not os.path.exists(path):
        if create:
            file = open(path, 'w')
            file.close()
        return False
    else:
        return True


if __name__ == '__main__':
    path = '...'

    if check_if_file_exists(path):
        erase(path)

    print(check_if_file_exists(path, create=True))

    print(get_num_lines(path))

    print(write(path, 'line 1'))

    print(write(path, 'line 2'))

    print(read(path))

    print(add_line(path, 'line 3'))

    print(erase_line(path, 0))

    print(add_line(path, 'line 4'))

    print(get_num_lines(path))

    print(get_lines(path))

    print(check_if_file_exists(path))

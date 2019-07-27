import os


def get_sub_dirs(path):
    """
    :param path: directory path
    :return: list of sub directories
    """
    return [os.path.join(path, dI) for dI in os.listdir(path) if os.path.isdir(os.path.join(path, dI))]


def check_if_dir_exists(path, create=False):
    """
    :param path: directory path
    :param create: create dir if does not exist?
    :return:
    """
    if not os.path.isdir(path):
        if create:
            os.mkdir(path)
        return False
    else:
        return True


if __name__ == '__main__':
    path = '...'
    sub_dirs = get_sub_dirs(path)

    print(sub_dirs)

    new_dir = '...'

    exist = check_if_dir_exists(new_dir, create=True)
    print(exist)

    sub_dirs = get_sub_dirs(path)
    print(sub_dirs)

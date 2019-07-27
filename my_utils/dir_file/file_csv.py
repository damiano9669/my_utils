import pandas as pd

import my_utils.data_structures.dictionaries as dt
import my_utils.dir_file.files as fl


def save_list(path, list):
    """
    :param path: csv path
    :param list: list of lines to write in the file
    :return:
    """
    df = pd.DataFrame(list, index=None)
    df.to_csv(path, mode='a', header=False, index=None)


def save_dict(path, dict, pop=False, max_num_lines=200):
    """
        save a dict in csv file
    :param path: csv path
    :param dict: dictionary
    :param pop: pop or not?
    :param max_num_lines: max num lines per file
    :return:
    """
    new_dict = dt.scalar_to_list(dict)
    df = pd.DataFrame(new_dict, index=None)

    fl.check_if_file_exists(path, create=True)

    n_lines = fl.get_num_lines(path)
    if n_lines == 0:
        # save with headers
        df.to_csv(path, mode='a', header=True, index=None)
    else:
        # pop if necessary
        if pop:
            while n_lines > max_num_lines:
                fl.erase_line(path, 1)
                n_lines = fl.get_num_lines(path)
        # save without headers
        df.to_csv(path, mode='a', header=False, index=None)
    return True


def get_dicts(path):
    """
        read csv file and get list of dictionaries
    :param path: csv path
    :return: list of dictionaries
    """
    df = pd.read_csv(path)
    keys = df.keys()
    values = df.values
    dictionaries = []
    for line in values:
        dictionaries.append(dict(zip(keys, line)))
    return dictionaries


def get_last_dict(path):
    """
        read last line of csv file
    :param path: csv path
    :return:
    """
    return get_dicts(path)[-1]


def get_column(path, i_col):
    """
        get column of csv file
    :param path: csv path
    :param i_col: column to extract
    :return: list of value
    """
    dict_list = get_dicts(path)

    column = []
    for dict in dict_list:
        column.append(dict[list(dict.keys())[i_col]])
    return column


if __name__ == '__main__':
    path = '...'

    dict_a = {
        'a': 5,
        'b': 4,
        'c': 78,
        'd': 25
    }

    save_dict(path, dict_a)
    dict_a = dt.sum_value(dict_a, 5)
    save_dict(path, dict_a)
    dict_a = dt.sum_value(dict_a, 2.3)
    save_dict(path, dict_a)

    print(get_dicts(path))

    print(get_last_dict(path))

    print(get_column(path, 2))

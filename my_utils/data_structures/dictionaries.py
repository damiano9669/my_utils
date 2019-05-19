import operator


def get_max_key(dict):
    """
        get key based on max value
    :param dict: dictionary
    :return:
    """
    return max(dict.items(), key=operator.itemgetter(1))[0]


def get_max_item(dict):
    """
    :param dict: dictionary
    :return: dictionary {key: value}
    """
    key = get_max_key(dict)
    return {key: dict[key]}


def get_value(dict):
    """
        get value of a dict with only one item
    :param dict: dictionary
    :return: value
    """
    value = list(dict.values())[0]
    return value


def get_key(dict):
    """
        get key of a dict with only one item
    :param dict: dictionary
    :return: value
    """
    value = list(dict.keys())[0]
    return value


def sum_value(dict, value):
    """
        add value at all items
    :param dict: dictionary
    :param value: value to add
    :return: dictionary
    """
    new_dict = {}
    for key in dict:
        new_dict[key] = dict[key] + value

    return new_dict


def sum_dicts(dict1, dict2, k1=1., k2=1., r=2):
    """
        sum two dictionaries elem per elem
    :param dict1: dictionary
    :param dict2: dictionary
    :param k1: weight coefficient
    :param k2: weight coefficient
    :return: dictionary of float values
    """
    result = {}
    for item in dict1:
        result[item] = round(float(dict1[item] * k1 + dict2[item] * k2), r)

    return result


def scalar_to_list(dict):
    """
        convert scalar values to elements of list
    :param dict: dictionary
    :return: dictionary
    """
    new_dict = {}
    for key, value in dict.items():
        new_dict[key] = [value]

    return new_dict


def is_equal(dict1, dict2):
    """
        are dicts equal?
    :param dict1: dictionary
    :param dict2: dictionary
    :return:
    """
    if len(dict1) == len(dict2):
        for item in dict1:
            if dict1[item] != dict2[item]:
                return False
        return True
    else:
        return False


def is_equal_float(dict1, dict2):
    """
        are dicts equal? (dicts containing float)
    :param dict1: dictionary
    :param dict2: dictionary
    :return:
    """
    if len(dict1) == len(dict2):
        for item in dict1:
            if float(dict1[item]) != float(dict2[item]):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    dict_1 = {
        'a': '10.1',
        'b': 123,
        'c': 54
    }

    dict_2 = {
        'a': 10.1,
        'b': 123,
        'c': 54
    }

    print(is_equal_float(dict_1, dict_2))

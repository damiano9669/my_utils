import numpy as np


def calc_percentage(value, percentage):
    """
        calculate value percentage
    :param value: reference value
    :param percentage: percentage
    :return: percentage of the value
    """
    result = percentage * np.abs(value) / 100.
    return result


def add_percentage(value, percentage):
    """
        add percentage to value
        (sum and sub)
    :param value: reference value
    :param percentage: percentage
    :return:
    """
    add = calc_percentage(value, percentage)
    return value + add


def difference_percentage(old_value, new_value):
    """
        calculate difference percentage
        between two values
    :param old_value:
    :param new_value:
    :return:
    """
    if old_value != 0:
        ratio = new_value / old_value
        diff = (ratio - 1) * 100.

        return diff
    else:
        return np.NaN


if __name__ == '__main__':
    val_a = 85.23
    print(val_a)
    val_b = add_percentage(val_a, 5.)
    print(val_b)
    diff = difference_percentage(val_a, val_b)
    print(diff)
    add = add_percentage(val_b, 10.)
    print(add)

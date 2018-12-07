import numpy as np


def polynomial(y, rank):
    x = range(len(y))
    coeffs = np.polyfit(x, y, rank)
    new_y = []
    for xi in x:

        new_xi = 0

        for i in range(rank + 1):
            coef = coeffs[len(coeffs) - 1 - i]
            new_xi += coef * xi ** i
        new_y.append(new_xi)

    return new_y


if __name__ == '__main__':
    pass

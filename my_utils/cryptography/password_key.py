import binascii
import os


def generate_password(length=8):
    """
        to generate a general password
    :param length:
    :return: password bytes
    """
    return binascii.hexlify(os.urandom(length))


if __name__ == '__main__':
    print(generate_password())

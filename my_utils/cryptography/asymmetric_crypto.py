import base64
import os

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

import my_utils.dir_file.directories as d
import my_utils.dir_file.files as fl


def generate_keys():
    """
    :return: private and public keys in RSA_object
    """
    # key length must be a multiple of 256 and >= 1024
    modulus_length = 256 * 4
    private_key = RSA.generate(modulus_length, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key


def encrypt(raw_message, public_key):
    """
        to encrypt message
    :param raw_message: string message to encrypt
    :param public_key: RSA_object key
    :return:
    """
    cipher = PKCS1_v1_5.new(public_key)
    ciphertext = base64.b64encode(cipher.encrypt(raw_message))
    return ciphertext


def decrypt(encrypted_msg, private_key):
    """
        to decrypt message
    :param encrypted_msg: byte array encrypted message
    :param private_key: RSA_object key
    :return:
    """
    cipher = PKCS1_v1_5.new(private_key)
    plaintext = cipher.decrypt(base64.b64decode(encrypted_msg), 'Error while decrypting')

    return plaintext


def save_key(key, path):
    """
        to save in txt the RSA_object key
    :param key: RSA_object
    :param path: file_path
    :return:
    """
    key_string = key.exportKey()
    fl.check_if_file_exists(path, create=True)
    fl.write(path, key_string.decode('utf-8'))
    return True


def load_key(path):
    """
        to load the key from file txt
    :param path: file_txt of the key
    :return: RSA_object key
    """
    key_string = fl.read(path)
    RSA_key_obj = RSA.importKey(key_string)
    return RSA_key_obj


if __name__ == '__main__':

    keys_path = 'my_keys'
    pub_file = 'pub.txt'
    priv_file = 'priv.txt'

    pub_path = os.path.join(keys_path, pub_file)
    priv_path = os.path.join(keys_path, priv_file)

    d.check_if_dir_exists(keys_path, create=True)
    if fl.check_if_file_exists(pub_path):
        fl.erase(pub_path)
        fl.erase(priv_path)

    priv_key, pub_key = generate_keys()
    save_key(pub_key, pub_path)
    save_key(priv_key, priv_path)

    priv_key = load_key(priv_path)
    pub_key = load_key(pub_path)

    message = b'Un messaggio da crittare.'
    print(message)

    encry = encrypt(message, pub_key)
    print(encry)

    decry = decrypt(encry, priv_key)
    print(decry)

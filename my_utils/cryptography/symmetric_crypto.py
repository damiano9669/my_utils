import base64

from cryptography.fernet import Fernet


def generate_key():
    """
        to generate the key
    :return: key
    """
    key = Fernet.generate_key()
    return key


def encrypt(raw_message, key):
    """
        to encrypt the message
    :param raw_message: string byte message to encrypt
    :param key: key
    :return: encoded and encrypted message
    """
    fernet = Fernet(key)
    encrypted_msg = fernet.encrypt(raw_message)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg


def decrypt(encoded_encrypted_msg, key):
    """
        to decrypt message
    :param encoded_encrypted_msg: message encrypted
    :param key: key
    :return: decoded and decrypted message
    """
    fernet = Fernet(key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = fernet.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


if __name__ == '__main__':
    key = generate_key()
    print(key)

    message = b'Un messaggio da crittare.'
    print(message)

    encry = encrypt(message, key)
    print(encry)

    decry = decrypt(encry, key)
    print(decry)

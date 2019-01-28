from Crypto import Random
from Crypto.PublicKey import RSA
import base64


def generate_keys():
    """
    :return: private and public keys
    """
    # key length must be a multiple of 256 and >= 1024
    modulus_length = 256 * 4
    private_key = RSA.generate(modulus_length, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key


def encrypt(raw_message, public_key):
    """
        to encrypt message
    :param raw_message: byte string -> message to encrypt
    :param public_key: public key
    :return: encoded in base64 and encrypted message
    """
    encrypted_msg = public_key.encrypt(raw_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg


def decrypt(encoded_encrypted_msg, private_key):
    """
        to decrypt message
    :param encoded_encrypted_msg: message encrypted
    :param private_key: private key
    :return: decoded and decrypted message
    """
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = private_key.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


if __name__ == '__main__':
    priv_key, pub_key = generate_keys()
    print(priv_key, pub_key)

    message = b'Un messaggio da crittare.'
    print(message)

    encry = encrypt(message, pub_key)
    print(encry)

    decry = decrypt(encry, priv_key)
    print(decry)

from yaml import load
from json import loads, dumps
from datetime import datetime
from Crypto.Cipher import AES
import base64
import sys


# read config.yaml
def read_config():
    # Open the config file
    with open('config/config.yaml') as data_file:
        # return the json object as a python object
        return load(data_file)


def write_log(message):
    sys.stdout.write(''.join(['[', str(datetime.now()), '] ', message, "\n"]))


def write_json_log(message):
    sys.stdout.write(dumps(message) + "\n")


def write_json_error(message):
    sys.stderr.write(dumps(message) + "\n")


def write_error(message):
    sys.stderr.write(''.join(['[', str(datetime.now()), '] ', message, "\n"]))


def __decrypt_string(encrypted_data, key):
    unpad = lambda s: s[0:-ord(s[-1])]
    AES.key_size = 256
    parts = encrypted_data.split(':')
    iv = base64.b64decode(parts[1])
    key = base64.b64decode(key)
    encrypted_message = base64.b64decode(parts[0])

    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)

    decrypted = unpad(crypt_object.decrypt(encrypted_message))

    return str(decrypted)


def _read_message(json_string):
    return loads(json_string)


def read_encrypted_message(encrypted_data, key):
    decrypted_json = __decrypt_string(encrypted_data, key)
    return _read_message(decrypted_json)


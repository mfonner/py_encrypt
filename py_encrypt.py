#!/usr/bin/env python3

import sys
import secrets
import string
from cryptography.fernet import Fernet

# Check that we are using Python 3 to run
try:
    if sys.version_info[0] < 3:
        raise Exception("This script requires Python 3")
except Exception:
    print("This script requires Python 3")
    sys.exit()

# Generate a password (16 characters by default, could be configurable)
def gen_password(length=16):

    charset = string.ascii_letters + string.digits + string.punctuation

    pwd = "".join([secrets.choice(charset) for _ in range(0, length)])

    return pwd

# Gets key generated in gen_key.py and returns it
def get_key():

    with open('key.key', 'rb') as file:
        key = file.read()

    return key

# Encrypts file with key from get_key()
def encrypt_file(pwd):

    key = get_key()
    fernet = Fernet(key)

    pwd_bytes = bytes(pwd, 'utf-8')

    cipher = fernet.encrypt(pwd_bytes)

    with open('pwd.encrypted', 'wb') as file:
        file.write(cipher)

# Reads the cipher text file to prep for decryption
def read_cipher():

    with open('pwd.encrypted', 'rb') as file:
        encrypted_file = file.read()

    return encrypted_file

# Decrypts file (primarily here for PoC and debugging)
def decrypt_file():

    key = get_key()
    fernet = Fernet(key)

    encrytped_file = read_cipher()

    plain_text_bytes = fernet.decrypt(encrytped_file)
    plain_text = plain_text_bytes.decode('utf-8')

    return plain_text


def main():

    pw = gen_password()

    # Prints and saves plain text password as a text file, useful for debugging
    # Uncomment the next 3 lines of code to enable this feature
    # TODO: Add this feature as a command line arg 

    #print(pw)
    #with open('pwd.txt', 'w') as file:
    #    file.write(pw)

    encrypt_file(pw)

    plain_text = decrypt_file()

    # Another line useful for debugging/verificaiton of decryption process
    # Uncomment the print statement below to enable
    # TODO: Add this to the command line args 

    print(plain_text)

if __name__ == '__main__':
    main()

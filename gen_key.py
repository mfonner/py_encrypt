#!/usr/bin/env python3

from cryptography.fernet import Fernet
import sys

# Check that we are using Python 3 to run
try:
    if sys.version_info[0] < 3:
        raise Exception("This script requires Python 3")
except Exception:
    print("This script requires Python 3")
    sys.exit()

key = Fernet.generate_key()

with open('key.key', 'wb') as file:
    file.write(key)

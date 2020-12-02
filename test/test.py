# -*- coding: utf-8 -*-

import os
import sys

cwd = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, os.path.split(cwd)[0])

from tea_encrypt import EncryptStr, DecryptStr, __version__

k = b"de1182b0f4203cad8d2ec629e35403d7"
v = b"this is a test"

print("version: %s" % __version__)

encrypt_bytes = EncryptStr(v, k)
print(encrypt_bytes)

original_bytes = DecryptStr(encrypt_bytes, k)
print(original_bytes)
# -*- coding: utf-8 -*-

from tea_encrypt.utils.pyctea import tea_str_c_encrypt, tea_str_c_decrypt
from tea_encrypt.utils.pytea import str_encrypt, str_decrypt

k = b"de1182b0f4203cad8d2ec629e35403d7"
v = b"this is a test"

encrypt_bytes = tea_str_c_encrypt(v, k)
print(encrypt_bytes)

original_bytes = tea_str_c_decrypt(encrypt_bytes, k)
print(original_bytes)

encrypt_bytes = tea_str_c_encrypt(v, k)
print(encrypt_bytes)

original_bytes = str_decrypt(encrypt_bytes, k)
print(original_bytes)

encrypt_bytes = str_encrypt(v, k)
print(encrypt_bytes)

original_bytes = tea_str_c_decrypt(encrypt_bytes, k)
print(original_bytes)
# -*- coding: utf-8 -*-

import struct
import logging
import binascii
from random import seed
from random import randint

import numpy

from tea_encrypt import strtea

LOG = logging.getLogger(__name__)

OP_64 = 0xffffffffffffffff


def tea_str_c_encrypt(v, k, iterations = 32):
    '''
    v is bytes or string
    k is md5 bytes or string
    iterations must be 32 or 64
    return bytes
    '''
    v = v.encode("utf-8") if isinstance(v, str) else v
    k = k.decode() if isinstance(k, bytes) else k
    # ascii str to bin
    k = binascii.unhexlify(k)
    result = b""
    end_char = b"\0"
    fill_n_or = 0xf8
    v_length = len(v)
    fill_n = (8 - (v_length + 2))%8 + 2
    fill_s = b""
    fill_bytes = []
    for i in range(fill_n):
        fill_bytes.append(randint(0, 0xff))
    fill_s = bytes(fill_bytes)
    v = bytes([(fill_n - 2) | fill_n_or]) + fill_s + v + end_char * 7
    k0, k1, k2, k3 = struct.unpack(">LLLL", k)
    k_c = numpy.ascontiguousarray([k0, k1, k2, k3], dtype = numpy.uint32)
    v_new_length = len(v) # after add '\0'
    v_pack_str = ">" + "LL"*int(v_new_length/8)
    tube_v = struct.unpack(v_pack_str, v)
    v_c = numpy.ascontiguousarray(tube_v, dtype = numpy.uint32)
    strtea.tea_c_str_encrypt(v_c, k_c, int(v_new_length/4), iterations)
    for n,i in enumerate(v_c):
        result += struct.pack(">L", i)
    return result


def tea_str_c_decrypt(v, k, iterations = 32):
    '''
    v is bytes or string
    k is md5 bytes or string
    iterations must be 32 or 64
    return bytes
    '''
    k = k.decode() if isinstance(k, bytes) else k
    iterations = 64 if iterations > 32 else 32
    # ascii to bin
    if isinstance(v, str):
        v = binascii.unhexlify(v)
    k = binascii.unhexlify(k)
    result = b""
    v_length = len(v)
    pos = 0
    k0, k1, k2, k3 = struct.unpack(">LLLL", k)
    k_c = numpy.ascontiguousarray([k0, k1, k2, k3], dtype = numpy.uint32)
    v_pack_str = ">" + "LL"*int(v_length/8)
    tube_v = struct.unpack(v_pack_str, v)
    v_c = numpy.ascontiguousarray(tube_v, dtype = numpy.uint32)
    pos = strtea.tea_c_str_decrypt(v_c, k_c, int(v_length/4), iterations)
    plaintext = struct.pack('>L', pos)
    pos = (plaintext[0] & 0x07) + 2
    # pos = 6 # tmp
    for n,i in enumerate(v_c):
        result += struct.pack(">L", i)
    if result[-7:] != b"\0" * 7: return ""
    return result[pos + 1: -7]

# -*- coding: utf-8 -*-
'''
Created on 2014-12-26
@summary:  tea
@author: fiefdx
''' 
import numpy as np
cimport numpy as np
from libc.stdint cimport uint32_t

cimport strtealink

def tea_c_encrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, tea_sum):
    strtealink.tea_encrypt (<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> tea_sum)

def tea_c_decrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, tea_sum):
    strtealink.tea_decrypt (<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> tea_sum)

def tea_c_str_encrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, length, tea_sum):
    strtealink.tea_str_encrypt(<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> length, <uint32_t> tea_sum)

def tea_c_str_decrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, length, tea_sum):
    pos = strtealink.tea_str_decrypt(<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> length, <uint32_t> tea_sum)
    return pos

def tea_c_str_pointer_encrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, length, tea_sum):
    strtealink.tea_str_pointer_encrypt(<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> length, <uint32_t> tea_sum)

def tea_c_str_pointer_decrypt(np.ndarray[np.uint32_t, ndim=1] v, np.ndarray[np.uint32_t, ndim=1] k, length, tea_sum):
    pos = strtealink.tea_str_pointer_decrypt(<uint32_t*> v.data, <uint32_t*> k.data, <uint32_t> length, <uint32_t> tea_sum)
    return pos
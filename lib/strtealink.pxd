# -*- coding: utf-8 -*-
'''
Created on 2014-05-25
@summary: strtealink.pxd for tea C lib
@author: fiefdx
''' 
cimport numpy as np
from libc.stdint cimport uint32_t, uint64_t

cdef extern from "strtea.h":
    void tea_encrypt (uint32_t * v, uint32_t * k, uint32_t tea_sum)
    void tea_decrypt (uint32_t * v, uint32_t * k, uint32_t tea_sum)
    void tea_str_encrypt(uint32_t* v, uint32_t* k, uint32_t length, uint32_t tea_sum)
    uint32_t tea_str_decrypt(uint32_t* v, uint32_t* k, uint32_t length, uint32_t tea_sum)
    void tea_str_pointer_encrypt(uint32_t* v, uint32_t* k, uint32_t length, uint32_t tea_sum)
    uint32_t tea_str_pointer_decrypt(uint32_t* v, uint32_t* k, uint32_t length, uint32_t tea_sum)

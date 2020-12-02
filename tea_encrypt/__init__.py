# -*- coding: utf-8 -*-

import logging

LOG = logging.getLogger(__name__)

WITH_CTEA = False
try:
    from tea_encrypt import strtea
    from tea_encrypt.utils import pyctea
    WITH_CTEA = True
except ImportError:
    pass

from tea_encrypt.version import __version__
from tea_encrypt.utils import pytea

if WITH_CTEA:
    EncryptStr = pyctea.tea_str_c_encrypt
    DecryptStr = pyctea.tea_str_c_decrypt
else:
    EncryptStr = pytea.str_encrypt
    DecryptStr = pytea.str_decrypt
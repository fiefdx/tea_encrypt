# tea_encrypt

encrypt & decrypt string(bytes) with interleaving and padding random numbers TEA


## Install
   
```bash
$ pip3 install tea_encrypt
```

## Usage
```python
from tea_encrypt import EncryptStr, DecryptStr

k = b"de1182b0f4203cad8d2ec629e35403d7"
v = b"this is a test"

encrypt_bytes = EncryptStr(v, k)
original_bytes = DecryptStr(encrypt_bytes, k)
```

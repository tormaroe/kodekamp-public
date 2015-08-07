# -*- coding: cp1252 -*-
from operator import add,sub
import sys

ALPHABET = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."

def otp(data, key, encrypt):
    """If 'encrypt', encrypt data with key. Else decrypt data with key"""
    op = add if encrypt else sub
    enc_dec_data = ""
    for d,k in zip(data,key):
        # Character not in the alphabet, do not touch it
        if d not in ALPHABET:
            enc_dec_data += d
            continue
        # Add if encrypting, substract if decrypting
        index = op(ALPHABET.index(d), ALPHABET.index(k)) % len(ALPHABET)
        enc_dec_data += ALPHABET[index]
    return ''.join(enc_dec_data)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(-1)
    enc = (sys.argv[1]) == 'e'
    data = open(sys.argv[2]).read().decode('utf-8')
    key = open(sys.argv[3]).read().decode('utf-8').replace("-","").replace("\r","").replace("\n","")
    
    print otp(data,key,enc)
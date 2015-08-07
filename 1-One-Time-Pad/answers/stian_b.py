# -*- encoding: utf-8 -*-
import sys
import codecs

alphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."
weights = dict(x for x in zip(alphabet, range(len(alphabet))))

def encrypt_char(char, key):
    assert key in weights
    if not char in weights: return char
    weight = weights[char] + weights[key]
    return alphabet[weight % 31]

def decrypt_char(char, key):
    assert key in weights
    if not char in weights: return char
    weight = weights[char] - weights[key]
    weight = weight if (weight >= 0) else 31 + weight
    return alphabet[weight]

def read_msg(filepath):
    return codecs.open(filepath, 'r', encoding="utf-8").read()

def read_key(filepath):
    text = codecs.open(filepath, 'r', encoding="utf-8").read()
    return ''.join(c for c in text if c not in "-\n")

def gen_str(op, msg, key):
    return ''.join(op(c, key[n]) for n,c in enumerate(msg))

op = sys.argv[1]
msg = read_msg(sys.argv[2])
key = read_key(sys.argv[3])

if op == 'd':
    print gen_str(decrypt_char, msg, key)
else:
    print gen_str(encrypt_char, msg, key)

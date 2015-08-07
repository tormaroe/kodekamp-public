#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Generator-basert loesning for kjempekjekt kodekamp 1.
# av @stianeikeland
#
# Tror python 3 er hakket mer egnet til dette, hvor en har generator delegates
# osv, men siden det er KGB som skal bruke den saa faar det heller gaa med 2.7
# (PS: python 3 er 7(!) aar gammel og leeengter etter bruk :p)
#

from __future__ import with_statement
from itertools import ifilter, izip
from sys import argv, stdout

import codecs

INVALID_KEY_CHARS = u"-\n"

# Alphabet lookup and inverse lookup tables (a->v, v->a)
ALPHABET = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."
VALUES = {v: k for k, v in dict(enumerate(ALPHABET)).items()}


def file_iter(filename):
    with codecs.open(filename, "r", "utf-8") as f:
        for char in iter(lambda: f.read(1), ""):
            yield char


def key_cleaner(key):
    return ifilter(lambda char: char not in INVALID_KEY_CHARS, key)


def process_message(operator, message, key):
    for [m, k] in izip(message, key):
        if m in VALUES:
            yield operator(m, k)
        else:
            yield m


def decrypter(msg_chr, key_chr):
    plaintext_val = (VALUES[msg_chr] - VALUES[key_chr]) % len(ALPHABET)
    return ALPHABET[plaintext_val]


def encrypter(msg_chr, key_chr):
    ciphertext_val = (VALUES[msg_chr] + VALUES[key_chr]) % len(ALPHABET)
    return ALPHABET[ciphertext_val]


def main():
    if len(argv) != 4 or argv[1] not in "ed":
        print("Usage: otp.py [e|d] [message-file] [key-file]")
        print("Example: otp.py d secret1.txt key1.1tp")
        exit(1)

    mode, message_file, key_file = argv[1:]

    message = file_iter(message_file)
    key = key_cleaner(file_iter(key_file))

    op = {'e': encrypter,
          'd': decrypter}[mode]

    output = process_message(op, message, key)

    for x in output:
        stdout.write(x)


if __name__ == "__main__":
    main()

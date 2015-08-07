#!/usr/bin/python
# coding=UTF-8

import sys, getopt

alphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."

def usage(appname):
    print appname + " [-e|--encrypt|-d|--decrypt] <input> <key>"

def char_to_alphabet_index(char):
    return alphabet.find(char)

def decrypt_char(a, b):
    return (a - b) % (len(alphabet))

def encrypt_char(a, b):
    return (a + b) % (len(alphabet))

def do_crypt(fun, text, otp):
    res = u""
    for i, c in enumerate(text):
        alphabet_index = char_to_alphabet_index(c)
        # Encrypt characters present in alphabet
        if alphabet_index >= 0:
            res = res + alphabet[fun(alphabet_index, otp[i % len(otp)])]
        else:
            res = res + c
    return res

def key_to_ints(key):
    otp = []
    for i, char in enumerate("-".join(key.splitlines()), 1):
        # Skip the block separators
        if not i % 7 == 0:
            otp.append(char_to_alphabet_index(char))
    return otp

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "de", ["decrypt", "encrypt"])
        if len(args) != 2:
            raise
    except Exception as e:
        usage(argv[0])
        sys.exit(2)

    cryptf = encrypt_char
    text = open(args[0]).read().decode('UTF-8')
    otp = key_to_ints(open(args[1]).read().decode('UTF-8'))

    # Encrypt or decrypt?
    for opt, arg in opts:
        if opt in ('-d', '--decrypt'):
            cryptf = decrypt_char

    print do_crypt(cryptf, text, otp).encode("UTF-8"),

if __name__ == "__main__":
    main(sys.argv)

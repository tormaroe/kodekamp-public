#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

def fix_broken_utf8_piping():
    reload(sys)
    sys.setdefaultencoding('utf-8')

def show_helpful_text_if_wrong_no_of_arguments():
    if len(sys.argv) < 4:
        print 'usage: otp.py [d|e] message_file key_file'
        print 'options: d(ecode), e(ncode)'
        quit()

def alphabet():
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .'.decode('utf8')
    d = dict()

    for i in range(0, len(a)):
        d[a[i]] = i
        d[i] = a[i] # Add the index as well as the letter to get bidirectional dict

    return d

def next_letter(f):
    return f.read(1)

def next_valid_letter(f, alphabet):
    letter = f.read(1)

    if not letter:
        return letter
    if letter not in alphabet:
        return next_valid_letter(f, alphabet)

    return letter

def encode(message_index, key_index):
    return message_index + key_index

def decode(message_index, key_index):
    return message_index - key_index

def crypt_letter(crypter, letter, key_letter, alphabet):
    if letter not in alphabet:
        return letter

    return alphabet[crypter(alphabet[letter], alphabet[key_letter]) % (len(alphabet) / 2)]

def crypt_and_display_all_letters(crypter, message, key, alphabet):
    while 1:
        m = next_letter(message)
        k = next_valid_letter(key, alphabet)

        if not m or not k: # We have reached the end of the message- or key-file
            break

        r = crypt_letter(crypter, m, k, alphabet)
        sys.stdout.write(r)

def open_message_and_key_file_and_crypt_contents(crypt_mode, message_location, key_location):
    with codecs.open(message_location, encoding='utf-8') as message, \
         codecs.open(key_location, encoding='utf-8') as key:

        if crypt_mode == 'd':
            crypt_and_display_all_letters(decode, message, key, alphabet())
        else:
            crypt_and_display_all_letters(encode, message, key, alphabet())

fix_broken_utf8_piping()
show_helpful_text_if_wrong_no_of_arguments()
open_message_and_key_file_and_crypt_contents(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os.path, operator
from functools import partial

alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .".decode('utf8')

if_encrypt = sys.argv[1]
de_en_crypted_file = sys.argv[2]
key_file = sys.argv[3]

def generate_matched_key(key_str, length):
    return (key_str * (length / len(key_str) + 1))[:length]

def str_to_num(s, alp):
    return operator.indexOf(alp, s)

def num_to_str(num, alp):
    return alp[num]

def mod(num, alp):
    return num % len(alp)

def de_or_encrypt(de_en_content, key, alpha, oper):
    content_num_list = map(partial(str_to_num, alp=alpha), de_en_content)
    matched_length_key = generate_matched_key(key, len(de_en_content))
    key_num_list = map(partial(str_to_num, alp=alpha), matched_length_key)
    encrypted_num_list = map(oper, content_num_list, key_num_list)
    mod_num_list = map(partial(mod, alp=alpha), encrypted_num_list)
    return "".join(map(partial(num_to_str, alp=alpha), mod_num_list))

def read_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as f:
            content = f.read().splitlines()
        return "".join(content).replace("-", "").upper().decode('utf8')
    else:
        print file_name + " does not exist!"

de_en_crypted_file_content = read_file(de_en_crypted_file)
key_content = read_file(key_file)
if "d" == if_encrypt:
    print "The content of file " + de_en_crypted_file + " is encrypted:\n" \
          + de_or_encrypt(de_en_crypted_file_content, key_content, alphabeth, \
          operator.sub)
elif "e" == if_encrypt:
    print "The content of file " + de_en_crypted_file + " is decrypted:\n" \
          + de_or_encrypt(de_en_crypted_file_content, key_content, alphabeth, \
          operator.add)
else:
    print "No such operation!"

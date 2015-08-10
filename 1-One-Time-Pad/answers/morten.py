# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

alphabet = unicode('ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .', 'utf-8')

def decrypt(messageChar, keyChar):
    if alphabet.find(messageChar) < 0: return messageChar
    index = alphabet.find(messageChar) - alphabet.find(keyChar)
    if index < 0: index += 31
    return alphabet[index]

def encrypt(messageChar, keyChar):
    if alphabet.find(messageChar) < 0: return messageChar
    return alphabet[(alphabet.find(messageChar) + alphabet.find(keyChar)) % 31]

message = codecs.open(sys.argv[2], "r","utf8").read()
key = codecs.open(sys.argv[3], "r", "utf8").read().replace("-", "").replace("\n", "").replace("\r", "")

if sys.argv[1] == 'e':
    print ''.join(map(lambda pair: encrypt(pair[0], pair[1]), zip(message, key)))    
else:
    print ''.join(map(lambda pair: decrypt(pair[0], pair[1]), zip(message, key)))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

alphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."

def main():
    encrypt = sys.argv[1] == "e"
    fMsg = sys.argv[2]
    fKey = sys.argv[3]

    msg = loadMessage(fMsg)
    key = loadKey(fKey)[:len(msg)]

    print process(msg, key, encrypt)

def readFile(fname):
    return codecs.open(fname, encoding="utf-8").read()

def loadMessage(fname):
    return readFile(fname)

def loadKey(fname):
    return readFile(fname).replace("-", "").replace("\r", "").replace("\n", "")

def process(msg, key, e):
    res = map(lambda m, k: processChar(m, k, e), msg, key)
    return "".join(res)

def processChar(m, k, e):
    if (m in alphabet):
        mi = alphabet.index(m)
        ki = alphabet.index(k)
        ri = calcChar(mi, ki, e)
        return alphabet[ri]

    return m

def calcChar(mi, ki, e):
    if (e):
        return (mi + ki) % len(alphabet)
    else:
        return (mi - ki) % len(alphabet)

if __name__ == "__main__":
    main()



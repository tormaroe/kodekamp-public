# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

alph = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."
key = open(sys.argv[3], "rb").read().decode("utf-8").replace("\n", "").replace("-", "")
msg = open(sys.argv[2], "rb").read().decode("utf-8")

def f(a,b):
    try:
        x = alph.rindex(a)
        y = alph.rindex(b)
        return alph[(y-x if sys.argv[1] == "d" else x+y) % 31]
    except:
        return b

print("".join(map(f, key[:len(msg)], msg)), end="")
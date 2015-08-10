#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys, codecs

alf=u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."
n = len(alf)
crypt = { 'd': (lambda x,y: alf[(alf.find(x) - alf.find(y)) % n]),
          'e': (lambda x,y: alf[(alf.find(x) + alf.find(y)) % n]) }

encr_type = sys.argv[1]
with codecs.open(sys.argv[2], 'r', 'UTF-8') as msg,\
     codecs.open(sys.argv[3], 'r', 'UTF-8') as otp:
    
    txt = msg.read()
    key = (x for x in otp.read() if x in alf)

    print ''.join([crypt[encr_type](x,y) if x in alf else x
                   for x,y in zip(txt,key)])

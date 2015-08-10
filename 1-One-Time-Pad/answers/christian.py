#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''One Time Pad by Christian S Røsnes (@NorSoulx) - 2015.08.07'''
import sys, codecs

def usage():
    print "Usage: %s <d|e> msgfile keyfile" % __file__
    sys.exit(1)

def readfile(filename):
    return codecs.open(filename, "r", "utf-8").read().upper()

def otp(msg,key,alphabet,op):
    '''(string,string,string,int) -> (list of char)'''
    alen  = len(alphabet)
    alist = list(enumerate(list(alphabet)))         # list of tuples (idx,char)
    chash = dict(map(lambda (x,y):(y,x), alist))    # lookup hash {char : idx}
    klist = filter(lambda x: x in chash, list(key)) # sanitize key list
    return map(lambda (m,k):                        # foreach (msg,key) char tuple (m,k)
        alist[(chash[m]+(op*chash[k]))%alen] [1]    #   perform op (encode/decode)
        if m in chash                               #   if m is in chash 
        else m,                                     #   or if m not in chash use as is
        zip(list(msg), klist))                      # from zipped list of (m,k) tuples
                                                    # with length = min(len(msg),len(klist))  
def runotp():
    alphabet = u'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .'
    (encode,decode) = (1,-1)
    operations = {'e':encode,'d':decode}
    if (len(sys.argv) < 4 or sys.argv[1] not in operations): usage()
    (opcode,msgfile,keyfile) = sys.argv[1:4]
    result = otp(readfile(msgfile),readfile(keyfile),alphabet,operations[opcode])
    print ''.join(result).encode('utf-8'), 

if __name__ == "__main__":
    runotp()

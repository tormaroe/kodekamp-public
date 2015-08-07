# -*- coding: utf-8 -*-
# lol, hadde tenkt lett, fikser streaming og sånt, men ble dritsur og gav nesten opp pga 
# diverse encoding issues, men einar sendte meg noe greier så jeg fikk feilsøkt litt
# viste seg at BOM encoding ødela en del, i tillegg til alt annet surr.
# fant også en del her om iterators og strømmer
# http://blog.etianen.com/blog/2013/10/05/python-unicode-streams/
# mye av det jeg har gjort var vel egentlig basert på einars eksempel
# Har brukt lazy enumerables sammen med streams en del på jobben i det siste, så ville lissom få det til å virke
# Skal være streaming og samtidig skal den teste seg selv før den skriver ut kode, hvis dokumentarene feiler
# så kræsjer programmet. Artig

from functools import partial
import codecs 
import random

def randChar():
    """Used for testing only"""
    return random.choice(list(u'ABCDEFGHIJKLMNOPQRSTUVWXYÆØÅ .'))
	
def randSequence(limit):
    """Used for testing only"""
    i = 0
    while(i < limit):
        i += 1
        yield randChar()
		
def iter_input(path,alfabet):
    
    """Returns an iterator from file.
	
	It filters out characters that are not in the alfabet.
	>>> alfabet = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYÆØÅ .')
	>>> iterator = iter_input("key1.1tp",alfabet)
    >>> iterator.next()
    u'K'
    >>> iterator.next()
    u'D'
    """
    with open(path, "r") as input:
        binary_chunks = iter(partial(input.read, 1), "")        
        for unicode_chunk in codecs.iterdecode(binary_chunks, "utf-8"):
            if not unicode_chunk in alfabet:
                continue
            yield unicode_chunk

def otp(keyiterator, secretiterator, encodearg, output,extendedAlfabet):
    """Decode or maybe even encodes if it works
    >>> import StringIO
    >>> encoder = StringIO.StringIO()
    >>> otp(u'XMCKL',u'HELLO','e',encoder, False)
    >>> print(encoder.getvalue())
    EQNVZ
    <BLANKLINE>
    >>> decoder = StringIO.StringIO()
    >>> otp(u'ZKD..JEN',u'BOOKNH','d',decoder, True)
    >>> print(decoder.getvalue())
    HELLO 
    <BLANKLINE>
    >>> encoderandom = StringIO.StringIO()
    >>> decoderandom = StringIO.StringIO()
    >>> key = list(randSequence(100))
    >>> msg = list(randSequence(100))
    >>> otp(key,msg,'e',encoderandom, True)
    >>> otp(key,encoderandom.getvalue(),'d',decoderandom, True)
    >>> decoderandom.getvalue() == "".join(msg)+'\\n'
    True
    """
    encode = 1 if encodearg is 'e' else -1
    if extendedAlfabet:
        alfabet = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .')
    else:
        alfabet = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for s,k in zip(secretiterator, keyiterator):
        decoded = alfabet[((alfabet.index(s) + encode*(alfabet.index(k))) % len(alfabet))]
        output.write(decoded)		
    output.write('\n')

if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()
    if not (sys.argv[1] == 'e' or sys.argv[1] == 'd') or len(sys.argv) == 3:
        print("Wrong command line input, example: python.exe otp.py d secret1.txt key1.1tp")		
        exit()
    import os.path
    if (not os.path.isfile(sys.argv[2]) or not os.path.isfile(sys.argv[3])):
        print("One or more of input files does not exist")
        exit()
    alfabet = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .')
    secretiterator = iter_input(sys.argv[2],alfabet)
    keyiterator = iter_input(sys.argv[3],alfabet)
    output = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
    otp(keyiterator, secretiterator, sys.argv[1], output, True)
    
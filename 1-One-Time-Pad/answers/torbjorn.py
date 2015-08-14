#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from operator import add, sub
import codecs

alphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."

def toValidAlphabetIndex(n):
	if n < 0:
		return (n + len(alphabet))
	else:
		return n % len(alphabet)

def shiftChar(op, c, cKey):
	if c in alphabet:
		n = op(alphabet.index(c), alphabet.index(cKey))
		return alphabet[toValidAlphabetIndex(n)]
	else:
		return c # keep char as is if not in alphabeth

def shiftString(op, st, key):
	shifted = map(
		lambda (c, k): shiftChar(op, c, k), 
		zip(st, key))
	return "".join(shifted)

def readMessage(path):
	with codecs.open(path, "r", "utf-8") as file:
		return file.read()

def readKey(path):
	return readMessage(path)\
               .replace("-", "")\
               .replace("\r", "")\
               .replace("\n", "")

def cryptoOperator(option):
	return sub if option.startswith("d") else add

op = cryptoOperator(argv[1])
message = readMessage(argv[2])
key = readKey(argv[3])

print shiftString(op, message, key)

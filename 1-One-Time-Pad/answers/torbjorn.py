#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import codecs, operator

alphabeth = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ ."

def toValidAlphabetIndex(n):
	if n < 0:
		return (n + len(alphabeth)) % len(alphabeth)
	else:
		return n % len(alphabeth)

def shiftChar(op, c, cKey):
	if c in alphabeth:
		n = op(alphabeth.index(c), alphabeth.index(cKey))
		return alphabeth[toValidAlphabetIndex(n)]
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
	#return "".join(readMessage(path).split())
	return readMessage(path).replace("-", "").replace("\r", "").replace("\n", "")

def cryptoOperator(option):
	return operator.sub if option.startswith("d") else operator.add

op = cryptoOperator(argv[1])
message = readMessage(argv[2])
key = readKey(argv[3])

print shiftString(op, message, key)
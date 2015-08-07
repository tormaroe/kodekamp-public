import sys
from functools import partial
from codecs import iterdecode

alfa = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ\xc6\xd8\xc5 .'
d = { ch : ix for (ix, ch) in enumerate(alfa) }

def otp(f, x, p):
  return alfa[f(d[x], d[p]) % len(alfa)]

def enc(x, p):
  return otp(lambda a, b: a + b, x, p)

def dec(x, p):
  return otp(lambda a, b: a - b + len(alfa), x, p)

def iter_alfa(path):
  with open(path, "rb") as input:
    binary = iter(partial(input.read, 1), "")
    return [ u for u in iterdecode(binary, 'utf-8') if u != '-' and u != '\r' and u != '\n']

otpop = dec if sys.argv[1] == 'd' else enc
message = iter_alfa(sys.argv[2])
otpkey = iter_alfa(sys.argv[3])
output = [ otpop(x, p) for (x, p) in zip(message, otpkey) ]

print u''.join(output)
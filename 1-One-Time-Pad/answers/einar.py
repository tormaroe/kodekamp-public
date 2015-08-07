import sys
import codecs

alfa = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ\xc6\xd8\xc5 .'
d = { ch : ix for (ix, ch) in enumerate(alfa) }

def readfile(fn):
  with codecs.open(fn,'r', 'utf-8') as f:
    return f.read()

def otp(f, x, p):
  return alfa[f(d[x], d[p]) % len(alfa)]

def enc(x, p):
  return otp(lambda a, b: a + b, x, p)

def dec(x, p):
  return otp(lambda a, b: a - b + len(alfa), x, p)

otpop = dec if sys.argv[1] == 'd' else enc
message = readfile(sys.argv[2]).strip()
otpkey = readfile(sys.argv[3]).replace("-", "").replace("\r", "").replace("\n", "")
output = [ otpop(x, p) for (x,p) in zip(message, otpkey) ]

print u''.join(output)
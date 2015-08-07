# coding=utf-8
__author__ = 'tormodh@gmail.com'
import sys, re

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .".decode('utf-8')


def fix_key(key):
    p = re.compile('[^'+ALPHABET+']')
    return p.sub('', key)


def get_pos_from_code_alphabet(index, key, mode):
    if mode == 'e':
        return ALPHABET.find(key[index])
    return -ALPHABET.find(key[index])


def file_content_utf_8(file_name):
    file = open(file_name, 'r')
    content = file.read().decode('utf-8')
    file.close()
    return content


def main(mode, inputFile, keyFile):
    assert mode == 'e' or mode == 'd', "Mode is not 'e'ncode or 'd'ecode: %s" % mode
    key = file_content_utf_8(keyFile)
    key = fix_key(key)
    input = file_content_utf_8(inputFile)
    assert len(input) <= len(key), "Key is too short to encode/decode, missing %r characters." % -(len(key) - len(input))
    output = transform(mode, input, key)
    print output


def transform(mode, input, key):
    output = ''
    for index in range(len(input)):
        pos = ALPHABET.find(input[index])
        if pos < 0:
            output += input[index]
        else:
            offset = get_pos_from_code_alphabet(index, key, mode)
            pos = (pos + offset + len(ALPHABET))%len(ALPHABET)
            output += ALPHABET[pos]
    return output
        

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
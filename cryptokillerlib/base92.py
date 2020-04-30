#coding=utf-8
'''
感谢 Gu-f  thenoviceoof 两位作者的相关项目
Gu-f github: https://github.com/Gu-f/py3base92
thenoviceoof github: https://github.com/thenoviceoof/base92
请支持一下两位原作者
'''
import math
__version__ = (1, 0, '3-1')
def base92_chr(val):
    if val < 0 or val >= 91:
        raise ValueError('val must be in [0, 91)')
    if val == 0:
        return '!'
    elif val <= 61:
        return chr(ord('#') + val - 1)
    else:
        return chr(ord('a') + val - 62)

def base92_ord(val):
    num = ord(val)
    if val == '!':
        return 0
    elif ord('#') <= num and num <= ord('_'):
        return num - ord('#') + 1
    elif ord('a') <= num and num <= ord('}'):
        return num - ord('a') + 62
    else:
        raise ValueError('val is not a base92 character')

def base92_encode(bytstr):
    # always encode *something*, in case we need to avoid empty strings
    if not bytstr:
        return '~'
    # make sure we have a bytstr
    #if (not isinstance(bytstr, str)) or (not isinstance(bytstr, bytes)):
    if not isinstance(bytstr, str):
        # we'll assume it's a sequence of ints
        bytstr = ''.join([chr(b) for b in bytstr])
    # prime the pump
    bitstr = ''
    while len(bitstr) < 13 and bytstr:
        bitstr += '{:08b}'.format(ord(bytstr[0]))
        bytstr = bytstr[1:]
    resstr = ''
    while len(bitstr) > 13 or bytstr:
        i = int(bitstr[:13], 2)
        resstr += base92_chr(i // 91)
        resstr += base92_chr(i % 91)
        bitstr = bitstr[13:]
        while len(bitstr) < 13 and bytstr:
            bitstr += '{:08b}'.format(ord(bytstr[0]))
            bytstr = bytstr[1:]
    if bitstr:
        if len(bitstr) < 7:
            bitstr += '0' * (6 - len(bitstr))
            resstr += base92_chr(int(bitstr,2))
        else:
            bitstr += '0' * (13 - len(bitstr))
            i = int(bitstr, 2)
            resstr += base92_chr(i // 91)
            resstr += base92_chr(i % 91)
    return resstr.replace('\\','\\\\')

def base92_decode(bstr):
    bitstr = ''
    resstr = ''
    if bstr == '~':
        return ''
    # we always have pairs of characters
    for i in range(len(bstr)//2):
        x = base92_ord(bstr[2*i])*91 + base92_ord(bstr[2*i+1])
        bitstr += '{:013b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    # if we have an extra char, check for extras
    if len(bstr) % 2 == 1:
        x = base92_ord(bstr[-1])
        bitstr += '{:06b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    return resstr
encode = base92_encode
b92encode = base92_encode

decode = base92_decode
b92decode = base92_decode

# m=encode(b'flag{123456}')
# print(m)
# c=decode(m)
# print(c)

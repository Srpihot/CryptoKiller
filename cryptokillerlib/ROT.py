#coding=utf-8
'''
object: rot3-encode-and-decode
author: Srpihot
date: 2020-04-30
version: 1.0
'''
# import string

#rot13只加密字母
def rot13_encode(str_text):
    start_a = ord('a')
    start_A = ord('A')
    encode_str = ""
    for key in str_text:
        if not key.isalpha():
            encode_str += key
            continue
        if key.islower():
            start = start_a
        if key.isupper():
            start = start_A
        #alpha表，除26求余
        encode_letter = (ord(key) - start + 13) % 26 + start
        encode_str += chr(encode_letter)
    return encode_str

#rot5只加密数字
def rot5_encode(str_text):
    encode_str = ""
    for key in str_text:
        if not key.isdigit():
            encode_str += key
        else:
            digit = (int(key) + 5) % 10
            encode_digit = '%d' %digit
            encode_str += encode_digit
    # print("rot5:" + encode_str)
    return encode_str

#rot18 = rot13 + rot5
def rot18_encode(str_text):
    str_text = rot5_encode(str_text)
    encode_str = rot13_encode(str_text)
    # print("rot18:" + encode_str)
    return encode_str

#rot47 对数字、字母、常用符号进行编码，按照它们的ASCII值进行位置替换，用当前字符ASCII值往前数的第47位对应字符替换当前字符
def rot47_encode(str_text):
    encode_str = ""
    for key in str_text:
        tmp = ord(key) + 47
        if tmp > 126:
            tmp = tmp - 126 + 32
        encode_str += chr(tmp)
    # print("rot47:" + encode_str)
    return encode_str

def rot13_decode(str_text):
    str_text = rot13_encode(str_text)
    return str_text

def rot5_decode(str_text):
    str_text = rot5_encode(str_text)
    return str_text

def rot18_decode(str_text):
    str_text = rot18_encode(str_text)
    return str_text

def rot47_decode(str_text):
    str_text = rot47_encode(str_text)
    return str_text

def How_to_use_this_module( ):
    # 通过ROT-5加密
    a = rot5_encode('123456')
    print('通过ROT-5加密:',a)
    # 通过ROT-5解密
    b = rot5_decode(a)
    print('通过ROT-5解密:',b)

    # 通过ROT-13加密
    a = rot13_encode('Howdoyoudo')
    print('通过ROT-13加密:',a)
    # 通过ROT-13解密
    b = rot13_decode(a)
    print('通过ROT-13解密',b)

    # 通过ROT-18加密
    a = rot18_encode('flag123456')
    print('通过ROT-18加密:',a)
    # 通过ROT-18解密
    b = rot18_decode(a)
    print('通过ROT-18解密:',b)

    # 通过ROT-47加密
    a = rot5_encode('flag{123456}')
    print('通过ROT-47加密:',a)
    # 通过ROT-47解密
    b = rot5_decode(a)
    print('通过ROT-47解密:',b)

# 查看演示,注释本条语句即可
# How_to_use_this_module()

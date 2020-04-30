#coding = utf-8
'''
object: caesar-encode-and-decode
author: Srpihot
date: 2020-04-20
version: 1.0
'''
def caesar_encode(str_text):
	# j即为key
    caesar_result=dict()
    for j in range(26):
        str_list = list(str_text)
        i = 0
        while i <len(str_text):
            if not str_list[i].isalpha():
                str_list[i] = str_list[i]
            else:
                a = "A" if str_list[i].isupper() else "a"
                str_list[i] = chr((ord(str_list[i]) - ord(a) + j) % 26 + ord(a))
            i = i + 1

        caesar_result[j]=''.join(str_list)
    # print(caesar_result)
    return caesar_result

def caesar_decode(str_text):
    return caesar_encode(str_text)

def How_to_use_this_module( ):
    plaintext = "qwlr{vlDlT_qmyvuovdDQRSQvquvdlmqoUYVWOHZTlqdloq}"
    print('caesar解密:')
    #返回一个字典 key为int型 values为字符串型
    print(caesar_decode(plaintext))

    plaintext = "flag{kaSaI_fbnkjdksSFGHFkfjksabfdJNKLDWOIafsadf}"
    print('caesar加密:')
    #返回一个字典 key为int型 values为字符串型
    print(caesar_encode(plaintext))

# How_to_use_this_module()
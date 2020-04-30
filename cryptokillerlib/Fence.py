#coding=utf-8
'''
object: Fence-encode-and-decode
author: Srpihot
date: 2020-04-30
version: 1.0
'''
def fence_decode(str_text):
    fence_result=dict()
    for space in range(2,len(str_text)):
        fence_ans = ""
        key = 0
        # 小于间隔继续
        while key < space:
            for i in range(0, len(str_text), space):
                # 不能越界
                if (i + key) < len(str_text):
                    fence_ans += str_text[i + key]
                    # print(str_text[i + key], end="")
            key = key + 1
        fence_result[space]=fence_ans
    return fence_result

def fence_encode(str_text):
    return fence_decode(str_text)



def How_to_use_this_moudle():
    print(fence_decode("felyaagn{gnziid}"))
    print(fence_encode("flag{nideyangzi}"))

# How_to_use_this_moudle()

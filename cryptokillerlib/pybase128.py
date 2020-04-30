#coding=utf-8
'''
object: Base128-encode-decode
author: Srpihot
date: 2020-4-29
version: 1.0
notice: 此版本base128 还有点小问题 CryptoKiller默认不是用此版本base128进行解密
'''
ascii_det='!#$%()*,.0123456789:;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎ'

def b128_encode(str_text):
    size=len(str_text)
    ls=0;
    rs=7;
    r=0;
    ans=""
    for inx in range(0,size):
        if ls>7:
            inx-=1
            ls=0
            rs=7
        nc=ord(str_text[inx])
        print(nc)
        r1=nc
        nc=nc<<ls
        nc=(nc & 0x7f)|r
        r=(r1>>rs) & 0x7F
        ls+=1
        rs-=1
        ans+=ascii_det[nc]
    return ans
def b128_decode(str_text):
    size=len(str_text)
    rs=8
    ls=7
    r=0
    ans=""
    for inx in range(0,size):
        nc=ascii_det.find(str_text[inx])
        if rs>7:
            rs=1
            ls=7
            r=nc
            continue
        r1=nc;
        nc=(nc<<ls)&0xFF
        nc=nc | r
        r=r1>>rs
        rs+=1
        ls-=1
        ans+=chr(nc)
    return ans

# m=b128_encode('flag123456')
# print(m)
# c=b128_decode(m)
# print(c)
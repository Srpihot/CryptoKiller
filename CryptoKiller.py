#coding=utf-8
'''
object: CryptoKiller
author: Srpihot
date: 2020-4-30
version: 1.0
'''
import base64
import argparse
from hashlib import md5
from cryptokillerlib import base58
from cryptokillerlib import base36
from cryptokillerlib import base91
from cryptokillerlib import base92
from cryptokillerlib import base128

check_code_yes_dic=['yes','YES','Y','y','Yes','yEs','yES','yeS','YE5','ye5','Ye5','yE5']
check_code_no_dic=['no','NO','N','n','No','oN']
number_str = "0123456789"
alpha_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base_decode(cipher_text):
    cipher_text = cipher_text.encode('ascii')
    # base16解密
    try:
        cipher_ans = base64.b16decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base16编码:',cipher_ans)
    except:
        pass
    
    # base36解密
    try:
        cipher_ans = base36.dumps(int(cipher_text))
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base36编码:',cipher_ans)
    except:
        pass
    
    # base58解密
    try:
        cipher_ans = base58.b58decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base58编码:',cipher_ans)
    except:
        pass
    
    # base64解密
    try:
        cipher_ans = base64.b64decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base64编码:',cipher_ans)
    except:
        pass
    
    # base85(ascii85型)编码
    try:
        cipher_ans = base64.a85decode(cipher_text).decode()   #ctf中常用
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base85(ASCII85型)编码:', cipher_ans) 
    except:
        pass
    
    # base85(RFC1924型)编码
    try:
        cipher_ans = base64.b85decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base85(RFC1924型)编码:',cipher_ans)
    except:
        pass
    
    # base91编码
    try:
        cipher_ans=base91.decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base91编码:',cipher_ans)
    except:
        pass

    # base92编码
    try:
        cipher_ans=base92.b92decode(cipher_text).decode()
        if cipher_ans == '':
            pass
        else:
            print('[+]探测到为Base92编码:',cipher_ans)
    except:
        pass
    # base128编码
    # try:
    #     b128 = base128.base128(chars = None ,chunksize = 126)
    #     cipher_ans_list=list()
    #     cipher_ans_list.append(cipher_text)
    #     for i in range(0,len(str(cipher_text,encoding='utf-8'))):
    #         try:
    #             cipher_ans_list.append([i])
    #             cipher_ans = b''.join(b128.decode(cipher_ans_list))
    #         except:
    #             pass
    #     if cipher_ans == '':
    #         pass
    #     else:
    #         print('[+]探测到为Base128编码:',cipher_ans.decode())
    # except:
    #     pass


def base_encode(str_text):
    str_text = str_text.encode('ascii')
    #base16编码
    try:
        print('[+]通过Base16编码:',base64.b16encode(str_text).decode())
    except:
        pass
    
    #base36编码
    try:
        print('[+]通过Base36编码:',base36.loads(str_text))
    except:
        pass

    #base58编码
    try:
        print('[+]通过Base58编码:',base58.b58encode(str_text).decode())
    except:
        pass

    #base64编码
    try:
        print('[+]通过Base64编码:',base64.b64encode(str_text).decode())
    except:
        pass

    #base85(ascii85型)编码
    try:
        print('[+]通过Base85(ASCII85)型编码:',base64.a85encode(str_text).decode())
    except:
        pass

    #base85(RFC1924型)编码
    try:
        print('[+]通过Base85(RFC1924)型编码:',base64.b85encode(str_text).decode())
    except:
        pass

    #base91编码
    try:
        print('[+]通过Base91编码:',base91.encode(str_text))
    except:
        pass

    #base92编码
    try:
        print('[+]通过Base92编码:',base92.base92_encode(str_text))
    except:
        pass

    #base128编码
    # try:
    #     b128 = base128.base128(chars = None ,chunksize = 126)
    #     print('[+]通过Base128编码(python字节码):',list(b128.encode(str_text))[0])
    #     # print('[+]通过Base128编码(UTF-8编码)',list(b128.encode(str_text))[0].decode('utf-8'))
    # except:
    #     pass

def md5_encode(str_text):
    mdS=md5()
    mdS.update(str_text.encode('utf-8'))
    str_md5 = mdS.hexdigest()
    print('[+]通过MD5编码:',str_md5)
    # return str_md5

def md5_decode(cipher_text):
    if len(cipher_text) == 32 :
        flag=0
        for i in range(0,len(cipher_text)):
            if ord(cipher_text[i]) > ord('f'):
                return
            else:
                flag=1
        
        if flag==1:
            print('[+]探测到为MD5(32位)')
            print('[+]请问选择多线程破解(boom) API查询(api) 字典查询(dict) 退出(exit):',end=' ')
            choice_code=input()
            if choice_code == 'boom':
                from cryptokillerlib import md5_boom
                # md5_boom.main(cipher_text)
                print('[-]此功能性能不佳正在升级中……')
                #如果想要使用目前已经开发模块可以取消注释，相关线程配置请到crytokillerlib/md5_boom.py中设置
            if choice_code == 'api':
                from cryptokillerlib import md5_api
            if choice_code == 'dict':
                from cryptokillerlib import md5_dict
                if md5_dict.find_md5(cipher_text) is None:
                    print('[-]抱歉暂无发现此MD5(32位)相关信息')
                    return
                else:
                    print('[+]成功发现密文:',md5_dict.find_md5(cipher_text))
            if choice_code == 'exit':
                return

def misc_decode(str_text):
    print("[+]开始探测常见加密\n[+]请输入明文中可能相关的字符串(多个请以'/'为间隔符):",end=' ')
    keys_result=input()
    # ROT-3编码
    from cryptokillerlib import ROT
    print('[+]探测到为ROT-5编码:',ROT.rot5_decode(str_text))
    print('[+]探测到为ROT-13编码:',ROT.rot13_decode(str_text))
    print('[+]探测到为ROT-18编码:',ROT.rot18_decode(str_text))
    print('[+]探测到为ROT-47编码:',ROT.rot47_decode(str_text))
    
    # CAESAR编码
    from cryptokillerlib import caesar
    print('[+]探测到为凯撒编码')
    # print("[+]请输入可能相关的字符串(多个请以'/'为间隔符):",end=' ')
    search_caesar = keys_result
    search_caesar = search_caesar.split("/")
    caesar_result = caesar.caesar_decode(str_text)
    find_flag = 0
    for i in range(0,len(caesar_result)):
        for j in range(0,len(search_caesar)):
            if search_caesar[j].lower() in caesar_result[i].lower():
                print('[+]探测到凯撒密码的偏移量为:{0} 明文:{1}'.format(i,caesar_result[i]))
                find_flag = 1
    if find_flag == 0:
        print('[-]没有搜索到相关信息,是否展示所有解密信息(y/n)?',end=' ')
        check_code = input()
        if check_code in check_code_yes_dic:
            for i in range(0,len(caesar_result)):
                print('[+]偏移量:{0} 明文:{1}'.format(i,caesar_result[i]))
        if check_code in check_code_no_dic:
            pass

    # Fence编码
    from cryptokillerlib import Fence
    print('[+]探测到为栅栏编码')
    # print("[+]请输入可能相关的字符串(多个请以'/'为间隔符):",end=' ')
    search_fence = keys_result
    search_fence = search_fence.split('/')
    fence_result = Fence.fence_decode(str_text)
    find_flag = 0
    # print(fence_result)
    for i in range(2,len(fence_result)):
        for j in range(0,len(search_fence)):
            if search_fence[j].lower() in fence_result[i].lower():
                print('[+]探测到栅栏密码的明文:{0}'.format(fence_result[i]))
                find_flag = 1
    if find_flag == 0:
        print('[-]没有搜索到相关信息,是否展示所有解密信息(y/n)?',end=' ')
        check_code = input()
        if check_code in check_code_yes_dic:
            for i in range(2,len(fence_result)):
                print('[+]明文:{0}'.format(fence_result[i]))
        if check_code in check_code_no_dic:
            pass

    # Morse解密
    check_mode = dict()
    for i in range(0,len(str_text)):
        check_mode[str_text[i]] = 1
    if len(check_mode) > 3 :
        pass
    else :
        from cryptokillerlib import MorseCode
        print('[+]探测到为Morse编码')
        try:
            if check_mode['.'] == 1 and check_mode['-'] == 1:
                print('[+]请输入间隔符:',end=' ')
                space_mark = input()
                print('[+]通过Morse解码:',MorseCode.Morse_decode(str_text,'.','-',space_mark))
        except:
            print('[+]这似乎不是标准的Morse编码')
            print('[+]请输入第一种Morse编码:',end=' ')
            code_one = input()
            print('[+]请输入第二种Morse编码:',end=' ')
            code_tow = input()
            print('[+]请输入间隔符:',end=' ')
            space_mark = input()
            Morse_result = MorseCode.Morse_decode(str_text,code_one,code_tow,space_mark)
            print('[+]通过Morse解码第一种情况:',Morse_result[0])
            print('[+]通过Morse解码第二种情况:',Morse_result[1])

    
        

def misc_encode(str_text):
    # ROT-3编码
    from cryptokillerlib import ROT
    print('[+]通过ROT-5编码:',ROT.rot5_encode(str_text))
    print('[+]通过ROT-13编码:',ROT.rot13_encode(str_text))
    print('[+]通过ROT-18编码:',ROT.rot18_encode(str_text))
    print('[+]通过ROT-47编码:',ROT.rot47_encode(str_text))

    # CAESAR编码
    from cryptokillerlib import caesar
    caesar_result = caesar.caesar_encode(str_text)
    print('[+]开始CAESAR编码')
    print('[+]请输入偏移量(输入0则全部展示):',end=' ')
    caesar_go = input()
    if caesar_go == '0':
        for i in range(0,len(caesar_result)):
            print('[+]偏移量:{0} 密文:{1}'.format(i,caesar_result[i]))
    elif caesar_go in number_str :
        print('[+]偏移量:{0} 密文:{1}'.format(int(caesar_go),caesar_result[int(caesar_go)]))
    else:
        for i in range(0,len(caesar_result)):
            print('[+]偏移量:{0} 密文:{1}'.format(i,caesar_result[i]))

    # 栅栏密码
    from cryptokillerlib import Fence 
    fence_result = Fence.fence_encode(str_text)
    print('[+]开始Fence编码')
    print('[+]请输入分割量(输入0则全部展示):',end=' ')
    fence_go = input()
    if fence_go == '0':
        for i in range(2,len(fence_result)):
            print('[+]偏移量:{0} 密文:{1}'.format(i,fence_result[i]))
    elif caesar_go in number_str :
        print('[+]偏移量:{0} 密文:{1}'.format(int(fence_go),fence_result[int(fence_go)]))
    else:
        for i in range(2,len(fence_result)):
            print('[+]偏移量:{0} 密文:{1}'.format(i,fence_result[i]))
    
    # Morse编码
    from cryptokillerlib import MorseCode
    MorseTEXT=str_text.lower()
    print('[+]通过Morse编码:',MorseCode.Morse_encode(MorseTEXT,'.','-',' ')[0])
    print('[+]是否需要自定义Morse编码(yes/no):',end= ' ')
    check_code = input()
    if check_code in check_code_yes_dic:
        print('[+]请输入第一种Morse编码:',end=' ')
        code_one = input()
        print('[+]请输入第二种Morse编码:',end=' ')
        code_tow = input()
        print('[+]请输入间隔符:',end=' ')
        space_mark = input()
        Morse_result = MorseCode.Morse_encode(MorseTEXT,code_one,code_tow,space_mark)
        print('[+]通过自定义Morse解码第一种情况:',Morse_result[0])
        print('[+]通过自定义Morse解码第二种情况:',Morse_result[1])
    if check_code in check_code_no_dic:
        pass


def CrytoKiller_Welcome():
    print("   ______                  _          ___  ____    _   __   __                 ")
    print(" .' ___  |                / |_       |_  ||_  _|  (_) [  | [  |                ")
    print("/ .'   \_| _ .--.  _   __`| |-' .--.   | |_/ /    __   | |  | | .---.  _ .--.  ")
    print("| |       [ `/'`\][ \ [  ]| | / .'`\ \ |  __'.   [  |  | |  | |/ /__\\[ `/'`\] ")
    print("\ `.___.'\ | |     \ '/ / | |,| \__. |_| |  \ \_  | |  | |  | || \__., | |      V1.0")
    print(" `.____ .'[___]  [\_:  /  \__/ '.__.'|____||____|[___][___][___]'.__.'[___]  by-Srpihot")
    print("                  \__.'                                                        ")
    print("       SITE:http://srpihot.site        Github:https://github.com/srpihot       ")


def main():
    CrytoKiller_Welcome()
    parse=argparse.ArgumentParser(description='一款面向CTFer的编码密码探测器。例如:python CrytoKiller.py -e "flag{CrytoKiller_is_C@me}"')
    parse.add_argument('-d','--decode',metavar="密文",type=str,help='想要检测的密文')
    parse.add_argument('-e','--encode',metavar="明文",type=str,help='想要加密的明文')
    args = parse.parse_args()

    if args.decode is not None and args.encode is None:
        base_decode(args.decode)
        misc_decode(args.decode)
        md5_decode(args.decode)

    elif args.encode is not None and args.decode is None:
        base_encode(args.encode)
        misc_encode(args.encode)
        md5_encode(args.encode)
    else:
        CrytoKiller_Welcome()
        print('[-]您的输入有误,请使用命令 --help 或者 -h 获得帮助。')


if __name__ == "__main__":
    main()
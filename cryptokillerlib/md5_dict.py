#coding=utf-8
'''
object: MD5-dict-find
author: Srpihot
date: 2020-4-30
version: 1.0
'''
def find_md5(str_text):
    with open('./cryptokillerlib/dict/md5_dict.cyk','r') as f:
        # 2333 md5_dict.cyk其实就是一TXT文件啦 闲的没事起了个cyk后缀名 （这个不是个人名缩写）
        md5_db = f.readlines()
        f.close()
    for md5_mes in md5_db:
        md5_mes = md5_mes.strip('\n').split(',')
        if str_text == md5_mes[1]:
            return md5_mes[0]
        else:
            pass
    return None


# 测试样例
# print(find_md5("e10adc3949ba59abbe56e057f20f883e"))


#生成字典

# with open(r'.\cryptokillerlib\dict\password.txt','r') as f:
#     md5_more=f.readlines()
# for str_text in md5_more:
#     str_text = str_text.strip('\n')
#     print(str_text.encode('utf-8'))
#     mdS=md5()
#     mdS.update(str_text.encode('utf-8'))
#     str_md5 = mdS.hexdigest()
#     with open('.\cryptokillerlib\dict\md5_dict.cyk','a+') as ff:
#         ff.write(str_text+','+str_md5+'\n')
#     print('[+]通过MD5编码:',str_md5)
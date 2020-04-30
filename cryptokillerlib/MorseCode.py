#coding = utf-8
'''
object: Morse-encode-and-decode
author: Srpihot
date: 2020-4-30
version: 1.0
'''

MorseList = {
    'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",
    'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",
    'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--..",'1':".----",'2':"..---",'3':"...---",
    '4':"....-",'5':".....",'6':"-....",'7':"--...",'8':"---..",'9':"----.",'0':"-----",'.':".-.-.-",
    '?':"..--..",'!':"-.-.--",'(':"-.--.",'@':".--.-.",':':"---...",'=':"-...-",'-':"-....-",')':"-.--.-",
    '+':".-.-.",',':"--..--","\'":".----.",'_':"..--.-",'$':"...-..-",';':"-.-.-.",'/':"-..-.",
    '\"':".-..-.","{":".....-","}":"-----."
}
def Morse_decode(str_text,zero_code,one_code,split_sign):
    s = str_text
    if zero_code=='.' and one_code=='-':
        try:
            cipher_ans = ""
            while True:
                ss = s.split(split_sign)
                for c in ss:
                    for k in MorseList.keys():
                        if MorseList[k] == c:
                            cipher_ans+=k
                return cipher_ans
        except:
            # print('[-]似乎不是正确的输入格式')
            return
    else:
        MorseList_zero=dict()
        MorseList_one=dict()
        for code in MorseList:
            MorseList_zero[code] = MorseList[code].replace('.',zero_code).replace('-',one_code)
            MorseList_one[code] = MorseList[code].replace('-',zero_code).replace('.',one_code)
        # print(MorseList_zero)
        cipher_ans_list=list()
        try:
            cipher_ans = ""
            while True:
                ss = s.split(split_sign)
                for c in ss:
                    for k in MorseList_zero.keys():
                        if MorseList_zero[k] == c:
                            cipher_ans+=k
                cipher_ans_list.append(cipher_ans)
                break
        except:
            # print('[-]似乎不是正确的输入格式')
            pass
        
        try:
            cipher_ans = ""
            while True:
                ss = s.split(split_sign)
                for c in ss:
                    for k in MorseList_one.keys():
                        if MorseList_one[k] == c:
                            cipher_ans+=k
                cipher_ans_list.append(cipher_ans)
                break
        except:
            # print('[-]似乎不是正确的输入格式')
            return

        return cipher_ans_list
            

def Morse_encode(str_text,zero_code,one_code,split_sign):
    Morse_one=""
    Morse_tow=""
    encode_result=list()
    MorseList_zero=dict()
    MorseList_one=dict()
    for code in MorseList:
        MorseList_zero[code] = MorseList[code].replace('.',zero_code).replace('-',one_code)
        MorseList_one[code] = MorseList[code].replace('-',zero_code).replace('.',one_code)
    for i in range(0,len(str_text)):
        Morse_one += MorseList_zero[str_text[i]] + split_sign
        Morse_tow += MorseList_one[str_text[i]] + split_sign
    Morse_one = Morse_one.strip(split_sign)
    Morse_tow = Morse_tow.strip(split_sign)
    encode_result.append(Morse_one)
    encode_result.append(Morse_tow)  
    return encode_result


# print(Morse_decode('.--/--.','.','-','/'))
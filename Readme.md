## CryptoKiller V1.0

```text
简介：
    一款面向CTF的密码编码探测器,用法简单。
起源：
	1.平时遇到一些编码或者密码的时候要去各种网站上测，经常抢不到一血。
	2.准备给学弟们出一点题目，写了一个脚本(CryptoKiller前身)比较各种编码方式，研究如何不被一眼看出来。于是就写着写着就完善一下发出来吧。
	3.希望做一个自动化探测的工具
安装：
	
功能：
	目前集成的CTF中MISC与Crypto常见的一些编码方式。
		已经完成：
			BASE16 BASE36 BASE58 BASE64 BASE85 BASE91 BASE92 BASE128 BASE256
			ROT-5 ROT-13 ROT-18 ROT-47
			Fence Ceaser Morse
			MD5(32bit)
		待完善：
			其他常见的方式(主要是比较菜2333 有密码学大佬带带我吗 卑微WEB手）
未来：
	如果有人用的话，考虑加个GUI。用C#或者C++重写一个啦~
用法:
    usage: CryptoKiller.py [-h] [-d 密文] [-e 明文]

    一款面向CTFer的编码密码探测器。例如:python CrytoKiller.py -e   "flag{CrytoKiller_is_C@me}"

    optional arguments:
      -h, --help          show this help message and exit
      -d 密文, --decode 密文  想要检测的密文
      -e 明文, --encode 明文  想要加密的明文

```

![](https://i.loli.net/2020/04/30/157kdKBpWhiogam.png)

### 使用截图

+ 加密
  + ![](https://i.loli.net/2020/04/30/FNE4uB29h8Yj6Dr.png)
  + ![](https://i.loli.net/2020/04/30/nY8Iyr7Vq9OP2Lv.png)
  + 以前教协会学弟的时候写的一个脚本 之后就直接集成进来了2333~
+ 解密
  + 自动探测密文
  + base家族 部分
  + ![](https://i.loli.net/2020/04/30/b4Nu2RAoh3Vgqe6.png)
  + ![](https://i.loli.net/2020/04/30/5DwdJYq3N2XZsxm.png)
  + ![](https://i.loli.net/2020/04/30/OTQIF7Jg8Xslbj5.png)
  + 常见加密破解 支持关键字搜取
  + ![](https://i.loli.net/2020/04/30/gJHzCxuXFblsjcG.png)
  + CTF中MD5破解(常用7000个左右弱口令密码 AWD跟某些CTF题目会遇到)
  + ![image-20200430174954897](C:\Users\61944\AppData\Roaming\Typora\typora-user-images\image-20200430174954897.png)
  + 目前 已经写完多线程破解 与 字典查询 (多线程测试效果不太理想 打算研究一下) API打算考虑PMD5的api为主 但是字典查询感觉蛮可用的 例如 ?admin 在某md5平台上是收费查询
  + Morse编码检测 (偶尔比赛中会碰到这种)
  + ![](https://i.loli.net/2020/04/30/1FenENGUgxPts2D.png)
  + ROT
  + ![](https://i.loli.net/2020/04/30/Ko5Vh6f4swPWDL9.png)

###  欢迎star与fork~ 欢迎star与fork~ 欢迎star与fork~

感谢以下大佬的大赏：

| 打赏用户名 | 打赏金额 | 打赏方式 |
| :--------: | :------: | :------: |
|            |          |          |




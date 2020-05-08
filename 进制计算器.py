#!/usr/bin/env python3
# -*- coding: utf-8 -*-
bdh=input("请输入需转换的进制缩写(b,d,h):")
'''还有一堆bug得修复，233。比如转换范围太小，
以及无法检测一些特殊字符什么的，还得边学习边
完善啊。还打算追加进制猜测代码。。。
不管有多么fw，这也算我写的第一个有点用的东西
吧，233。。。
'''
print('-'*20)
if 99<ord(bdh)<101:
    dex=int(input("请输入一个十进制数\nDex:"))
    print('-'*20)
    str=(bin(dex))
    print('Bin:'+str[2:])
    str = (hex(dex))
    print('Hex:' + str[2:])
elif 97<ord(bdh)<99:
    bin=input("请输入一个二进制数\nBin:")
    print('-'*20)
    print('Dex:'+str(int(bin,2)))
    str=(hex(int(bin,2)))
    print('Hex:'+str[2:])
elif 103<ord(bdh)<105:
    hex=input("请输入一个十六进制数\nHex:")
    print('-'*20)
    stb=(bin(int(hex,16)))
    print('Bin:'+stb[2:])
    print('Dex:'+str(int(hex,16)))
else:
    print('输入无效')
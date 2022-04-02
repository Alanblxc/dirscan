import os
import time
# 导入requests模块
import requests

print("")
print("  /\    |       /\   |\  |")
print(" /__\   |      /__\  | \ |")
print("/    \  |___  /    \ |  \|")
print()
print("author: Alan")
print("")


zidiandir=input("输入字典所在目录,不输入会用默认词典:")
print("格式类似于(https://www.bixuge.com/)")
bpurl=input("输入要找后台的网站:")
print("输入后台错误返回的页面('<Response [404]>')不输入默认为这个:")
bpflase=input("")
if bpflase=='':
    bpflase='<Response [404]>'
if zidiandir == '':
    zidiandir=os.getcwd()+'/字典'
filenames = os.listdir(r''+zidiandir)
for x in filenames:
    file = open('字典/'+x, encoding='utf-8')
    a=0
    while 1:
        a=a+1
        line = file.readline()
        # 接口地址
        awa=str(line)
        url = (bpurl+awa).strip('\n')
        r = requests.get(url)
        print(str(a)+'次')
        if str(r) != bpflase:
            print("成功,链接为:"+url)
            break
        print(line+"不是\n")
        if not line:
            break
        pass  # do something


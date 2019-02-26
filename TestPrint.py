# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/13 17:03
# FileName    : TestPrint.PY
# ProductName : PyCharm

fp=open(r'D:\mr.txt','a+')
print("go big or go home ",file=fp)
fp.close();



# 输入当前的日期

import datetime;
print("当前的年份"+str(datetime.datetime.now().year))
print("当前的时间 "+datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

#输入
temp=input("请输入你的名字")

print(temp)

lucknum=int(input("请输入你的幸运数字"))

print(type(lucknum))






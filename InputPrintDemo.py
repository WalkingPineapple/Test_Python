# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/13 17:25
# FileName    : InputPrintDemo.PY
# ProductName : PyCharm


# 年龄小于18未成年 大于等于18并且小于等于60青年   大于等于60老年 用户输入出生年份

import datetime

UserYear=int(input("请输入您的出生年份"))
NowYear=datetime.datetime.now().year;
UserAge=NowYear-UserYear;
if UserAge<18:print("您当前的年龄为"+str(UserAge)+"岁,您属于未成年人")
if 18<=UserAge<60:print("您当前的年龄为"+str(UserAge)+"岁,您属于青年人")
if UserAge>=60:print("您当前的年龄为"+str(UserAge)+"岁,您属于未成年人")



#进制转换

input_number = int(input("请输入一个十进制数："))
print(str(input_number)+"二进制数是"+str(bin(input_number)[2:]))
print(str(input_number)+"十六进制数是"+str(hex(input_number)[2:]))
print(str(input_number)+"八进制数数是"+str(oct(input_number)[2:]))


# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/25 13:51
# FileName    : modulestask.PY
# dev tools   : PyCharm


import datetime
def inputdate():
    indate = input("请输入开始日期（20190505）后按<enter>键：")
    indate = indate.strip()
    if len(indate)==0:
        return datetime.date.today()
    else:
        if len(indate)==8:
             datester=indate[0:4]+"-"+indate[4:6]+"-"+indate[6:8]
             return datetime.datetime.strptime( datester,"%Y-%m-%d")
        else:
            print("输入错误，将按当前日期推算！！")
            return datetime.date.today()
print("********推算几天后的日期********")
sdate=inputdate()
innum= input("请输入间隔天数后按<enter>键(输入负数则往前计算)：")
if int(innum)!=0:
    fdate=sdate +datetime.timedelta(days=int(innum))
    fdate=datetime.datetime.strftime( fdate ,"%Y-%m-%d")

    print("你推算的日期是： "+ str(fdate))
else:
    print("输入错误，程序将退出！！")





import random

def ball3d():
    radball = ""
    number = "1234567890"
    for i in range(3):
        radball = radball + str(random.choice(number))
    return str(radball)

def inputnew():
    instr = input("请输入一个福彩3D彩票（3位数字）:")  # 请输入一个福彩3D号码(只能为3位数字)
    instr = instr.strip()
    return instr

def inputbox():
    cxstr = inputnew()
    if len(cxstr) == 3 and cxstr.isdigit():  # 输入数据的长度不为零
        return cxstr
    else:
        print("输入错误，请重新输入3位数字的3D彩票:")  # 请输入一个福彩3D号码(只能为3位数字)

inball = []
while len(inball) < 3:
    inball.append(inputbox())
    if None in inball:
        inball.remove(None)
inball.append(ball3d())
inball.append(ball3d())
inball.append(ball3d())
print("您需要的3D彩票已生成:")
print(("\n").join(inball))


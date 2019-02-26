# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/21 15:46
# FileName    : func.PY
# dev tools   : PyCharm

def demo(obj):
    print("原值", obj)
    obj += obj


# 值传递
mot = "凡是不能将我毁灭的，必将使我强大"
print(mot)

demo(mot)
print(mot)

# 引用传递

list1 = ['蛮王', '妖姬']

demo(list1)

print(list1)


def fun_hero(name1):
    heroname = ""
    if name1 == "暗夜猎手":
        heroname = "VN"
    elif name1 == "德玛西亚之力":
        heroname = "盖伦"
    else:
        heroname = "当前英雄资料不足"
    return heroname


# 调用

name = input("请输入英雄外号")
heroname = fun_hero(name)
print(name, heroname)


# 匿名函数

import  math
def circlearea(r):
    return math.pi*r*r
print(circlearea(10))



result=lambda r:math.pi*r*r

print(result(10))


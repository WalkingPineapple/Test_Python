# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/22 14:05
# FileName    : classTrain.PY
# dev tools   : PyCharm


# 定义一个英雄类

class Hero:
    '''英雄类'''
    _HP = 2000  # 类属性
    __MP = 1300  # 类属性

    def __init__(self):  # 必须有参数
        print("这是一个英雄类")
        print(Hero._HP)
        print(Hero.__MP)


wildHer = Hero()
print(wildHer._HP)
print(wildHer._Hero__MP)

class car:
    '''汽车类'''

    def __init__(self):
        self.wheel = 4
        self.window = 10
        print("这是一个汽车类")
        print(self.wheel)
        print(self.window)


bus = car()

bus.wheel = 213

print(bus.wheel)

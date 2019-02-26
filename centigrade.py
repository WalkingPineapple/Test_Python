# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/13 21:21
# FileName    : centigrade.PY
# dev tools   : PyCharm


# 华摄氏度互相转换摄氏度

# 华摄氏度转摄氏度 C=(F-32)*5/9
# 摄氏度转华摄氏度 F=(c*5/9)+32


# 判断转换关系
select = int(input("选择转换关系，华摄氏度转摄氏度请扣1 摄氏度转华摄氏度请扣2 ："));
if select == 1 or select == 2:
    if select == 1:
        huacelsius = float(input("请输入华摄氏度："))
        print("转换后摄氏度为", (huacelsius - 32) * 5 / 9)
    else:
        celsius = float(input("请输入摄氏度："))
        print("转换后的华摄氏度为", (celsius * 5 / 9) + 32)

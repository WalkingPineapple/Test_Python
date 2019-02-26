# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/13 20:50
# FileName    : sale.PY
# dev tools   : PyCharm

# 打折时间：星期二的上午10点至11点和每周五下午的14点至15点
# 逻辑关系：1.判断是否是星期二 与 10-11 或 星期五 14-15

# 获取当前的星期 以及时间

custom_week = input("请输入中文的星期（全写）：")
custom_time = int(input("请输入时间点（0-24）："))

# 判断
if (custom_week == "星期二" and (10 <= custom_time and custom_time<= 11)) or (custom_week == "星期五" and (14 <= custom_time and custom_time <= 15)):
    print("打折啦")
else:
    print("不打折")

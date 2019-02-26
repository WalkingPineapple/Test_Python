# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/19 17:35
# FileName    : strTrain.PY
# dev tools   : PyCharm


# str = "2018 Amazon Jeff Bezos 1120"
# print(str[4:])
# str1 = str[0:4]
# str2 = str[23:]
# print(str1 + str2)
# print(str.replace("2018", "[2018]").replace("1120", "[1120]"))
# str3 = str.strip()
# print(str3)
# print(str.replace(" ", ""))


user_id = input("请输入您的身份证号：")
user_id_len = len(user_id)
print(user_id_len)
print(type(user_id_len))
if user_id_len == 18:
    birthday = user_id[6:14]
    year = birthday[0:4]
    month = birthday[4:6]
    day = birthday[6:]
    temp = int(user_id[16:17])
    if (temp % 2 == 0):
        print("你是一个女孩子")
        print("你的生日是"+year+"年"+month+"月"+day+"日")
        print("对吗?")
    else:
        print("你是一个蓝孩子")
        print("你的生日是" + year + "年" + month + "月" + day + "日")
        print("对吗?")

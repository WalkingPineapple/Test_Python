# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/18 15:41
# FileName    : stringOperation.PY
# dev tools   : PyCharm


str1="人生苦短，我用python！"
try:
    substr=str1[15]
except IndexError:
    print("指定字符串索引不存在")



# 字符串格式化

template='学号：%10d\t 姓名：%s\t 班级：%s\t  ' #定义模版
template1='学号:{:10d}\t 姓名:{:s}\t 班级：{:s}'
context=(2016611175,'董程杰','16计算机科学计术')
context1=(2016611177,'程杰董','16计算机科学计术')
print(template%context)
print(template1.format(2016611177,'程杰董','16计算机科学计术'))


# Match方法


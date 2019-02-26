# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/25 16:23
# FileName    : ostest.PY
# dev tools   : PyCharm



import os

print(os.name)
print(os.getcwd())

print(os.path.abspath("NEW.txt"))


# os.mkdir("D:\\ostest") #一级目录
# os.makedirs("D:\\ostest\\demo\\code")
# os.rmdir("D:\\ostest")


# os.makedirs("D:\\ostest\\demo\\code")

tuples=os.walk("D:\\ostest")

print(type(tuples)) # 返回值是一个元组生成器


for i in tuples:
    print(i)

# os.rename("D:\\ostest","D:\\pathtest")


fileinfo=os.stat("D:\\pathtest\\demo\\code\\01\\01.txt")

print(fileinfo.st_dev)
print(fileinfo.st_mtime)

# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/21 10:29
# FileName    : dic.PY
# dev tools   : PyCharm


dic={'JAVA语言程序设计':'90','软件工程':'64','ASP.NET程序设计':'98'}

print(dic.items())

for item in dic.items():
    print(item)  # 元组

for key,value in dic.items():
    print(key,"的成绩为",value)

print(dic.values())


for key in dic.keys():
        print(key,"的成绩为",dic.get(key,'找不到'))


dic['JAVA语言程序设计']='100'

for key,value in dic.items():
    print(key,"的成绩为",value)



import  random

randomdict={i:random.randint(10,100)for i in  range(1,5)}
print(randomdict)
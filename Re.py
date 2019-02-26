# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/19 15:56
# FileName    : Re.PY
# dev tools   : PyCharm


import re

string = "Mr.Dong mr.Dong "
string1="CUUHG Mr.Dong mr.Dong"
pattern = r'mr\.\w+'
match = re.match(pattern, string, re.I)
result=re.sub(pattern,'Mr.Jay',string)
print(result)
print(match)
print(match.string)
print(match.start())
print(match.end())
print(match.span())
print(match.group())

match1=re.search(pattern,string1,re.I)
print(match1)

match2=re.findall(pattern,string,re.I)
print( match2)



pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'      # 模式字符串
str1 = '127.0.0.1 192.168.1.66'                # 要配置的字符串
match = re.findall(pattern,str1)               # 进行模式匹配
print(match)



import re
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'  # 模式字符串
str1 = '127.0.0.1 192.168.1.66'              # 要配置的字符串
match = re.findall(pattern,str1)             # 进行模式匹配
print(match)
for item in match:
    print(item[0])




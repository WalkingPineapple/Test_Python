# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/14 15:00
# FileName    : list.PY
# dev tools   : PyCharm


import random

lsit=[random.randint(10,1000) for i in range(100)]
print(lsit)


price=[2213,21312,2154213,2132145]

saleprice=[x for x in price if x>5000]
print(saleprice)





vale=("Happy Valentine's Day.")  #字符串
print(vale)
vale1=("Happy Valentine's Day.",) #元
print(vale1)
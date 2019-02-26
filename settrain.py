# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/21 12:03
# FileName    : settrain.PY
# dev tools   : PyCharm



assassinhero = set(['男刀', '阿卡丽', '诡术妖姬', '奈德丽', '小鱼人'])
wildhero = set(['奈德丽', '狮子狗', '蛮王'])

print("既是打野英雄又是刺客英雄的是", assassinhero & wildhero)
print("都是英雄", wildhero | assassinhero)
print("不是打野英雄的是", assassinhero - wildhero)





# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/14 15:59
# FileName    : tencentsports.PY
# dev tools   : PyCharm

# 提供上一周QQ运动步数以及当前周运动步数
# 1.两周步数合并，先输出合并结果，在升序  降序分别输出
# 2.星期列表，通过步数的高低值然后添加到本周的星期列表
# 3.超过8000步，即为达标，分别输出本周和上周的达标日期和步数，并输出上周的总部数和本周总步数

# 建表

lastWeek = [4222, 5679, 12787, 21434, 21451, 3213, 6092]
thisWeek = [1231, 21314, 12423, 7666, 21341, 12412, 1213]

WEEK = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
print("（1）本周运动步数列表：", thisWeek)
print("（2）本周运动步数列表：", lastWeek)
##两周步数合并
sumWeek = []
for a, b in zip(lastWeek, thisWeek):
    sum = a + b
    sumWeek.append(sum)
print("（3）两周运动步数总表：", sumWeek)
sumWeek.sort()
print("（4）升序：", sumWeek)
sumWeek.sort(reverse=True)
print("（4）降序序：", sumWeek)

##获取最大步数和最小步数的定位

maxIndex = thisWeek.index(max(thisWeek))
minIndex = thisWeek.index(min(thisWeek))

WEEK.insert(maxIndex + 1, max(thisWeek))
WEEK.insert(minIndex + 1, min(thisWeek))

print("(5)", WEEK)

weekday = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
thislist1 = []
thislist2 = []
for item in thisWeek:
    if item > 8000:
        thislist1.append(item)
        i = thisWeek.index(item)
        thislist2.append(weekday[i])
print("（6）本周高于8000步的步数值：", thislist1)
print("     本周高于8000步的日期：", thislist2)
lastlist1 = []
lastlist2 = []
for item in lastWeek:
    if item > 8000:
        lastlist1.append(item)
        i = lastWeek.index(item)
        lastlist2.append(weekday[i])
print("     上周高于8000步的步数值：", lastlist1)
print("     上周高于8000步的日期：", lastlist2)

# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/22 17:07
# FileName    : propertyTrain.PY
# dev tools   : PyCharm


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.width * self.length


rect = Rectangle(540, 23)

print(rect.area)


class TVshow:
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show


tvshow = TVshow("zifuchuyb")
print(tvshow.show)



#
# class TVshow:   # 定义电视节目类
#     def __init__(self,show):
#         self.__show = show
#     @property                          # 将方法转换为属性
#     def show(self):                    # 定义show()方法
#         return self.__show             # 返回私有属性的值
# tvshow = TVshow("正在播放《战狼2》")   # 创建类的实例
# print("默认：",tvshow.show)            # 获取属性值





class furit:
    def __init__(self,color="green"):
        furit.color=color
    def harvest(self):
        print(furit.color)
class apple(furit):
    def __init__(self):
        print("apple")

super().__init__()
Apple=apple()
apple.harvest()










# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/21 18:15
# FileName    : functask.PY
# dev tools   : PyCharm




dict_data = {
    '0': 'O',
    '1': 'I',
    '2': 'Z',
    '3': 'E',
    '4': 'Y',
    '5': 'S',
    '6': 'G',
    '7': 'L',
    '8': 'B',
    '9': 'P',
}

def translate_code_word(word):
    '''转化字符串'''
    result = []
    global dict_data
    for i in word:
        print(i)
        result.append(dict_data[i])

    return result

if __name__ == '__main__':
    word = input('请输入暗语：')
    print(type(word))
    while True:
        result_list = translate_code_word(word)
        result_string = "".join(result_list)
        print('转换后是：%s ' % result_string)
        if result_string == 'BYE':
            break
        word = input('请输入暗语：')






# 以1月20日开始（水瓶座），根据星座的日期间隔，按顺序建立日期间隔的星座日期列表
sdate = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 21)
# 根据星座的顺序，根据星座出现的先后顺序，建立星座列表，列表中"摩羯座"出现两次，放到列表最前和最后
sstar = ("摩羯座","水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座")
# 要求用户输入日期，以“:”分割，注意不能使用中文符号
indate = input("请输入您的生日(格式：2018:10:12)：")
instr= indate.split(":")    # 把输入的日期按“：”进行分割成年、月、日
year = int(instr[0])        # 转换出年
month = int(instr[1])       # 转换出月
date = int(instr[2])        # 转换出日
if date >= sdate[month-1]:  # 如果日期大于等于日期列表中对应的前一个间隔日期
    print("您的星座是：" + sstar[month ] ) # 输出月份数字对应的星座列表的星座
else:
    print("您的星座是：" + sstar[month-1]) # 输出月份数字对应的星座列表的前一个星座

# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/20 15:37
# FileName    : loopstructure.PY
# dev tools   : PyCharm

# 1-99的累加和
result = 0
for i in range(100):
    result += i
print(result)

i = 0
while i <= 3:
    print("hhhhh")
    i = i + 1

password = 0
i = 1
while i < 7:
    num = input("请输入一位数字密码！")
    num = int(num)
    if num == password:
        print("密码正确，正进入系统！")
        i = 7
    else:
        print("密码错误，已经输错", i, "次")
    i += 1
print(i)
if i == 7:
    print("密码错误6次，请与发卡行联系！！")

# instr = "0"
# # 输入数字9，输出9的ASCII码值，并退出程序
# while ord(instr) != 57:
#     instr = input("请输入一个字母或数字：")
#     if len(instr) == 1:
#         # ASCII码 65-90大写字母A-Z；98-122小写字母a-z；48-57数字0-9.range函数不包含尾数值，一定要注意
#         if ord(instr)in range(65, 91)or ord(instr)in range(97, 123)or ord(instr)in range(48, 58):
#             print(ord(instr))
#         else:
#             print("输入数字不合法，退出程序！")
#             break
#     else:
#         print("输入长度超过一个字符，重新输入")
#         instr = "0"


for i in range(20):
    print((i+1) * "*")

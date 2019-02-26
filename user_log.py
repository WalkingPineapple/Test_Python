# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/26 15:43
# FileName    : user_log.PY
# dev tools   : PyCharm


# 记录用户日志
import time
def showinfo():
    print("输入提示数字，执行相应操作 0：退出 1：查看日志")

def wirte_log(username):
    '''写日志'''

    with open('user_log.txt','a') as f:
        string="用户名：{} 登录时间：{}\r".format(username ,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        f.write(string)
def read_log():

    with open('user_log.txt' ,'r') as  f:
        while True:
            line=f.readline()
            if line=='':
                break
            print(line)
if __name__=="__main__":
    username=input("请输入用户名")
    while len(username)<2:
        print("用户名不少于两位")
        username = input("请输入用户名")
    password=input("请输入密码")
    while len(password) < 6:
        print("密码不少于两位")
        password = input("请输入密码")
    if username.__eq__("admin") | password.__eq__("admin2314"):
        print("登陆成功")
        wirte_log(username)
        showinfo()
        num=int(input("请输入数字"))
        while True:
            if num==0:
                print("退出成功")
                break
            elif num==1:
                print("查看日志")
                read_log()
                showinfo()
                num=int(input("请继续执行操作"))
            else:
                print("您输入有误")
                showinfo()
                num=int(input("请输入操作数"))
    else:
        print("登陆失败，请联系管理员")

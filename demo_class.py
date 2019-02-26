# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/23 19:33
# FileName    : classtask.PY
# dev tools   : PyCharm


# 银行账户资金交易

import prettytable as pt   #生成美观的ASCII格式的表格
class Bank:
    def __init__(self,balance,amount_log):
        self.balance=balance
        self.amount_log=amount_log
    def deposit(self):
         amount=float(input("请输入存款金额"))
         self.balance+=amount
         self.write_log(amount,"转入")
    def withdawl(self):
         amount=float(input("请输入取款金额"))
         if amount>self.balance:
             print("您的账户余额不足")
         else:
             self.balance-=amount
             self.write_log(amount,"取款")
    def print_log(self):
        tb=pt.PrettyTable()
        tb.field_names=["交易日期","摘要","金额","币种","余额"]
        for info in self.amount_log:
            if info[1]=='转入':
                amout='+{}'.format(info[2])
            else:
                amout='-{}'.format(info[2])
            tb.add_row([info[0],info[1],amout,'RMB',info[3]])
        print(tb)
    def write_log(self):
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取创建时间
        data = [create_time, handle, amout, self.balance]  # 组装列表
        self.acount_log.append(data)  # 添加到日志列表

def show_menu():
    """显示菜单"""
    menu = '''菜单
    0：退出
    1：存款
    2：取款
    3：打印交易详情
    '''
    print(menu)
if __name__ == "__main__":
    show_menu()
    num = float(input('请根据菜单输入操作编号：'))
    bank = Bank(5000,)
    while num!= 0 :
        if num == 1:
            bank.deposit()
        elif num == 2:
            bank.withdrawl()
        elif num == 3:
            bank.print_log()
        else:
            print('您的输入有误！')
        num = float(input('请根据菜单输入操作编号：'))
    print('您已退出系统')




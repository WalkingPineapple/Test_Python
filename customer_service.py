# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/26 16:11
# FileName    : customer_service.PY
# dev tools   : PyCharm

def find_answer(question):
    with open('reply.txt','r') as f :
        while True:
            line = f.readline()
            if not line:
                break
            keyword = line.split("|")[0]
            reply = line.split("|")[1]
            if keyword in question :
                return reply
        return False

if __name__  == '__main__':
    # 输入问题
    question = input('Hi,你好，小蜜在此等主人很久了，有什么烦恼快和小蜜说说： ')
    # 文件中匹配
    while True:
        if question == 'bye':
            break
        reply = find_answer(question)
        if not reply:
            question = input('小蜜不懂您在说什么，您可以问一些与订单、账户和支付相关的内容（退出请输入bye）： ')
        else :
            print(reply)
            question = input('小主，您可以问一些与订单、账户和支付相关的内容（退出请输入bye）： ')

    print('小主再见')
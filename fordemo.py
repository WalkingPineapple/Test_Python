# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/20 16:21
# FileName    : fordemo.PY
# dev tools   : PyCharm

for i in range(20):
    print((i+1) * "*")

    head = "排名\t中文名\t\t\t财富\t\t年龄\t类别\t国家"
    data = ["1\t杰夫贝素斯\t\t1284亿美元\t54\t科技\t美国",
            "2\t比尔盖茨\t\t915亿美元\t62\t科技\t美国",
            "3\t沃伦巴菲特\t\t879亿美元\t87\t投资\t美国",
            "4\t伯纳德阿诺特及家族\t764亿美元\t69\t商业\t法国",
            "5\t马克扎克伯格\t\t735亿美元\t33\t科技\t美国",
            "6\t卡浩斯斯利烟埃卢及家族\t695亿美元\t78\t科技\t墨西哥",
            "7\t阿曼西奥·奥特加\t660亿美元\t81\t商业\t西班牙",
            "8\t拉里埃里森\t\t632亿美元\t73\t科技\t美国",
            "9\t大卫科赫\t\t608亿美元\t77\t能源\t美国",
            "10\t查尔斯·科赫\t\t608亿美元\t82\t能源\t美国",
            "11\t拉里佩奇\t\t522亿美元\t44\t科技\t美国",
            "12\t迈克尔布隆信格\t\t508亿美元\t76\t科技\t美国",
            "13\t谢尔盖布林\t\t508亿美元\t44\t科技\t美国",
            "14\t马化腾\t\t\t491亿美元\t46\t科技\t中国",
            "15\t梅耶尔贝当古\t\t446亿美元\t64\t商业\t法国",
            "16\t吉姆沃尔顿\t\t419亿美元\t69\t商业\t美国",
            "17\t罗伯森沃尔顿\t\t418亿美元\t73\t商业\t美国",
            "18\t艾丽斯沃尔顿\t\t416亿美元\t68\t商业\t法国",
            "19\t谢尔登阿德尔森\t\t411亿美元\t84\t娱乐\t美国",
            "20\t马云\t\t\t406亿美元\t53\t科技\t中国"]
    file = open("NEW.txt", 'w')  # 打开保存数据的文件，如果文件不存在，则创建该文件
    strlist = []
    print(head)
    # str=list.split(",")
    for item in data:
        print(item)
        if item.find("科技") != -1:
            strlist.append(item)
    print("*****************福布斯科技排行榜*******************************")
    print("科技排名  " + head)
    file.write("科技排名   " + head + "\n")
    i = 0
    for item in strlist:
        i = i + 1
        print(str(i) + "          " + item)
        file.write(str(i) + "          " + item + "\n")  # 写入文件
    file.close() 
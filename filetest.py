# _*_ coding  : UTF-8 _*_
# Author      : CJ
# Time        : 2019/2/25 14:13
# FileName    : filetest.PY
# dev tools   : PyCharm




file=open('NEW.txt','r')
print(file)

file=open('file_test.txt' ,'w')

file_image=open('logo-login.png','rb')
print(file_image)


file.close()
file_image.close()

with open('file_with','w') as file_with:
    pass






with open('line.txt','r') as file:
    # linenumber=0
    # while True:
    #     linenumber+=1
    #     line=file.readline()
    #     if line=='':
    #         break
    #     print(linenumber,line)



    lines=file.readlines()
    print(lines)










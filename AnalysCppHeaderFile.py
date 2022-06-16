import os

listAll = []

def GetFileNameFromLine(line):
    pos = line.rfind('/')
    if (pos != -1):
        return line[pos + 1 :]
    return line

def PrintList(list):
    if (len(list) == 0):
        return
    for i in range(0, len(list)):
        print (list[i])
    print ()
    return

def AppendList(list):
    global listAll
    for i in range(0, len(list)):
        listAll.append(list[i])

def cmpList(listAll, listNow):
    if (len(listAll) != len(listNow)):
        return False
    for i in range(0, len(listAll)):
        if (listAll[i] != listNow[i]):
            return False
    return True

def dealCppData(fileName):
    file = open("cppdata")
    global listAll
    #print ("fileName is " + fileName)

    # 元素声明
    '''
    list = []          ## 空列表
    list.append('Google')   ## 使用 append() 添加元素
    list.append('Runoob')
    '''
    listNow = []
    listMyself = []
    listc = []
    listsys = []
    listcpp = []
    listothers = []

    shortName = GetFileNameFromLine(fileName).replace(".cpp", "")
    #print ("shortName is " + shortName)

    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        strlist = line.split(':')
        headInfo = strlist[1]
        listNow.append(headInfo)
        #print (headInfo)
        expr1 = shortName + ".h"
        if expr1 in headInfo:
            listMyself.append(headInfo)
        elif "<sys/" in headInfo:
            listsys.append(headInfo)
        elif ".h" in headInfo and "<" in headInfo:
            listc.append(headInfo)
        elif "<" in headInfo and ".h" not in headInfo:
            listcpp.append(headInfo)
        else:
            listothers.append(headInfo)
    listMyself.sort()
    listc.sort()
    listsys.sort()
    listcpp.sort()
    listothers.sort()

    # print now
    AppendList(listMyself)
    AppendList(listc)
    AppendList(listsys)
    AppendList(listcpp)
    AppendList(listothers)

    # cmpList
    if (cmpList(listAll, listNow) == False):
        print ("文件 " + fileName + " 头文件包含顺序出现了差错")
        print ("当前顺序为:")
        PrintList(listNow)
        print ("应有的顺序为:")
        PrintList(listMyself)
        PrintList(listc)
        PrintList(listsys)
        PrintList(listcpp)
        PrintList(listothers)
        print ()
        print ()

    listAll.clear()

os.system("find * -name *.cpp >data")
file = open("data")
while True:
    line = file.readline().rstrip('\n')
    if not line:
        break
    cmd = "grep \"#include\" " + line + " -nr > cppdata"
    os.system(cmd)
    dealCppData(line)

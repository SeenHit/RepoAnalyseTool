import sys
import os

def getAllRepo():
    dataPath = "RepoTool/data"
    #os.system("find * -name *.git > " + dataPath)
    #os.system("nohup sed -i 's/\/.git//g' " + dataPath)
    file = open(dataPath)
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        repoName = getRepoNameFromLine(line)
        if os.path.isdir(line):
            print ("路径为:" + line + "   仓库名为:" + repoName)

def getGitCloneUrl(repoPath):
    os.system("cd " + repoPath + "; git remote -v > remoteInfo")
    file = open(repoPath + "/remoteInfo")
    url = file.readline().rstrip('\n')
    pos = url.find("git")
    os.system("rm -rf " + repoPath + "/remoteInfo")
    return url[pos :] 

def seachAllRepo(reponame):
    dataPath = "RepoTool/data"
    #os.system("find * -name *.git > " + dataPath)
    #os.system("nohup sed -i 's/\/.git//g' " + dataPath)
    file = open(dataPath)
    count = 0
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        repoName = getRepoNameFromLine(line)
        if (reponame in repoName):
            if os.path.isdir(line):
                cloneUrl = getGitCloneUrl(line)
                print ("已经找到类似的路径，路径为:" + line + "   仓库名为:" + repoName + " 克隆url是:" + cloneUrl)
                count = count + 1

    if (count == 0):
        print ("没有您想要的检索结果")

def checkRepoStatus(filePath):
    try:
        #print ("filePath is " + filePath)
        file = open(filePath)
        while True:
            line = file.readline().rstrip('\n')
            if not line:
                break
            if "modified" in line:
                file.close()
                return True
        file.close()
        return False
    except:
        return False

def searchModifiedRepo():
    dataPath = "RepoTool/data"
    #os.system("find * -name *.git > " + dataPath)
    #os.system("nohup sed -i 's/\/.git//g' " + dataPath)
    file = open(dataPath)
    count = 0
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        repoName = getRepoNameFromLine(line)
        cmd = "cd " + line + ";" + "git status > statusTmp ; cd -"
        os.system(cmd)
        filePath = line + "/statusTmp"
        if checkRepoStatus(filePath):
            cloneUrl = getGitCloneUrl(line)
            print ("该仓库最近有修改，路径为:" + line + "   仓库名为:" + repoName + " 克隆url是:" + cloneUrl)
            continue

def getRepoNameFromLine(line):
    pos = line.rfind("/")
    if (pos != -1):
        repoName = line[pos + 1 :]
        return repoName
    return line

def getAbsPath():
    absPath = os.path.abspath(".")
    print (absPath)
    return absPath

def getAllCommit():
    absPath = getAbsPath()
    dataPath = "RepoTool/data"
    os.system("find * -name \"*.git\" > " + dataPath)
    os.system("nohup sed -i 's/\/.git//g' " + dataPath)
    file = open(dataPath)
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        repoName = getRepoNameFromLine(line)
        if os.path.isdir(line):
            os.system("cd " + line + "; nohup git log --oneline > "  + absPath + "/RepoTool/" + repoName + "_commitInfo")
    os.system("cd -")
    os.system("cat *_commitInfo > wholeCommit")
    
def CommitSearch(keyword):
    #getAllCommit()
    os.system("cd RepoTool; grep \"" + keyword + "\" * -nr > searchResult")
    os.system("cd RepoTool; nohup sed -i 's/_commitInfo//g' searchResult")
    
    file = open("RepoTool/searchResult")
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        pos = line.find(' ')
        descrition = line[pos + 1 :]
        otherInfo = line[0 : pos]
        strlist = otherInfo.split(':')
        commitID = strlist[2]
        repoName = strlist[0]
        print (" 仓库名:" + repoName + " \t\t\t\tcommitID:" + commitID + " \tcommit描述:" + descrition)
    os.system("cd RepoTool; rm -rf searchResult")

def findRepoLocalPath(repoName):
    os.system("nohup find * -name " + repoName + " |grep -v \"out\" > RepoTool/repoResult")
    file = open("RepoTool/repoResult")
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        if (isRepoPathValid(line)):
            os.system("cd RepoTool; rm -rf repoResult")
            return line

    os.system("cd RepoTool; rm -rf repoResult")
    return ""

def isRepoPathValid(repoPath):
    try:
        for i in os.listdir(repoPath):
            if ".git" in i:
                return True
        return False
    except:
        return False

def ShowCommitID(commitID):
    #getAllCommit()
    os.system("cd RepoTool; grep \"" + commitID + "\" * -nr |grep -v \"commitResult\" > commitResult")
    os.system("cd RepoTool; nohup sed -i 's/_commitInfo//g' commitResult")

    file = open("RepoTool/commitResult")
    count = 0
    while True:
        line = file.readline().rstrip('\n')
        if not line:
            break
        count = count + 1
        #strlist = line.split(' ')
        pos = line.find(' ')
        descrition = line[pos + 1 :]
        otherInfo = line[0 : pos]
        strlist = otherInfo.split(':')
        commitID = strlist[2]
        repoName = strlist[0]
        #print (" 仓库名:" + repoName + " \t\t\t\tcommitID:" + commitID + " \tcommit描述:" + descrition)
        repoPath = findRepoLocalPath(repoName)
        if isRepoPathValid(repoPath):
            os.system("cd " + repoPath + "; git show " + commitID)
            break

    if (count == 0):
        print ("没有找到对应的commit id")
    os.system("cd RepoTool; rm -rf commitResult")

def IsNeedUpate():
    count = 0
    for i in os.listdir("RepoTool"):
        count = count + 1
    if (count != 0):
        return False
    return True
    

def updateAllResources():
    # 先删除原来的所有的资源
    os.system("cd RepoTool; rm -rf *")
    # 更新新资源进来
    getAllCommit()
    
    
storageDir = "RepoTool" 
if (os.path.exists(storageDir) == 0):
    os.system("mkdir " + storageDir)
#getAllRepo()
#getAllCommit()
#getAbsPath()
#CommitSearch("切换")
#ShowCommitID("bb48485")
if (len(sys.argv) < 2):
    print ("您没有输入命令参数，请输入命令参数")
    os._exit(0)

cmd = sys.argv[1]
#print (cmd)
#print (len(sys.argv))

# 需要更新所有的资源
if (cmd == "update"):
    updateAllResources()

if (cmd == "modified"):
    searchModifiedRepo()

if (cmd == "listall"):
    if (len(sys.argv) < 3):
        print ("您没有输入option参数，请输入option参数")
        os._exit(0)
    option = sys.argv[2]
    if (option == "repo"):
        if IsNeedUpate():
            updateAllResources()
        getAllRepo()
    else:
        print ("不支持的命令!")
    os._exit(0)

if (cmd == "search"):
    if (len(sys.argv) < 4):
        print ("您没有输入option参数，请输入option参数")
        os._exit(0)
    option = sys.argv[2]
    if (option == "repo"):
        if IsNeedUpate():
            updateAllResources()
        repo = sys.argv[3]
        seachAllRepo(repo)
    elif (option == "commit"):
        if IsNeedUpate():
            updateAllResources()
        commitKeyword = sys.argv[3]
        CommitSearch(commitKeyword)
    else:
        print ("不支持的命令!")
    os._exit(0)

if (cmd == "show"):
    if (len(sys.argv) < 4):
        print ("您没有输入commit参数，请输入option参数")
        os._exit(0)
    if IsNeedUpate():
        updateAllResources()
    
    option = sys.argv[2]
    if (option == "repo"):
        repo = sys.argv[3]
        seachAllRepo(repo)
    elif (option == "commit"):
        commitID = sys.argv[3]
        ShowCommitID(commitID)
    else:
        print ("不支持的命令!")
    os._exit(0)

import os

os.system("find * -name *.cpp > data")
file = open("data")
while True:
    line = file.readline().rstrip('\n')
    if not line:
        break
    cmd = "nohup cpplint " + line
    os.system(cmd)
os.system("rm -rf data")

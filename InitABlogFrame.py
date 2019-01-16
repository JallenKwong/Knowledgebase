# -*- coding: utf-8 -*

# 创建 博客基本框架 以博客标题命名的文件夹，文件夹内有image文件夹和README.md

import os,datetime

print "Please input the blog title."
dirName = raw_input()

while os.path.exists(dirName):
	print "Directory is existed. Please input again!"
	dirName = raw_input()

#os.makedirs(dirName)
os.makedirs("NF - " + dirName + "\\image")

md = open("NF - " + dirName + "\\README.md",'w')
md.write("# " + dirName + " #\n\n")
md.write("creation date:" + datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S") + "\n\n")
md.write("tag:\n\n")
md.write("[]()\n\n")

md.close()

print "Mission completed. Press Enter to exit. "

try:
    raw_input()
    print "Bye!"
except:
    print "Bye!"


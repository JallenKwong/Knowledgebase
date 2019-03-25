# -*- coding: utf-8 -*

#提取 ## XX ## 作索引 [XX](#XX), 直接打印出来

import re

filePath = 'README.md'

textFile = open(filePath, 'r')

indexRegex = re.compile(r'^## (.*) ##$')

for line in textFile.readlines():
    if indexRegex.match(line):
        
        mo = indexRegex.search(line)

        # line
        indexName = mo.group(1).decode('utf-8')#decode解码，encode编码
        print '[%s](#%s)\n'%(indexName, indexName.lower())

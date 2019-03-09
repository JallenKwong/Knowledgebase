# -*- coding: utf-8 -*

# 将数字变成标题2，如：02 -> ## 02 ##

import re

fileName = 'README.md'

textFile = open(fileName, 'r')

numRegex = re.compile(r'^(\d{2})$')

lines = textFile.readlines()

textFile.close()

###

textFile = open(fileName, 'w')

for line in lines:
    if numRegex.match(line):
        thing = numRegex.search(line).group(1)
        line = '## %s ##\n' % thing
    textFile.write(line)

textFile.close()

print 'Done!'


#!/usr/bin/env python3

import re
import sys

enzyme = sys.argv[1]
sequence = sys.argv[2]

with open('bionet.txt', 'r') as myFile:
  file = myFile.read()
  
  count = 0
  lineList = re.findall(r'[^\n]+',file)
  reDict = {}
  
  for i in range(len(lineList)):
    if i>10:
      if '(' in lineList[i]:
        found = re.search(r'([\S]+)([\s]+)([\S]+)([\s]+)([\S]+)', lineList[i])
        reDict[found.group(1)] = found.group(5)
        reDict[found.group(3)] = found.group(5)
      else:
        found = re.search(r'([\S]+)([\s]+)([\S]+)', lineList[i])
        reDict[found.group(1)] = found.group(3)

  print(reDict)

  




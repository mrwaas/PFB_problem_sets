#!/usr/bin/env python3

import re
count = 1

with open('Python_07_nobody.txt', 'r') as myFile:
  for line in myFile:
    for found in re.finditer(r'Nobody', line):
      print('line:',count,'found at',found.start()+1)
    count+=1

#!/usr/bin/env python3

import re
count = 1

with open('Python_07_nobody.txt', 'r') as myFile, open('Python_07_yuma.txt', 'w') as newWrite:
  for line in myFile:
    newLine = re.sub(r'Nobody' , 'Yuma', line)
    newWrite.write(newLine)






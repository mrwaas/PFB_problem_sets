#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta.txt', 'r') as myFile:
  file = myFile.read()
  cutFile = re.sub(r'([AG])(AATT[CT])',r'\1^AATT\2',file)
  print(cutFile)      
  cutFileLin = cutFile.replace('\n','')[5:]
  fragments = re.findall(r'[^\^]+',cutFileLin)
  print(fragments)
  print(sorted(fragments, key = len, reverse=True))




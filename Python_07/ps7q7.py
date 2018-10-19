#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta.txt', 'r') as myFile:
  file = myFile.read()
  cutFile = re.sub(r'(([AG])(AATT)([CT]))',r'\1^AATT\3',file)
  print(cutFile)      






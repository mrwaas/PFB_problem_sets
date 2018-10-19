#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta.txt', 'r') as myFile:
  file = myFile.read()
  mySites = re.findall(r'([AG]AATT[CT])', file)
  print(mySites)  






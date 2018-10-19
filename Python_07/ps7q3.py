#!/usr/bin/env python3

import re

with open('Python_07.fasta.txt', 'r') as myFile:
  file = myFile.read()
  myHeaders = re.findall(r'>[^\n]+', file)
  print(myHeaders)  






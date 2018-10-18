#!/usr/bin/env python3

file = open('Python_06.txt','r')
wFile= open('Python_06_uc.txt','w')

for line in file:
  line = line.upper()
  wFile.write(line)

  

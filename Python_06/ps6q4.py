#!/usr/bin/env python3

file = open('Python_06.fastq.txt','r')
lineCount = 0
charCount = 0

for line in file:
   lineCount += 1
   charCount += len(line.rstrip())

print('lines:',lineCount)
print('chars:',charCount)
print('ave line len:',charCount/lineCount)

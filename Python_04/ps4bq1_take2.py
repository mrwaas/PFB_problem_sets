#!/usr/bin/env python3

import random

dna = input('Please enter a DNA sequence: ')
dnaLen = len(dna)
dnaLis = list(dna)

for nt in range(dnaLen):
   randApos=random.randrange(dnaLen)
   randBpos=random.randrange(dnaLen)
   randA = dnaLis[randApos]
   randB = dnaLis[randBpos]
   dnaLis[randApos] = randB
   dnaLis[randBpos] = randA
   print(dnaLis)

dnaSeq=''
for nt in range(dnaLen):
   dnaSeq += dnaLis[nt]
   
print(dnaSeq)
   


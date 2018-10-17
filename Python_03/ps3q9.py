#!/usr/bin/env python3

import sys

dna = sys.argv[1]

ccDNA = dna.upper()

aCount = ccDNA.count('A')
tCount = ccDNA.count('T')
cCount = ccDNA.count('C')
gCount = ccDNA.count('G')

atContent = (aCount + tCount)/len(ccDNA)
cgContent = (gCount + cCount)/len(ccDNA)

print('AT content:',atContent,'\nCG content:',cgContent)

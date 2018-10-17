#!/usr/bin/env python3

import sys

dna = sys.argv[1]

ccDNA = dna.upper()

tDNA = ccDNA.replace('T','a')
aDNA = tDNA.replace('A','t')
cDNA = aDNA.replace('C','g')
gDNA = cDNA.replace('G','c')

compDNA = gDNA.upper()

rCdna = compDNA[::-1]

print(ccDNA)
print(compDNA)
print(rCdna)

#!/usr/bin/env python3

import sys

dna = sys.argv[1]

ccDNA = dna.upper()

numT = ccDNA.count('T')

print(numT)

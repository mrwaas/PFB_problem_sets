#!/usr/bin/env python3

import sys

dna = sys.argv[1]
ccDNA = dna.upper()

ssDNA = ccDNA[99:200]

gCount = ssDNA.count('G')



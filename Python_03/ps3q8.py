#!/usr/bin/env python3

import sys

dna = sys.argv[1]

rnaI = dna.replace('T','U')

rna = rnaI.replace('t','u')

print(rna)

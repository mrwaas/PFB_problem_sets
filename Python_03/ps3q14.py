#!/usr/bin/env python3

import sys

dna = sys.argv[1]
ccDNA = dna.upper()

ecoSite = ccDNA.find('GAATTC')

string= 'The EcoR1 site is at: {} and the sequence is {}.'

print(string.format(ecoSite+1,ccDNA[ecoSite:ecoSite+6]))

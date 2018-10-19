#!/usr/bin/env python3

def reverse_complement(dna):
    aDNA = dna.replace('A','t')
    tDNA = aDNA.replace('T','a')
    cDNA = tDNA.replace('C','g')
    gDNA = cDNA.replace('G','c')

    comp_dna = gDNA.upper()
    rc_dna = comp_dna[::-1]
    
    return rc_dna

dna = 'AAAAAAAAAAAAAAAAAG'
print('The sequence is',dna)

print('The reverse complement is',reverse_complement(dna))



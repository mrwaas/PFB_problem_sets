#!/usr/bin/env python3

file = open('Python_06.seq.txt','r')

geneSet = {}

for line in file:
  line = line.rstrip()
  id,seq = line.split()
  geneSet[id] = seq

geneSetRC = {}

for gene in geneSet:
  dna = geneSet[gene]
  tDNA = dna.replace('T','a')
  aDNA = tDNA.replace('A','t')
  cDNA = aDNA.replace('C','g')
  gDNA = cDNA.replace('G','c')

  compDNA = gDNA.upper()
  rCdna = compDNA[::-1]
  
  geneSetRC[gene] = rCdna
  
stOUT = 'This file is the reverse complement of the genes.\n'

for gene in geneSetRC:
  stOUT += '\n'
  stOUT += '>'
  stOUT += gene
  stOUT += '\n'
  stOUT += geneSetRC[gene]

print(stOUT)

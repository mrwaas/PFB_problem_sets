#!/usr/bin/env python3

import sys
import re

file = sys.argv[1]

seq_dict= {}
mod_dict= {}

with open(file, 'r') as myFile:
  for line in myFile:
    line = line.rstrip()
    if line.startswith('>'):
        found = re.search(r'([\S]+)',line)
        seq_name = found.group().lstrip('>')
        seq_dict[seq_name] = ''        
    else:
        seq_dict[seq_name] += line

def formatDNA(dna, line_length):
    dna = dna.replace('\n','')
    print(dna)
    dna_length = len(dna)
    num_lines = int((dna_length / line_length)+1)
    formatted_dna = ''
    for line in range(num_lines):
        formatted_dna += dna[line*line_length:(line+1)*line_length] + '\n' 
    return formatted_dna

for gene in seq_dict:
    mod_dict[gene] = formatDNA(seq_dict[gene], int(sys.argv[2]))
    
with open('formatted.fasta','w') as myFile:
    for gene in mod_dict:
        myFile.write('>'+gene+'\n'+mod_dict[gene])

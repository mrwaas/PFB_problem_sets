#!/usr/bin/env python3

from Bio import SeqIO
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as myFile:
    for line in myFile:
       line = line.rstrip()
       specs = line.split()
       #print(len(specs))
       #spec = specs[2]
       print(specs[2]) 

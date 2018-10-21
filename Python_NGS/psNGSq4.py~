#!/usr/bin/env python3

from Bio import SeqIO
import sys

file_name = sys.argv[1]
seq_dict = {}
trimmed_fastq = ''

ID_set = set()
ID_list = []
counts = {}

# split each line of the file based on MI id - add to a set and to a list

with open(file_name, 'r') as myFile:
    for line in myFile:
        ID = line.split('MI:i:')[1]
        ID = ID.rstrip()
        ID_set.add(ID)
        ID_list.append(ID)

    # count the instances of each ID contained within the set in the list 
    
    for ID in ID_set:
        counts[ID] = ID_list.count(ID)

    print(counts)
        

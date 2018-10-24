#!/usr/bin/env python3

import sys
from Bio import SeqIO
from mattsfavorite import *

file_name = sys.argv[1]

count_dict = {}

with open(file_name, 'r') as file_obj:
    for line in file_obj:
        read = line.split()[0]
        gene = line.split()[2].split('^')[0]
        if gene in count_dict:
            count_dict[gene].add(read)
        else :
            count_dict[gene] = {read}

    for entry in count_dict:
        print(entry+'\t'+str(len(count_dict[entry])))

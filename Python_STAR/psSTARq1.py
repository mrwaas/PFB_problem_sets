#!/usr/bin/env python3

import sys

log_final_file = sys.argv[1]
log_file = sys.argv[2]

# find the input file name and the reference genome

with open( log_file , 'r') as logfile:
    read_files = []
    read_genome = []
    for line in logfile:
        if line.startswith('readFilesIn'):
            read_files = line.split()[1::]
        if line.startswith('genomeDir'):
            read_genome = line.split()[1]
    print(read_files)
    print(read_genome)

with open( log_final_file , 'r') as lff:
    splice_dict = {}
    for line in lff:
        print(line.lstrip())
    

    

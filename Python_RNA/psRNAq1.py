#!/usr/bin/env python3

import sys
from Bio import SeqIO
from mattsfavorite import *

kmer_length = int(sys.argv[1])
file_name = sys.argv[2]
num_top_kmers = int(sys.argv[3])

# kmer counter

kmer_dict = {}

for seq_record in SeqIO.parse(file_name, 'fastq'):
    seq_str = str(seq_record.seq)
    
    for i in range(len(seq_str)-kmer_length+1):
        kmer = seq_str[i:i+kmer_length:]
        if kmer_dict.get(kmer) == None:
            kmer_dict[kmer] = 1
        else :
            kmer_dict[kmer] += 1
pl(kmer_dict)

top10_kmer = {}

sorted_kmers =  sorted(kmer_dict.keys(), key = lambda x: kmer_dict[x], reverse = True)

for i in range(num_top_kmers):
    print(sorted_kmers[i]+'\t'+str(kmer_dict[sorted_kmers[i]]))



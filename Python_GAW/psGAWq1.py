#!/usr/bin/env python3

import sys

from Bio import SeqIO

file_name = sys.argv[1]

sequence_dict = {}

for seq_record in SeqIO.parse(file_name, 'fasta'):
    sequence_dict[seq_record.id] = str(seq_record.seq)

print(len(sequence_dict))

len_list = []

for key in sequence_dict:
    len_list.append(len(sequence_dict[key]))

print(min(len_list))
print(max(len_list))

total_len = 0
for contig in range(len(len_list)):
    total_len += len_list[contig]

print(total_len)

n50len = total_len / 2

print(n50len)

sorted_len_list = sorted(len_list, reverse = True)

print(sorted_len_list)

i = 0
sum_len = 0

while sum_len < n50len:
    sum_len += sorted_len_list[i]
    if sum_len > n50len:
        n50 = sorted_len_list[i]
    i += 1
print(i)
print(n50)

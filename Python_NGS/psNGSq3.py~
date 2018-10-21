#!/usr/bin/env python3

from Bio import SeqIO
import sys

file_name = sys.argv[1]
seq_dict = {}
trimmed_fastq = ''

# parse fasta into dictionary of {id: seq}
for seq_record in SeqIO.parse(file_name, 'fastq'):
    fastq = seq_record.format('fastq')
    qual = fastq.split('+\n')[1]
    trim_qual = qual[5::]
    trim_seq = seq_record.seq[5::]

    trimmed_fastq = seq_record.id + '\n' + trim_seq + '\n' + '+\n' + trim_qual + '\n'

# determine the fraction of nt above a quality score of 30

for seq_record in SeqIO.parse(file_name, 'fastq'):
    qual_str = seq_record.format('qual')

    extract_quality = qual_str.split('\n', maxsplit = 1)[1]
    quality_list = extract_quality.replace('\n' , ' ').split()

    qual_count = 0
    trash_count = 0
    
    for nt in range(len(quality_list)):
        
        if int(quality_list[nt]) > 30:
            qual_count += 1
        else:
            trash_count += 1
    print('Percent of good reads:',str(qual_count/(qual_count+trash_count)))
    

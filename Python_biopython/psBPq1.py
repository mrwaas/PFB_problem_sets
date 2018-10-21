#!/usr/bin/env python3

from Bio import SeqIO
import sys
 
    
class DNAseq(object):

    #define class attributes

    def __init__(self, sequence, gene_name, organism):
        self.sequence = sequence
        self.gene_name = gene_name
        self.organism = organism


    def length(self):
        return len(self.sequence)

    def nt_comp(self):
        countA = self.sequence.count('A')
        countG = self.sequence.count('G')
        countT = self.sequence.count('T')
        countC = self.sequence.count('C')
        comp = { 'A':countA, 'G':countG , 'T':countT, 'C':countC }
        return comp

    def gc_cont(self):
        gc_cont = (self.nt_comp()['G'] + self.nt_comp()['C']) / self.length()
        return gc_cont

    def write_fasta(self):
        head = '>'+self.gene_name+'\n'
        seq = self.sequence+'\n'
        return (head + seq)
    
file_name = sys.argv[1]
seq_dict = {}

# parse fasta into dictionary of {id: seq}
for seq_record in SeqIO.parse(file_name, 'fasta'):
    seq_dict[seq_record.id] = str(seq_record.seq)

print('number of records:',len(seq_dict))

# calculate the total number of nt
num_nt = 0

for record in seq_dict:
    num_nt += len(seq_dict[record])

print('number of nt:',num_nt)

# calculate the average sequence length
print('ave seq length:',str(num_nt/len(seq_dict)))

# determine the shortest sequence length and the max sequence length

length_list = []

for record in seq_dict:
    length_list.append(len(seq_dict[record])) 

print('The shortest sequence is length:',str(min(length_list))+'\n'+'The longest sequence is length:',str(max(length_list)))

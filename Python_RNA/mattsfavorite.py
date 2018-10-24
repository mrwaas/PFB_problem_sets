#!/usr/bin/env python3

def pl(input):
    print(len(input))

def pt(input):
    print(type(input))

def dict_my_fasta(file_name):

    from Bio import SeqIO

    fasta_dict = {}
    
    for seq_record in SeqIO.parse(file_name, 'fasta'):
        fasta_dict[str(seq_record.id)] = str(seq_record.seq)

    return fasta_dict

    

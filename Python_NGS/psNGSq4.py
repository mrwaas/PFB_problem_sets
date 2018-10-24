#!/usr/bin/env python3

from Bio import SeqIO
import sys

file_name = sys.argv[1]

feature_type_gene = 0
gene_length_list = []

# count the number of gene files in the file

with open(file_name, 'r') as myFile:
    for line in myFile:
       if line.startswith('##') == False :
           feature_type = line.split()[2]
           if feature_type  == 'gene':
               feature_type_gene += 1

               # creates a list of the length of genes
               gene_length = int(line.split()[4])-int(line.split()[3])
               gene_length_list.append(gene_length)

    print(gene_length_list)          
    print(feature_type_gene)

    
              
    

#!/usr/bin/env python3

class DNAseq(object):

    #define class attributes

    def __init__(self, sequence, gene_name, organism):

        self.sequence = sequence
        self.gene_name = gene_name
        self.organism = organism



q2seqObj = DNAseq('AAACCCTTTGGG', 'mygene', 'gazorpazorp')
print(q2seqObj)
    

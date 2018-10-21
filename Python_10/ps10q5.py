#!/usr/bin/env python3

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
    
q2seqObj = DNAseq('AAACCCTTTGGG', 'mygene', 'gazorpazorp')

print(q2seqObj.gc_cont())


    

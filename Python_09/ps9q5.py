#!/usr/bin/env python3

def gc_content(dna):
    c_count = dna.count('C')
    g_count = dna.count('G')
    gc_cont = (c_count + g_count)/len(dna)
    form_gc_c = '{:.2%}'.format(gc_cont)
    return form_gc_c

dna = 'AAAAAAAAAAAAAAAAAG'

print('The GC content is',gc_content(dna))



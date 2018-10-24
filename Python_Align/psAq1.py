#!/usr/bin/env python3

sequence1 = 'agtctgtca'
sequence2 = 'gatctctgc'

def rc(dna):
    dna = dna.replace('a','T')
    dna = dna.replace('t','A')
    dna = dna.replace('c','G')
    dna = dna.replace('g','C')

    dna = dna.lower()
    dna = dna[::-1]

    return dna

# calculate the match score using +1 for match and -1 for mismatch

match_score = 0

for nt in range(len(sequence1)):
    if sequence1[nt] == sequence2[nt]:
        match_score += 1
    else :
        match_score += -1

print(match_score)


# calculate the match score using +1 for match and -1 for mismatch

match_score = 0

for nt in range(len(sequence1)):
    if sequence1[nt] == rc(sequence2)[nt]:
        match_score += 1
    else :
        match_score += -1

print(match_score)


# calculate the match score using +1 for match and -1 for mismatch

match_score = 0

for nt in range(len(sequence1)):
    if rc(sequence1)[nt] == sequence2[nt]:
        match_score += 1
    else :
        match_score += -1

print(match_score)


# calculate the match score using +1 for match and -1 for mismatch

match_score = 0

for nt in range(len(sequence1)):
    if rc(sequence1)[nt] == rc(sequence2)[nt]:
        match_score += 1
    else :
        match_score += -1

print(match_score)

# calculate the match score using +2 for match and -2 for mismatch

match_score_2 = 0

for nt in range(len(sequence1)):
    if sequence1[nt] == sequence2[nt]:
        match_score_2 += 2
    else :
        match_score_2 += -2

print(match_score_2)
    

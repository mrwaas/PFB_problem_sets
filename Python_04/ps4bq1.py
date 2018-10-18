#!/usr/bin/env python3

import random

dna = input('Please enter a DNA sequence: ')
dnaL = len(dna)
print(dna)
print(dnaL)
for nt in range(dnaL):
   randApos = random.randrange(dnaL)
   print(randApos)
   randBpos = random.randrange(dnaL)          
   print(randBpos)
   randA = dna[randApos]
   print(randA)
   randB = dna[randBpos]
   print(randB)
   preA = dna[:randApos]
   print(preA)
   postA = dna[randApos+1:]
   print(postA)
   subA = preA + randB + postA
   print(subA)
   preB = subA[:randBpos]
   print(preB)
   postB = subA[randBpos+1:]
   print(postB)
   subB = preB + randA + postB
   print('Shuffle',nt+1,'is',subB)

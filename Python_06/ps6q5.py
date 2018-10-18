#!/usr/bin/env python3

with open('alpaca_all_genes.tsv','r') as file:
  lineCount = 0
  allGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    allGenes.add(line)
    lineCount += 1

with open('alpaca_pigmentation_genes.tsv','r') as file:
  lineCount = 0
  pigGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    pigGenes.add(line)
    lineCount += 1

with open('alpaca_stemcellproliferation_genes.tsv','r') as file:
  lineCount = 0
  proGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    proGenes.add(line)
    lineCount += 1

with open('alpaca_transcriptionFactors.tsv','r') as file:
  lineCount = 0
  tfGenes=set()

  for line in file:
    if lineCount == 0:
      lineCount += 1
      continue
    tfGenes.add(line)
    lineCount += 1    

print(len(allGenes))
print(len(proGenes))
print(len(pigGenes))
print(len(tfGenes))

notInscp = allGenes - proGenes
print(len(notInscp))

proNpig = proGenes & pigGenes
print(len(proNpig))

proTF = proGenes & tfGenes
print(len(proTF))

#!/usr/bin/env python3

q11list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

q11len = [ (len(q11list[i]), q11list[i]) for i in range(4)]

print(q11len)
  
for i in range(4):
 text=str(q11len[i])
 text2=text.replace('(','')
 text3=text2.replace(')','')
 text4=text3.replace(', ','\t')
 print(i+1,'\t',text4)

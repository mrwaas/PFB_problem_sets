#!/usr/bin/env python3

q6list=[101,2,15,22,95,33,2,27,72,15,52]

q6list.sort()
evenSum=0
oddSum=0

for num in q6list:
   print(num)
   if num%2 == 0:
      evenSum+=num
   else :
      oddSum+=num
print('even sum:',evenSum)
print('odd sum:',oddSum)

   
      

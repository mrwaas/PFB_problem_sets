#!/usr/bin/env python3
import sys

myQ8var = float(sys.argv[1])

if myQ8var>0 :
   print('Positive')
   if myQ8var<50 :
      print('Your value is positive and smaller than 50')
elif myQ8var == 0 :
   print('Your number is equal to zero!')
else:
   print('Negative')



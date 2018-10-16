#!/usr/bin/env python3
import sys

myQ8var = float(sys.argv[1])

if myQ8var>0 :
   if myQ8var<50 :
      print('Your value is positive and smaller than 50')
      if myQ8var%2 == 0:
         print('Your value is positive, smaller than 50, and even!')
      else :
         print('Your value is positive, smaller than 50, but not even :(')
   else :
       if myQ8var%3 == 0:
         print('Your value is positive, greater than 50, and divisible by 3!')
       else:
         print('Your value is positive, greater than 50, but is NOT divisible by 3')
elif myQ8var == 0 :
   print('Your number is equal to zero!')
else:
   print('Negative')



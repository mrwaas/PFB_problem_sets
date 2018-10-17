#!/usr/bin/env python3

import sys

eV=int(sys.argv[len(sys.argv)-1])
cV=int(sys.argv[1])

while cV <= eV:
  if cV%2 != 0:
    print(cV)
  cV+=1    
    

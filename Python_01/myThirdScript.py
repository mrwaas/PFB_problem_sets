#!/usr/bin/env python3
import sys

myName = sys.argv[1]
myFaveColor = sys.argv[2]
myFaveActivity = sys.argv[3]
myFaveAnimal = sys.argv[4]

for  x in (range(len(sys.argv))):
	if x > 0:
		message = sys.argv[x]
		print(message)


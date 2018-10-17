#!/usr/bin/env python3

q2string = 'sapiens, erectus, neanderthalensis'

print(q2string)

q2list = q2string.split(', ')

print(q2list)

print(sorted(q2list))

print(sorted(q2list, key=len))

#!/usr/bin/env python3

myFav = { 'book' : 'I am a strange loop', 'song' : 'IACTMN', 'tree' : 'willow'}

myFav['organism'] = 'tardigrades'

myFav['organism'] = 'dog'

desired = input('Please enter a topic for  my fave thing: ');

print('Received input is:',desired)

thething = input('Please enter my favorite thing of this topic: ');

print('Received input is:',thething)

myFav[desired] = thething

print('my fave', desired,'is',thething)








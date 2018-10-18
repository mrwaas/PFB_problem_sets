#!/usr/bin/env python3

myFav = { 'book' : 'I am a strange loop', 'song' : 'IACTMN', 'tree' : 'willow'}

desired = input('Please select a topic to know my fave - select book, song, or tree: ');

print('Received input is:',desired)

print(myFav[desired])



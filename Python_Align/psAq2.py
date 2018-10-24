#!/usr/bin/env python3

import sys

import re

file_name = sys.argv[1]
head_str = ''
count = 0
head_list = []

with open(file_name, 'r') as myFile:
    for line in myFile:
        
        if line.startswith('>>'):
            
            if len(head_str) > 0:
                head_list.append(head_str.replace('\n', ''))

            head_str = ''
            count = 1
            
        if count == 1:
            head_str += line
            
        if line == '\n':
            count = 0

    print(head_list)

    for hit in range(len(head_list)):
        str = head_list[hit]
        ID = re.search(r'SP:(.+?)\s', str).group(1)
        print(ID)

        percent_query_coverage = re.search(r'in\s(.+?)\saa\soverlap', str).group(1)
        print(percent_query_coverage)

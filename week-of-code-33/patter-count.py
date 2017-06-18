#!/bin/python

import sys

def patternCount(s):

    binary = ''
    pattern = []
    for x in s:
        if not x.isalpha() and x == '1':
            if len(binary) >= 2:
                binary += str(x)
                pattern.append(int(binary, 2))
                binary='1'
            elif len(binary) == 0:
                binary += str(x)


        elif not x.isalpha() and x == '0' and len(binary) >=1:
            binary+=str(x)
        else:
            binary=''


    return len(pattern)
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)



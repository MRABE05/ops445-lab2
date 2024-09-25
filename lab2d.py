#!/usr/bin/env python3

import sys

#the check should be before the arguments

if len(sys.argv) != 3:
    print('Usage: '+ sys.argv[0] + " name age" )
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]


print('Hi ' + name + ', you are ' + str(age) + ' years old.')

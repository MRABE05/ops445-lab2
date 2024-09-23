#!/usr/bin/env python3

import sys

message = sys.argv[0]
name = sys.argv[1]
age = sys.argv[2]

print(len(sys.argv))
if len(sys.argv) == 3:
    print(len(sys.argv))
    print('Hi ' + name + ', you are ' + str(age) + ' years old.')
    sys.exit()




print('Usage: ' + message + " " + name + " " + age )
sys.exit()
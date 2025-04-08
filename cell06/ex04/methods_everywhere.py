#!/usr/bin/env python3

import sys

def shrink(txt):
    return txt[:8]

def enlarge(txt):
    return txt.ljust(8, 'Z')

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) < 8:
            print(enlarge(arg))
        elif len(arg) > 8:
            print(shrink(arg))
        else:
            print(arg)

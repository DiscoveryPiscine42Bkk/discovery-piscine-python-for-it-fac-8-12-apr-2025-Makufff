#!/usr/bin/env python3

import sys

def downcase_it(txt):
    return txt.lower()

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        print(downcase_it(arg))

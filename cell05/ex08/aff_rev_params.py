#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    arr = sys.argv
    arr.pop(0)
    arr.reverse()
    print(*arr, sep="\n")

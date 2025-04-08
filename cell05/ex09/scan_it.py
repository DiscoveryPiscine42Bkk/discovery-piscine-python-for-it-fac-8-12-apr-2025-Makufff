#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    text = sys.argv[2]
    fnd = sys.argv[1]
    count = text.count(fnd)
    print(count)

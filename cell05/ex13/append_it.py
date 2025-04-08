#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    arr = sys.argv
    arr.pop(0)

    for i in range(len(arr)):
        if arr[i].endswith("ism"):
            pass
        else:
            print(arr[i], end="ism\n")
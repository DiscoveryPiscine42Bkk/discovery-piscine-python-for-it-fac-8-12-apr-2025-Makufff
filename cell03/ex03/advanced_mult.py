#!/usr/bin/env python3

first = 0
second = 0

while first <= 10:
    print(f"Table of {first}:", end="")
    while second <= 10:
        print(f" {first * second}", end="")
        second +=1
    print("")
    second = 0
    first += 1
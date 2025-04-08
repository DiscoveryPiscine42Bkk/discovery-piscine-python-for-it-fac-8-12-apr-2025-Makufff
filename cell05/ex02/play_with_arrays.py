#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

new_array = [x + 2 for x in arr if x > 5]

print(f"Original array: {arr}")
print(f"New array:  {new_array}")

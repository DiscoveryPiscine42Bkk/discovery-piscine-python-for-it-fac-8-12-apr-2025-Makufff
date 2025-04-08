#!/usr/bin/env python3

n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))

ans = n1 * n2

string = f"{n1} x {n2} = {ans} \n"

if ans == 0:
    print(string + "The result is positive and negative.")
elif ans < 0:
    print(string + "The result is negative.")
else:
    print(string + "The result is positive.")
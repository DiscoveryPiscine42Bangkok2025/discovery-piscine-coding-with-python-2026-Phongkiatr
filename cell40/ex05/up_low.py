#!/usr/bin/env python3

s = input()

result = ""
for c in s:
    if c.islower():
        result += c.upper()
    elif c.isupper():
        result += c.lower()

print(result)
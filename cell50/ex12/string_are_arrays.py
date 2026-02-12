#!/usr/bin/env python3
import sys

def main():
    # พารามิเตอร์แค่ 1 ตัว
    if len(sys.argv) != 2:
        print("none")
        return

    s = sys.argv[1]

    # นับ 'z'
    result = ""
    for c in s:
        if c == 'z':
            result += 'z'

    if result == "":
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    main()

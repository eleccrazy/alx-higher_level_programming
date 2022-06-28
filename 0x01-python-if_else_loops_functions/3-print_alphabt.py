#!/usr/bin/python3
for i in "abcdefghijklmnopqrstuvwxyz":
    if (i == 'q' or i == 'e'):
        continue
    print(f"{i:s}", end='')

#!/usr/bin/env python3

import sys
from re import compile

try:
    address = int(sys.argv[1]) 
except:
    address = compile(sys.argv[1][1:-1])

line_num = 1

while True:
    line_content = input()
    print(line_content)
    if isinstance(address, int):
        if line_num == address:
            break
    else:
        if address.search(line_content):
            break
    
    line_num += 1
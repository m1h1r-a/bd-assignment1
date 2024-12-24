#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    line = line.strip()
    # print(f"before: {line}")
    if line[0]=='[' or line[0]==']':
        continue;
    line  = line.strip(',')
    # print(f"after: {line}")
    data = json.loads(line)
    print(data)

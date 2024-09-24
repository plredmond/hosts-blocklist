#!/usr/bin/env python3

import os
import re
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue # skip blanks

    first = line[0]
    last = line[-1]

    if '#' == first:
        continue # skip comments

    if '[' == first and ']' == last:
        continue # skip abp headers

    if '!' == first:
        continue # skip abp headers

    # lines are like '||domain^'
    m = re.match(r'\|\|([-\w\.]+)\^', line)
    assert m is not None, (line, m)
    domain = m.group(1)

    print('127.0.0.1', domain)

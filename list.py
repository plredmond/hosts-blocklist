#!/usr/bin/env python3

import os
import sys

names = {
        'www.google-analytics.com',
        'google-analytics.com',
        'adwords.google.com',
        'amazon-adsystem.com',
        'googletagservices.com',
        }

for line in sys.stdin:

    if not line.strip():
        continue # skip blanks

    if line.strip().startswith('#'):
        continue # skip comments

    addr, dns = line.strip().split()
    assert addr == '0.0.0.0'

    names.add(dns)

for name in sorted(names):
    print('127.0.0.1', name)

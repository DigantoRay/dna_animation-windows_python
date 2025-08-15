#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 23:17:31 2025.

@author: Diganto Ray
"""

import time
import sys
import csv


with open('DNA.csv') as dna_file:
    dna_reader = csv.reader(dna_file)
    dna_strings = list(dna_reader)
    try:
        while True:
            for line in dna_strings:
                print(line[0])
                time.sleep(0.025)

    except KeyboardInterrupt:
        dna_file.close()
        sys.exit()

#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-07-06
# file: exercise_2.25.py
##########################################################################################

import csv
from datetime import datetime

if __name__ == '__main__':

    f = open('Data/dowstocks.csv')
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)

    print(headers)
    print(row)

    types = [str, float, str, str, float, float, float, float, int]
    converted = [func(val) for func, val in zip(types, row)]
    record = dict(zip(headers, converted))

    print(record)
    print(record['name'])
    print(record['price'])
    print(record['date'])

    date_formatter = lambda x: datetime.strptime(x, "%m/%d/%Y").strftime('(%-m, %d, %Y)')
    # Bonus:
    types = [str, float, date_formatter, str, float, float, float, float, int]
    converted = [func(val) for func, val in zip(types, row)]
    record = dict(zip(headers, converted))

    print(record)
    print(record['date'])

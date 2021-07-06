#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-07-06
# file: exercise_2.24.py
##########################################################################################

import csv

if __name__ == '__main__':

    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    print(row)

    types = [str, int, float]

    converted = [func(val) for func, val in zip(types, row)]

    print(converted)

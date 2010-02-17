#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv

def extract_names_from_csv(lines):

    def only_data(string):
        return string.startswith('"')
        
    def entries_in_first_column(lines):
        csv_reader = csv.reader(lines, delimiter='\t')
        return [row[0] for row in csv_reader]
    
    return entries_in_first_column(filter(only_data, lines))


#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv

def extract_names_from_csv(csv_contents):
    lines = csv_contents.split('\n')
    
    def not_empty(string):
        return string
    def not_header(string):
        return string.startswith('"')
    lines_with_data = filter(not_header, filter(not_empty, lines))
    csv_reader = csv.reader(lines_with_data, delimiter='\t')
    entries_in_first_column = [row[0] for row in csv_reader]
    
    all_data_entries = entries_in_first_column
    return all_data_entries


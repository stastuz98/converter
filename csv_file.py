#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json

#csvTOjson

dictionary = []

def read_csv_file(file_name):
    with open(file_name) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dictionary.append(row)
    return dictionary

def toJson(data, file_name):
    with open(file_name, 'w') as jsonFile:  
        jsonFile.write(json.dumps(data,indent=4))

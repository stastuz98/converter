#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json

#csvTOjson

FILE_NAME1 = 'TOjson.json' 
FILE_NAME2 = 'csv_file.csv'

dictionary = []

def read_csv_file(file_name):
    with open(file_name) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dictionary.append(row)
    return dictionary

def toJson(data):
    with open(FILE_NAME1, 'w') as jsonFile:  
        jsonFile.write(json.dumps(data,indent=4))


#toJson(read_csv_file('dict.csv'))
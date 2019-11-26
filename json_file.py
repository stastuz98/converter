import json
import csv

FILE_INPUT = 'TOjson.json' 
FILE_OUTPUT = 'csv_fi.csv'

#jsonTOcsv


def reader_json():
    with open(FILE_INPUT, 'r') as reader:
        my_dictionary = reader.read()
    return my_dictionary
    
def writer_csv(my_list):
    with open(FILE_OUTPUT, 'w', newline='') as file:
        colums = colums_for_fieldnames(my_list)
        writer = csv.DictWriter(file, fieldnames=colums)
        writer.writeheader()
        writer.writerows(my_list)

def colums_for_fieldnames(my_list):
    name_colums =[]
    for key in my_list[0]:
        name_colums.append(key)
    return name_colums

my_list = json.loads(reader_json())
writer_csv(my_list)

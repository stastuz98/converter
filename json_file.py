import json
import csv

FILE_NAME1 = 'csvTOjson.json' 
FILE_NAME2 = 'csv_file.csv'

def reader_json():
    with open(FILE_NAME1, 'r') as f:
        my_dictionary = f.read()
    return my_dictionary

def colums_for_fieldnames(my_list):
    name_colums =[]
    for key in my_list[0]:
        name_colums.append(key)
    return name_colums
    

def writer_csv(my_list):
    with open(FILE_NAME2, 'w', newline='') as file:
        colums = colums_for_fieldnames(my_list)
        writer = csv.DictWriter(file, fieldnames=colums)
        writer.writeheader()
        writer.writerows(my_list)

my_list = json.loads(reader_json())
writer_csv(my_list)

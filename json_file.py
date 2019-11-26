import json
import csv

FILE_NAME1 = 'csvTOjson.json' 
FILE_NAME2 = 'csv_file.csv'

#jsonTOcsv

def reader_json():
    with open(FILE_NAME1, 'r') as reader:
        my_dictionary = reader.read()
    return my_dictionary
    
def writer_csv(my_list):
    with open(FILE_NAME2, 'w', newline='') as file:
        colums = colums_for_fieldnames(my_list)
        writer = csv.DictWriter(file, fieldnames=colums)
        writer.writeheader()
        writer.writerows(my_list)

def colums_for_fieldnames(my_list):
    name_colums =[]
    for key in my_list[0]:
        name_colums.append(key)
    return name_colums

my_list = (reader_json())
print(my_list)
#writer_csv(my_list)

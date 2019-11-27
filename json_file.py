import json
import csv

#jsonTOcsv

def reader_json(file_input):
    with open(file_input, 'r') as reader:
        my_dictionary = reader.read()
    return my_dictionary
    
def writer_csv(file_input, file_output):
    my_list = json.loads(reader_json(file_input))
    with open(file_output, 'w', newline='') as file:
        colums = colums_for_fieldnames(my_list)
        writer = csv.DictWriter(file, fieldnames=colums)
        writer.writeheader()
        writer.writerows(my_list)

def colums_for_fieldnames(my_list):
    name_colums =[]
    for key in my_list[0]:
        name_colums.append(key)
    return name_colums

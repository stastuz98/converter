import re
import json_file
import csv_file

def LenEquals1():
    file_name = input('Hello! Enter the name of the file whose format you want to change\n')
    if re.search(r'.json', file_name):
        json_file.writer_csv(file_name, 'result_file.csv')
    elif re.search(r'.csv', file_name):
        csv_file.toJson(csv_file.read_csv_file(file_name), 'result_file.json') 
    else:
        print('Check the correctness of the entered data')
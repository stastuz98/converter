import re
import argparse
import json_file
import csv_file

def lenMore1():
    parser = argparse.ArgumentParser(description='Converter JsonToCsv and CsvToJson')
    parser.add_argument('-in', '--input', metavar='',required=True, help='Name of the file whose format you want to change')
    parser.add_argument('-out', '--output', metavar='',required=True, help='Result file name')
    args = parser.parse_args()
    if re.search(r'.json', args.input):
        json_file.writer_csv(args.input, args.output)
    elif re.search(r'.csv', args.input):
        csv_file.toJson(csv_file.read_csv_file(args.input), args.output)
    else:
        print('Check the correctness of the entered data!')
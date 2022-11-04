import csv

import json

# Copy to EXCEL from TXT file
import openpyxl

with open(r'paths.json') as d:
    paths = json.load(d)['Unzip'][0]


input_file = (paths['ac_simulationtxt'])
output_file = (paths['ac_simulationexcel'])

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)

wb.save(output_file)

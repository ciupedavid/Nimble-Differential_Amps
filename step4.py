import csv


# Copy to EXCEL from TXT file

input_file = (r"C:\Users\davciupe\Downloads\AC_Simulation.txt")
output_file = (r"C:\Users\davciupe\Downloads\AC_simulation.xlsx")

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)

wb.save(output_file)


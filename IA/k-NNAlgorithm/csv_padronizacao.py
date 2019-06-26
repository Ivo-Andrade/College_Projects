import csv
import random

filename = "dataset_teste.csv"

padronizedFilename = "dataset_teste_padronizado.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

rowsMinValue = []
rowsMaxValue = []

i = 0
while i < len(rows[0]) - 1:
    rowsMinValue.append(-1)
    rowsMaxValue.append(-1)
    i = i + 1

for row in rows[:1]:
    i = 0
    while i < len(row) - 1:
        rowsMinValue[i] = row[i]
        rowsMaxValue[i] = row[i]
        i = i + 1

for row in rows[1:]:
    i = 0
    while i < len(row) - 1:
        if float(row[i]) < float(rowsMinValue[i]):
            rowsMinValue[i] = row[i]
        elif float(row[i]) > float(rowsMaxValue[i]):
            rowsMaxValue[i] = row[i]
        i = i + 1

rowsMeanValue = []

i = 0
while i < len(rowsMinValue):
    rowsMeanValue.append( ( float(rowsMinValue[i]) + float(rowsMaxValue[i]) ) / 2 )
    i = i + 1

for row in rows:
    i = 0
    while i < len(row) - 1:
        row[i] = ( float(row[i]) / float(rowsMeanValue[i]) )
        row[i] = row[i] - 1
        i = i + 1

with open(padronizedFilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for row in rows:
        csvwriter.writerow(row)

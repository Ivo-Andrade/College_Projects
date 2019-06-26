import csv
import random

filename = "dataset_corrigido.csv"

discretizedFilename = "dataset_corrigido_discretizado.csv"

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

rowsIntervalValue = []

i = 0
while i < len(rowsMinValue):
    intervalValue = ( float(rowsMaxValue[i]) - float(rowsMinValue[i]) )
    rowsIntervalValue.append( intervalValue / 6 )
    i = i + 1

intervalClasses = ['A', 'B', 'C', 'D', 'E', 'F']

i = 0
while i < len(rowsMinValue):
    for row in rows:
        x = 0
        while x < 5:
            if float(row[i]) <= ( float(rowsMinValue[i]) + float( (rowsIntervalValue[i]) * (x + 1) ) ):
                row[i] = intervalClasses[x]
                break
            x = x + 1
        if x == 5:
            row[i] = 'F'
    i = i + 1

with open(discretizedFilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for row in rows:
        csvwriter.writerow(row)

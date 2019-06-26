import csv
import random

filename = "dataset_corrigido.csv"

pracFilename = "dataset_treinamento.csv"
testFilename = "dataset_teste.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

rowsBus = []
rowsCar = []
rowsStill = []
rowsTrain = []
rowsWalking = []

for row in rows:
    if row[13] == 'Bus':
        rowsBus.append(row)
    if row[13] == 'Car':
        rowsCar.append(row)
    if row[13] == 'Still':
        rowsStill.append(row)
    if row[13] == 'Train':
        rowsTrain.append(row)
    if row[13] == 'Walking':
        rowsWalking.append(row)

random.shuffle(rowsBus)
random.shuffle(rowsCar)
random.shuffle(rowsStill)
random.shuffle(rowsTrain)
random.shuffle(rowsWalking)

pracRows = []
testRows = []

i = 0
for row in rowsBus:
    if i < 0.7*len(rowsBus):
        pracRows.append(row)
        i = i + 1
    else:
        testRows.append(row)

i = 0
for row in rowsCar:
    if i < 0.7*len(rowsCar):
        pracRows.append(row)
        i = i + 1
    else:
        testRows.append(row)

i = 0
for row in rowsStill:
    if i < 0.7*len(rowsStill):
        pracRows.append(row)
        i = i + 1
    else:
        testRows.append(row)

i = 0
for row in rowsTrain:
    if i < 0.7*len(rowsTrain):
        pracRows.append(row)
        i = i + 1
    else:
        testRows.append(row)

i = 0
for row in rowsWalking:
    if i < 0.7*len(rowsWalking):
        pracRows.append(row)
        i = i + 1
    else:
        testRows.append(row)

random.shuffle(pracRows)
random.shuffle(testRows)

with open(pracFilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for row in pracRows:
        csvwriter.writerow(row)

with open(testFilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for row in testRows:
        csvwriter.writerow(row)

import csv

filename = "dataset_5secondWindow%5B1%5D.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

busCont = 0
carCont = 0
stillCont = 0
trainCont = 0
walkCont = 0

for row in rows:
    if row[13] == 'Bus':
        busCont = busCont + 1
    elif row[13] == 'Car':
        carCont = carCont + 1
    elif row[13] == 'Still':
        stillCont = stillCont + 1
    elif row[13] == 'Train':
        trainCont = trainCont + 1
    elif row[13] == 'Walking':
        walkCont = walkCont + 1

print("Contagem" + '\n')
print("Bus: %d"%(busCont) + '\n')
print("Car: %d"%(carCont) + '\n')
print("Still: %d"%(stillCont) + '\n')
print("Train: %d"%(trainCont) + '\n')
print("Walking: %d"%(walkCont) + '\n')
    
            

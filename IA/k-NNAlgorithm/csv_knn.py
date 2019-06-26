import csv
import math

pracFilename = "dataset_treinamento_padronizado.csv"
testFilename = "dataset_teste_padronizado.csv"

k = 1
klimit = 11
while k < klimit:
    euclidian = 1
    correctGuesses = 0

    fields = []
    rows = []

    with open(pracFilename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    cases = 0

    with open(testFilename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            
            cases = cases + 1
            if cases%100 == 0:
                print("Case %d"%(cases))

            shortestDists = []

            for row2 in rows:

                dist = 0
                i = 0

                if euclidian == 1:
                    while i < len(row) - 1:
                        dist = dist + math.pow(float(row[i]) - float(row2[i]), 2)
                        i = i + 1
                    dist = math.sqrt(dist)
                else:
                    while i < len(row) - 1:
                        dist = dist + math.fabs(float(row[i]) - float(row2[i]))
                        i = i + 1

                shortestDists.append([dist, row2[len(row) - 1]])
                shortestDists.sort()
                if len(shortestDists) > k:
                    del shortestDists[k]

            guessedClass = 'null'
            i = k - 1
            classes = ['Bus', 'Car', 'Still', 'Train', 'Walking']
            
            
            while guessedClass == 'null':

                classFrequency = [ sum(x.count('Bus') for x in shortestDists),
                                   sum(x.count('Car') for x in shortestDists),
                                   sum(x.count('Still') for x in shortestDists),
                                   sum(x.count('Train') for x in shortestDists),
                                   sum(x.count('Walking') for x in shortestDists) ]

                classFrequencySorted = [ sum(x.count('Bus') for x in shortestDists),
                                         sum(x.count('Car') for x in shortestDists),
                                         sum(x.count('Still') for x in shortestDists),
                                         sum(x.count('Train') for x in shortestDists),
                                         sum(x.count('Walking') for x in shortestDists) ]
                classFrequencySorted.sort(reverse=True)
                
                if classFrequencySorted[0] == classFrequencySorted[1]:
                    del shortestDists[i]
                    i = i - 1
                else:
                    elemSorted = classFrequencySorted[0]
                    numIndex = classFrequency.index(elemSorted)
                    guessedClass = classes[numIndex]

            if guessedClass == row[len(row) - 1]:
                correctGuesses = correctGuesses + 1
                
    print("k = %d"%k)
    print("Correct Guesses: %d"%correctGuesses)
    print("Cases: %d"%cases)
    print("Accuracy: %f"%(correctGuesses / cases))
    k = k + 1

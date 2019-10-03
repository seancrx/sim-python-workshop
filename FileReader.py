import io
import csv

fileToOpen = io.open('TotalCitizenYear.csv', 'r', encoding='utf-8-sig')

inputFile = csv.reader(fileToOpen, delimiter=',')

for row in inputFile:
    print(row)
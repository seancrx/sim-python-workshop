import io
import csv

fileToOpen = io.open('TotalCitizenWithHeaders.csv', 'r', encoding='utf-8-sig')

inputFile = csv.reader(fileToOpen, delimiter=',')

for row in inputFile:
    if row[0] == "year" and row[1] == "total" and row[2] == "male" and row[3] == "female":
        print("Header row: ", row)
    elif row[0] == "1970":
        print("This is the first row after header: ", row)
    else:
        print(row)
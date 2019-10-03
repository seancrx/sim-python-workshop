import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io
import csv

totalYear = []
totalLevel = []
residentYear = []
residentLevel = []

file = io.open('LiveBirthYear.csv', 'r', encoding='utf-8-sig')
inputFile = csv.reader(file, delimiter=',')

for row in inputFile:
    if row[0] == "year":
        continue
    elif row[1] == "Total Live-births":
        totalLevel.append(int(row[2]))
        totalYear.append(int(row[0]))
    else:
        if row[2] == "na":
            residentLevel.append(0)
        else:
            residentLevel.append(int(row[2]))
        residentYear.append(int(row[0]))

plt.bar(totalYear, totalLevel, color='g')
plt.bar(residentYear, residentLevel, color='b')
plt.xlabel('year')
plt.ylabel('value')
plt.show()
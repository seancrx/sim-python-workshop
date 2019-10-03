import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io
import csv

totalLevel = []
residentLevel = []

file = io.open('LiveBirthYear.csv', 'r', encoding='utf-8-sig')
inputFile = csv.reader(file, delimiter=',')

for row in inputFile:
    if row[0] == "year":
        continue
    elif row[1] == "Total Live-births":
        totalLevel.append(int(row[2]))
    else:
        if row[2] == "na":
            residentLevel.append(0)
            continue
        residentLevel.append(int(row[2]))

plotArray = [totalLevel, residentLevel]

plt.boxplot(plotArray)
plt.show()
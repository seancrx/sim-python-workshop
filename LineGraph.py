import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import io
import csv

totalYear = []
totalCitizen = []
totalMale = []
totalFemale = []

file = io.open('TotalCitizenYear.csv', 'r', encoding='utf-8-sig')
inputFile = csv.reader(file, delimiter=',')

for row in inputFile:
    if row[0] == "year" and row[1] == "total" and row[2] == "male" and row[3] == "female":
        continue
    else:
        totalYear.append(int(row[0]))
        totalCitizen.append(int(row[1]))
        totalMale.append(int(row[2]))
        totalFemale.append(int(row[3]))

plt.plot(totalYear, totalCitizen, 'g--', totalYear, totalMale, 'b--', totalYear, totalFemale, 'r--')
plt.xlabel('year')
plt.ylabel('value')
plt.title('Total Citizen by Gender and Year')
plt.show()
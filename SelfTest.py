import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io
import csv

value = []
year = []

file = io.open('TotalCitizen.csv', 'r', encoding='utf-8-sig')
inputFile = csv.reader(file, delimiter=',')

for row in inputFile:
    if row[0] == "year":
        continue
    elif row[1] == "Total Female Citizens" and row[2] == "40 - 44 Years":
        value.append(int(row[3]))
        year.append(int(row[0]))

plt.bar(year, value, color='r')
plt.xlabel('year')
plt.ylabel('value')
plt.title('Total Female Citizen Aged 40-44 by Year')
plt.show()
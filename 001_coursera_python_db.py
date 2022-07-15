import pandas as pd
import csv


count = 0
A = list()
B = list()
while True:
    count += 1
    A.append(count)
    if count == 240:
        break
for i in A:
    B.append(i)


with open('list_to_csv.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in B:
        csv_writer.writerow([item])

C = pd.read_csv('list_to_csv.csv', sep=';')

print(C)

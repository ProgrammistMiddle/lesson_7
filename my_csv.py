import csv
from doc import file

f=file
f1=[]
f1.append(list(f.keys()))
f1.append(list(f.values()))
#print(f1)

with open('report.csv','w') as f: #
    writer = csv.writer(f,delimiter = ':')
    writer.writerows(f1)
#print('ok')

with open('report.csv') as f: #
    reader = csv.reader(f,delimiter = ':')
    for row in reader:
        print()

c = list(file.items())
c1 = []
count = 0
for i in c:
    if count==0: count+=1
    else: c1.append({'servis' : i[0], 'cost': i[1]})

fieldnames = ['servis','cost']

with open('report.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames,delimiter = ':')
    writer.writeheader()
    for i in range(len(c1)):
        writer.writerow(c1[i])

with open('report.csv') as f:
    reader = csv.DictReader(f,delimiter = ':')
    for row in reader:
        print(row)

import pandas as pd

DataFrame_from_csv = pd.read_csv('report.csv', sep=':')
print(DataFrame_from_csv)






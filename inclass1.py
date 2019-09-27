#Pengkai Fang  & Juntong Liu

import csv

afile = open('names', 'r')
bfile = open('city', 'r')
cfile = open('age', 'r')
dfile = open('phone', 'r')
efile = open('state', 'r')

a = list()
b = list()
c = list()
d = list()
e = list()

for line in afile:
    a.append(line.rstrip("\n"))
for line in bfile:
    b.append(line.rstrip("\n"))
for line in cfile:
    c.append(line.rstrip("\n"))
for line in dfile:
    d.append(line.rstrip("\n"))
for line in efile:
    e.append(line.rstrip("\n"))

with open('inclass1.csv', 'w') as csvfile:
    fieldnames = ['names', 'city',  'age', 'phone', 'state']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    i = 0
    writer.writeheader()
    for i in range(len(a)):
        writer.writerow({'names': a[i], 'city': b[i], 'age': c[i], 'phone': d[i], 'state': e[i]})

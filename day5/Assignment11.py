l = []
while True:
    d = {}
    l1 = input("Enter ID, Name, Age, Grade separated by space: ").split()
    d['ID'] = l1[0]
    d['Name'] = l1[1]
    d['Age'] = int(l1[2])
    d['Grade'] = (l1[3])
    l.append(d)
    i1=input("press 1  to continue:")
    if i1 == '1':
        continue
    else:
        break

import csv

i2 = input("Enter the name of file in which you want ot save the data: ")

with open(i2,'w', newline='') as csvfile:
    fieldnames = [k for k in l[0].keys()]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for iter in l:
        writer.writerow(iter)


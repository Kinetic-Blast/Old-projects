
'''
Author Baylee Byers
Class:IS-204-QL
'''

import csv
import SupportMod as SM

ElementList = []

readFileName = input("Please enter the name of the file you wish to open: ")

#opens file and add it to the ElementList
with open(readFileName+".txt") as csvfile:
    read = csv.reader(csvfile,delimiter=',')
    for row in read:
        ElementList.append(row)

#for loop to get fuel milage and and print it out
for data in ElementList:
    FuelValue=SM.FuleMileage(data)
    data.append(FuelValue)
    SM.PrintOut(data)

#collects file name
writeFileName = input("Please enter the name of the file you wish to create: ")

#writes out fill name
with open(writeFileName+".txt", 'w', newline='') as file:
    writer = csv.writer(file)

    for data in ElementList:
        writer.writerow(data)

'''
Author Baylee Byers
Class:IS-204-QL
'''

import csv

#storage for list
ElementList = []

#reads in file aand saves it to the list
with open('trips.txt') as csvfile:
    read = csv.reader(csvfile,delimiter=',')
    for row in read:
        ElementList.append(row)

#creates file, outputs data, and saves it to new file
with open('Output.txt', 'w', newline='') as file:
    writer = csv.writer(file)

#for loop to print all values
    for data in ElementList:
        Value = round(float(data[2]) / float(data[1]),2)
        print("Date:", data[0], "Fuel Used:", data[1], "gallons,", "Number of Miles:", data[2], "Fuel Mileage:", Value)

#Saves the values out
        data.append(Value)
        writer.writerow(data)


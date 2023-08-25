'''
Author Baylee Byers
Class:IS-204-QL
'''

import csv

#Values for use with in the program
Items = []
TotalSubCost= 0.0
Count = 0
discount = "0%"

#set out file name
writeFileName = input("Please enter the name of the file you wish to create: ")

print("To Exit/Finish Your Purchase input 'exit' at any time")
while True:
#input for users
    inp1 = input("Item Name: ")
    if inp1 == "exit":break

    inp2 = input("Item Quantity: ")
    if inp2 =="exit":break

    inp3 = input("Item Price: ")
    if inp3 =="exit":break

#adds in the subcost
    subcost = int(inp2)*int(inp3)
    TotalSubCost+= subcost

#adds item to list
    Items.append([inp1,inp2,inp3,subcost])
    temp = Items[Count]
    Count+=1

#outputs the item summary
    print("Item Summary:","Name:",temp[0],"Quantity:",temp[1],"Price:",temp[2],"Sub Total:",temp[3])

    print("---------------------------------------------------")
#asks user if they are done with purchasing
    inp4 = input("Do you have any other Purchases: (y for yes n for No):")
    print(inp4)
    if inp4 == "n":break
    print("---------------------------------------------------")

#sees if discount is required
if(TotalSubCost> 100):
    temp = TotalSubCost *0.1
    TotalSubCost = TotalSubCost - temp
    discount = "10%"

#displays the outputs discount and the subtotal and total cost
print("Subtotal With",discount,"discount:",TotalSubCost)
temp = TotalSubCost *0.08
print("Total at 8% tax: $",TotalSubCost+temp)

#outputs the values
with open(writeFileName + ".txt", 'w', newline='') as file:
    writer = csv.writer(file)

    for data in Items:
        writer.writerow(data)
'''
Author Baylee Byers
Class:IS-204-QL
'''

#required function that edits the order of the name and returns in order desired
def NameSplit(Name):
    temp,temp2 = Name.split(' ',1)
    return temp2+","+temp

#runs the collection on the user input
def collect():
    print("#######################################################################")
    print("Please Enter All Desired Names: (Format: FirstName LastName (separated with a space))")
    print("Once All Names Have been entered use keyword 'exit' in lowercase to exit")
    print("#######################################################################")

    # list for storage
    inputs = []

    #loop that takes user input
    while True:
        Names = input()
        if Names == "exit": #exits the loop
            break

        #calls name split
        Names =NameSplit(Names)
        inputs.append(Names) #adds to the list
        inputs = sorted(inputs, key=lambda x: x.split(",")[0]) #sorts the list by last name

    writeFileName = input("Please enter the name of the file you wish to create: ") #gets file name
    writer = open(writeFileName+".txt", "w")#sets up writer

    #loop that writes out data
    for data in inputs:
        writer.write(data+"\n")

    writer.close()

collect()
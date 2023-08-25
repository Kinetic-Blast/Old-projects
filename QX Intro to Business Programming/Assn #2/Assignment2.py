'''
Author: Baylee Byers
Class: IS-204-QL
'''

# Function Collects the User's Vehicle Details in order of (Make,Model Year, Model, Number of Miles on last Trip and
# Amount of Fuel Used)
def Collect():

# This Sets the Global Variables for reference
    global CarMake
    global CarModelYear
    global CarModel
    global NubOfMiles
    global CarFuelUsed

#Uses python's Input method to collect users information
    CarMake      = input("Please Enter the Car Make: ")
    CarModelYear = input("Please Enter the Model Year: ")
    CarModel     = input("Please Enter the Car Model: ")
    NubOfMiles   = input("Please Enter the Number Of Miles Taken On Your Last Trip: ")
    CarFuelUsed  = input("Please Enter the Amount of Fuel Used In Gallons: ")

#Runs the while loop and collects trip info
def MileCollector():
    global NubOfMiles
    global CarFuelUsed

#next section is a while loop that runs until user inputs n also collects info on the fuel and gas usage
    CheckYN = input("Do you want to account for more trips Y= Yes N= No")
    if CheckYN.capitalize() =="N":
        return
    print("To exit this process Enter 'N' at any time")

    while(True):
        tempNubOfMiles = input("Please Enter the Number Of Miles Taken On Your Trip: ")
        if tempNubOfMiles.capitalize() == "N":
            break
        tempCarFuelUsed = input("Please Enter the Amount of Fuel Used In Gallons: ")
        if tempCarFuelUsed.capitalize() == "N":
            break

# adds up the fuel usage and miles
        NubOfMiles  += tempNubOfMiles
        CarFuelUsed += tempCarFuelUsed

#outputs that info to user when they exit the while loop
    print("___________________________________________________________")
    TempMil = int(NubOfMiles) / int(CarFuelUsed)
    if TempMil < 25:
        print("Number of Miles:",NubOfMiles,"Amount of fuel used:",CarFuelUsed)
        TempMil = str(TempMil) + " Gas Guzzler"

    else:
        TempMil = str(TempMil) + " Fuel Efficient"

    print("Fuel Mileage Achieved For your Trip:",TempMil)

#Runs Collect and prints out the information as well as calculates the average fuel mileage as well as calls MileCollector
def Engine():
    Collect()

    TempMil = int(NubOfMiles) / int(CarFuelUsed)
    if TempMil < 25:
        TempMil = str(TempMil) + " Gas Guzzler"
    else:
        TempMil = str(TempMil) + " Fuel Efficient"


    print("___________________________________________________________")
    print("Car Information: ")
    print("Model Year:",CarModelYear,"Make:",CarMake,"Model:",CarModel,"\n"+"Fuel Mileage Achieved:",TempMil)

    MileCollector()

#This Runs the Program Function engine(): That Runs the rest of the program
Engine()
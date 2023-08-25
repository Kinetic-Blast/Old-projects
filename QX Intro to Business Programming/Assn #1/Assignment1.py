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

#Uses python's Input method to collect users infomation
    CarMake      = input("Please Enter the Car Make: ")
    CarModelYear = input("Please Enter the Model Year: ")
    CarModel     = input("Please Enter the Car Model: ")
    NubOfMiles   = input("Please Enter the Number Of Miles Taken On Your Last Trip: ")
    CarFuelUsed  = input("Please Enter the Amount of Fuel Used In Gallons: ")

#Runs Collect and prints out the infomation as well as calulates the average full mileage
def Engine():
    Collect()
    print("___________________________________________________________")
    print("Car Information: ")
    print("Model Year:",CarModelYear,"Make:",CarMake,"Model:",CarModel,"\n"+"Fuel Mileage Achieved:",int(NubOfMiles)/int(CarFuelUsed))


#This Runs the Program Function engine(): That Runs the rest of the program
Engine()
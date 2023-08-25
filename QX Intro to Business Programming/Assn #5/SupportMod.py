#calculates and returns data
def FuleMileage(TripData):
    Value = round(float(TripData[2]) / float(TripData[1]), 2)
    return Value

#prints out data
def PrintOut(data):
    print("Date:", data[0], "Fuel Used:", data[1], "gallons,",
          "Number of Miles:", data[2], "Fuel Mileage:", data[3])
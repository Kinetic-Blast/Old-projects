'''
Author Baylee Byers
Class:IS-204-QL
'''


import tkinter as tk
from tkinter import *
import csv

#############################################################

root = tk.Tk()
root.title("Project 6")
root.minsize(700, 700)
root.configure(bg = "#283346")

############################################################

#Variables

run = 0
fieName =" "

Fname    = StringVar()
Lname    = StringVar()
NumHours = StringVar()
PayRate  = StringVar()

name = StringVar()
numHours = StringVar()
payRate  = StringVar()
overTime = StringVar()
grossPay = StringVar()

###########################################################

#adds items to page as well as calculates the values
def GrossPay():
    name.set(Fname.get()+","+Lname.get())
    numHours.set(NumHours.get())
    payRate.set("$ "+str(re.findall('\d*\.?\d+',PayRate.get())[0])+" /per hour")

    NubHourTemp = float(re.findall('\d*\.?\d+',NumHours.get())[0])
    payRateTemp = float(re.findall('\d*\.?\d+',PayRate.get())[0])

    if (NubHourTemp> 40):
        temp = NubHourTemp-40

        grossPayTemp = 40 * payRateTemp
        grossPayTemp = grossPayTemp + (temp *(payRateTemp *1.5))

        overTime.set(str(temp) + " hours")
        grossPay.set("$ "+ str(grossPayTemp))

    else:
        grossPayTemp  = NubHourTemp * payRateTemp
        grossPay.set("$ " + str(grossPayTemp))
        overTime.set(str(0.0) + " hours")

#writes to the file and opens the second page
def SaveData():
    global run

    if (run == 0):
        run = 1

        master2 = tk.Toplevel()
        master2.geometry("500x150")
        master2.title("File input")

        Label(master2, text="Input Name of File:").grid(row = 0,pady = 10, padx = 100)
        box5 = Entry(master2, font="Helvetica 18")
        box5.grid(row = 1,pady = 10, padx = 100)


        #kills 2nd window
        def kill():
            global fieName
            fieName = box5.get()

            with open(fieName + ".txt", 'w', newline='') as file:
                    writer = csv.writer(file)

            with open(fieName + ".txt", 'a', newline='') as file:
                writer = csv.writer(file)
                print("ran")
                temp = [Fname.get(), Lname.get(), NumHours.get(), PayRate.get(),
                        re.findall('\d*\.?\d+', grossPay.get())[0]]
                writer.writerow(temp)

            master2.destroy()

        Button(master2, text = "Submit",command=kill).grid(row = 2,padx = 100 )
        master2.mainloop()


#saves out
    with open(fieName+".txt", 'a', newline='') as file:
        writer = csv.writer(file)
        print("ran")
        temp = [Fname.get(),Lname.get(),NumHours.get(),PayRate.get(),re.findall('\d*\.?\d+',grossPay.get())[0]]
        writer.writerow(temp)

#clears boxes
def Clear():
    box1.delete(0,END)
    box2.delete(0, END)
    box3.delete(0, END)
    box4.delete(0, END)

#kills program

def end():
    root.destroy()
###########################################################

#entry boxes and lables
Label(root,text = "First Name:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =0,padx = (25,0),pady =(25,0))
box1=Entry(root,font = "Helvetica 18",textvariable = Fname)
box1.grid(row = 0, column = 1,pady =(25,0))

Label(root,text = "Last Name:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =1,padx = (25,0),pady =(25,0))
box2= Entry(root,font = "Helvetica 18",textvariable = Lname)
box2.grid(row = 1, column = 1,pady =(25,0))

Label(root,text = "Number of Hours:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =2,padx = (20,0),pady =(25,0))
box3= Entry(root,font = "Helvetica 18",textvariable = NumHours)
box3.grid(row = 2, column = 1,pady =(25,0))

Label(root,text = "Pay Per Hour:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =3,padx = (25,0),pady =(25,0))
box4= Entry(root,font = "Helvetica 18",textvariable = PayRate)
box4.grid(row = 3, column = 1,pady =(25,0))

############################################################

#editable lables so you can see data
Label(root,text = "------------------",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =4,padx = (25,0),pady =(25,0))
Label(root,text = ("Name (first,last): "),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =5,padx = (25,0),pady =(10,0))
Label(root,text = ("Number Of Hours: "),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =7,padx = (25,0),pady =(10,0))
Label(root,text = ("Overtime Hours: "),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =8,padx = (25,0),pady =(10,0))
Label(root,text = ("pay rate: "),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =9,padx = (25,0),pady =(10,0))
Label(root,text = ("Gross Pay: "),bg = "#283346", fg = "white",font='Helvetica  12').grid(row =10,padx = (25,0),pady =(10,0))



Label(root,textvariable = name,bg = "#283346", fg = "white",font='Helvetica 12').grid(row =5,column = 1,padx = (25,0),pady =(10,0))
Label(root,textvariable = numHours,bg = "#283346", fg = "white",font='Helvetica 12').grid(row =7,column = 1,padx = (25,0),pady =(10,0))
Label(root,textvariable = overTime,bg = "#283346", fg = "white",font='Helvetica 12').grid(row =8,column = 1,padx = (25,0),pady =(10,0))
Label(root,textvariable = payRate,bg = "#283346", fg = "white",font='Helvetica 12').grid(row =9,column = 1,padx = (25,0),pady =(10,0))
Label(root,textvariable = grossPay,bg = "#283346", fg = "white",font='Helvetica  12').grid(row =10,column = 1,padx = (25,0),pady =(10,0))

#############################################################

#buttons
Button(root,text = "Gross Pay",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold', command = GrossPay).grid(row = 11,padx = (0,0),pady =(25,0))
Button(root,text = " Save User ",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold', command = SaveData).grid(row =11,column =1 ,padx = (0,0),pady =(25,0))
Button(root,text = "    Clear    ",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold', command = Clear).grid(row = 12,padx = (0,0),pady =(25,0))
Button(root,text = "  Save File ",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold',command = end).grid(row = 12,column = 1,padx = (0,0),pady =(25,0))

##############################################################

root.mainloop()
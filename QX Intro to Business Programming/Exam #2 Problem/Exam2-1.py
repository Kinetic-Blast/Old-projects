'''
Author Baylee Byers
Class:IS-204-QL
'''

#imports
import tkinter as tk
from tkinter import *
import csv
import Exam2Module as Ex2

################################################################
#Variables

root = tk.Tk()
root.title("Exam2 Program")
root.minsize(700, 400)
root.configure(bg = "#283346")

#################################################################
#Variables

Name    = StringVar()
Quantity    = StringVar()
Price = StringVar()

run = 0
fieName =""

Receipt = Ex2.SalesReceipt()

#################################################################
#funtions for clearing and making a save file

def Clear():
    box1.delete(0,END)
    box2.delete(0, END)
    box3.delete(0, END)



def MakeSaveFile():
    global run

    if (run == 0):
        run = 1

        master2 = tk.Toplevel()
        master2.geometry("500x150")
        master2.title("File input")

        Label(master2, text="Input Name of File:").grid(row=0, pady=10, padx=100)
        box5 = Entry(master2, font="Helvetica 18")
        box5.grid(row=1, pady=10, padx=100)


        def kill():
            global fieName
            fieName = box5.get()

            with open(fieName + ".txt", 'w', newline='') as file:
                    writer = csv.writer(file)

            master2.destroy()

        Button(master2, text="Submit",command = kill).grid(row=2, padx=100)
        master2.mainloop()

#################################################################
#entry boxes and lables

Label(root,text = "Item Name:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =0,padx = (25,0),pady =(25,0))
box1=Entry(root,font = "Helvetica 18",textvariable = Name)
box1.grid(row = 0, column = 1,pady =(25,0))

Label(root,text = "Item Quantity:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =1,padx = (25,0),pady =(25,0))
box2= Entry(root,font = "Helvetica 18",textvariable = Quantity)
box2.grid(row = 1, column = 1,pady =(25,0))

Label(root,text = "Item Price:",bg = "#283346", fg = "white",font='Helvetica 18 bold').grid(row =2,padx = (20,0),pady =(25,0))
box3= Entry(root,font = "Helvetica 18",textvariable = Price)
box3.grid(row = 2, column = 1,pady =(25,0))

#################################################################
Label(root,text = ("=========================="),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =4,padx = (25,0),pady =(10,0))
Label(root,text = ("Only Buttons I got working"),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =5,padx = (25,0),pady =(10,0))
Label(root,text = ("=========================="),bg = "#283346", fg = "white",font='Helvetica 12').grid(row =6,padx = (25,0),pady =(10,0))
#################################################################

#buttons
Button(root,text = "Make Save File",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold', command = MakeSaveFile).grid(row = 11,padx = (0,0),pady =(25,0))
Button(root,text = "    Clear     ",bg = "#72bcd4", fg = "white",font='Helvetica 18 bold', command = Clear).grid(row = 12,padx = (0,0),pady =(25,0))

root.mainloop()
def get_info():
    a = input("Enter your College Name :")
    return a


print("\n~\n~\n~\nYour college name is --->",get_info(),"\n")

# Write a Python program that will calculate area and circumference of circle using
# inbuilt Math Module

import math

def cicleParams():
    rad = int(input("Enter radiuous length : "))

    area = math.pi * rad **2
    
    circf = 2 * math.pi * rad
    
    print("\n\tArea of the circle is :->",math.floor(area),"\n\n\tThe circumfarance of Circle is :->",math.floor(circf),"\n")

cicleParams()

# Write a Python program that will display Calendar of given month using Calendar
# Module

import calendar

def showCal():

    mm = int(input("Enter the month of calender : "))
    yy = int(input("Enter the year of calendar : "))
    print("\n\n",calendar.month(yy,mm),"\n")

showCal()


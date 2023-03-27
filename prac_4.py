# # Write a program to check whether a number is even or odd

# a = int(input("Enter the number to check even or odd\n"))

# if a % 2 == 0:
#     print("Number is Even\n")
# else :
#     print("Number is Odd\n")
    
# # Write a program to find out absolute value of an input number

# b = int(input("Enter a number to find its absolute value\n"))

# if b * -1 != b:
#     print(f"Absolute Value of {b} is : {b*-1}")
# elif b ==0 :
#     print("Zero is not valid\n")
# else:
#     print("Number is already absolute\n")
    
# # Write a program to check the largest number among the three numbers

# num1 = int(input("Enter Number 1 :"))
# num2 = int(input("Enter Number 2 :"))
# num3 = int(input("Enter Number 3 :"))

# if num1 > num2 and num1 > num3:
#     print(f"First input {num1} is the Largest Number")
# elif num2 >num1 and num2 > num3:
#     print(f"Second input {num2} Is largest number")
# else:
#     print(f"Third number {num3} is larges number")
    
# # # Write a program to check if the input year is a leap year of not

# year = int(input("Enter a year to check , is it a leap year : "))

# if year%400 ==0 and year % 100 ==0:
#     print("\n%d is a leap year"%year)
# elif year % 4 ==0:
#     print("\n%d is a leap year" % year)
# else:
#     print(f"\n{year} is not a leap year")
    
# # Write a program to check if a Number is Positive, Negative or Zero

# ipt = int(input("\nEnter a number to check whether it's positive , negative or zero : "))

# if ipt > 0 :
#     print("\n%d is a Positive Number" % ipt)
# elif ipt ==0 :
#     print("\nInput Number is a Zero  ")
# else :
#     print("\n%d is a Negative number" % ipt)

# # Write a program that takes the marks of 5 subjects and displays the grade.
sum =0
for i in range(0,5):
    marks = float(input("Enter Subject%d  Marks :"%i))
    sum+=marks

avg = (sum/500.0)  * 100.0
print("\nYour percentage is :",avg)
# Create a class Employee with data members: name, department and salary. Create
# suitable methods for reading and printing employee information

# class Employee:
 
#     def getInfo(self):
#         a = input("Enter your name :")
#         b = input("Enter your department :")
#         c = int(input("Enter your salary :"))
        
#         print("\n\nMR.",a,"\nyour Department is : ",b,"\nWith Salary is : ",c,"\n")
        
# obj = Employee()
# obj.getInfo()

# # Python program to read and print students information using two classes using
# # simple inheritance.

# class g1:

#     def __init__(self):
#         ba= input("Enter your name :")
#         bb = input("Enter your stream :")
#         bc = input("Enter your roll number :")
        
#         print("\n\nName :",ba,"\tStream :",bb,"\tRoll no. :",bc,"\n")
        
# class g2(g1):
#     print()
   
    
# obj = g2()

# Write a Python program to implement multiple inheritance

class base1:
    a ="This is first super class"

class base2:
    b ="This is second super class"
    
    
    
class c(base1,base2):
    def info(self):
        print("This is a multiple inherited class")
        

ob = c()
print(ob.a)
print(ob.b)
ob.info()
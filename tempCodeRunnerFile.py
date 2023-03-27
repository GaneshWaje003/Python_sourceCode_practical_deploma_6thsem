Write a Python program to create a class to print an integer and a character with
# two methods having the same name but different sequence of the integer and the
# character parameters. For example, if the parameters of the first method are of the
# form (int n, char c), then that of the second method will be of the form (char c, int n)
# """

# # class getInfo:
    
# #     def getdata(delf,c:int,g:str):
# #         print("First parameter :",c," , second parameter:",g)
        
# #     def getdata(self,g:str,c:int):
# #         print("First parameter :",c," ,second parameter :",g)

        
# # c = getInfo()

# # c.getdata(6,"newthings")


# # c.getdata("wll",2)

        
# """
# Write a Python program to create a class to print the area of a square and a
# rectangle. The class has two methods with the same name but different number of
# parameters. The method for printing area of rectangle has two parameters which
# are length and breadth respectively while the other method for printing area of
# square has one parameter which is side of square
# """


# class getSizes:

#     def getArea(self,l:int,b:int):
#         a = l*b
#         print("Area of the rectangle is :",a)
  
#     def getArea(self,s:int):
#         a = s**2
#         print("The Area of Square is :",a)
        

# obj = getSizes()

# obj.getArea(10)
# obj.getArea(4,8)
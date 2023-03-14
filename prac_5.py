# Write a Python program to print all even numbers between 1 to 100 using while loop.

print("\nEven Numbers between 1 t0 101 are :--- \n")
i =0
 
while i<=100:
    if i % 2 == 0:
        print(i,end=",")
        i+=1
    else :
        i+=1
        
# Write a Python program to find the sum of first 10 natural numbers using for loop
sum =0
for i in range(0,11):
    sum += i

print("Sum of First 10 Natural Numbers is ",sum) 

# Write a Python program to print Fibonacci series

i = int(input('Enter last number of fibonacci last :'))

pvar = 0
cvar = 1
temp = 0

print("\nFibonacci series at end ",i,"is : ")
for j in range(0,i):
   temp = pvar 
   pvar = cvar 
   cvar += temp  
   print(cvar, end = " ")
   
# # Write a Python program to calculate factorial of a number

num = int(input("Enter Number to which find factorial :"))
sum =0

while num > 0 :
    print(num,end="*")
    sum +=num
    num -=1
    
print("\n\nFactorial of given Number is : ",sum)

# Write a Python Program to Reverse a Given Number

rev = input("Enter a number \n")
s = len(rev)-1

print("\nReversed Number is :")
for i in range(s,-1,-1):
    print(rev[i],end="")

# Write a Python program takes in a number and finds the sum of digits in a
# number

a = input("\nEnter number to find some its individual ones :")
sum =0

for i in a:
    sum += int(i)
    
print(sum)

# Write a Python program that takes a number and checks whether it is a palindrome
# or not.
    
rev = input("Enter a number \n")
s = len(rev)-1
str =""

for i in range(s,-1,-1):
    str += rev[i]

if rev == str:
    print("\nThe Given number %s is palindrome number "% str)
else :
    print("Number is not a palindrome")

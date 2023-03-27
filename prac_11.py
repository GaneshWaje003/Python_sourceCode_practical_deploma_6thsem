# Write a Python function that takes a number as a parameter and check the number is
# prime or not.\
    
def sPrime(d):
    if d%2 != 0 and d % 3 !=0:
        print("\n",d,"Is a Prime Number\n")
    else :
        print("\n",d,"\nIs not a prime number\n")

# sPrime(11)

# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def findFact(r):
    ft = 0
    st = 1
    temp =0
    
    for i in range(0,r):
        temp = st
        st = ft + st
        ft = temp
        print(st,end=" ")
        
# findFact(5)

# Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.


def findUpandlow(s):
    
    low =0
    upp =0
    
    for i in s:
        if i.isupper():
            upp+=1
        else :
            low+=1
            
    print("\n The upper cases charcters in string are : ",upp)
    print("\n The lower cases charcters in string are : ",low,"\n")

d = "newthingS"
findUpandlow(d)
    

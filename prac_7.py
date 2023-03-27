# Create a tuple and find the minimum and maximum number from it
tup = (12,32,4,65,3,89,12)
min = tup[0]
max = 0

for i in tup:
    if i > max:
        max = i
    elif i < min:
        min = i
    else : continue 
print("Original Tuple is ",tup,"\n")
print("Max element is :",max,"Mininmum element is: ",min)

# Write a Python program to find the repeated items of a tuple.

new_1 = (1,2,3,45,3,2,12,65,90)
_size = len(new_1)

lis =[]
for x in range(_size):
    k = x +1
    for y in range(k,_size):
        if new_1[x] == new_1[y] and new_1[y] not in lis:
            lis.append(new_1[y])         

print("Original Tuple is",new_1,"\n")

print("Duplicate Number in tuple is :")
print(tuple(lis))            
    

# print the number in words for Example: 1234 => One Two Three Four  
num = 1234
rev =0
print("Integer is :%d\n"%num)
print("The Integers to String values are : \n")

while num > 0 :
    rem = num % 10 
    rev = rev*10 + rem
    num = int(num/10)
    if rem==0:
        print("Zero",end=" ")
    elif rem == 1:
        print("One",end=" ")
    elif rem == 2:
        print("Two",end=" ")
    elif rem == 3:
        print("Three",end=" ")
    elif rem == 4:
        print("Four",end=" ")
    elif rem == 5:
        print("Five",end=" ")
    elif rem == 6:
        print("six",end=" ")
    elif rem == 7:
        print("Seven",end=" ")
    elif rem == 8:
        print("Eight",end=" ")
    elif rem ==9:
        print("Nine",end=" ")   
    
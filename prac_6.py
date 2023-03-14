# Write a Python program to sum all the items in a list.
list = [234,1,2,323,12,88]

sum =0
for x in list:
    sum +=x 

print("\nThe Sum of all list elements is :",sum)


# Write a Python program to multiplies all the items in a list.

list = [34,10,2,23,12,8]

mul =1
for x in list:
    mul *=x 

print("\nThe Multiplication of list elements is :",mul)


# Write a Python program to get the largest number from a list.

list = [23,12,3,4,54]
lar =0
for x in list:
    if x > lar:
        lar =x

print("\nThe largest element from list is",lar)


# Write a Python program to get the smallest number from a list.

list = [23,12,3,4,54]
small =0
for x in list:
    if x < lar:
        small =x

print("\nThe smallest number from list is :",small)

# Write a Python program to reverse a list

list = [12,3,223,12,4]
leng = len(list)-1
print("\nThe reverse list is:")

for x in range(0,leng):
    print(list[leng],end=",")
    leng -=1


# Write a Python program to find common items from two lists.

list_a = [12,3,21,56,75]
list_b = [23,3,21,34,89]
list_c = []
c=0

def findunion():
    for x in list_a:
        for y in list_b:
            if x == y:
                list_c.append(y)
            else:
                continue
                
    print("\n\nThe same elements in the list is :",list_c , sep=",") 

findunion()

# Write a Python program to select the even items of a list.

print("\nEven no. are:")
list = [12,32,45,22,89]
for x in list:
    if x%2==0:
        print(x,end=",")


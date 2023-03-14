# Create a tuple and find the minimum and maximum number from it
# tup = (12,32,4,65,3,89,12)
# min = tup[0]
# max = 0

# for i in tup:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
#     else : continue 
    
# print("Max element is :",max,"Mininmum element is: ",min)

# Write a Python program to find the repeated items of a tuple.

tup = (12,32,4,65,3,89,12,3,56,12)
new_tup = list(tup)
tr =  new_tup

for x in new_tup:
    for y in new_tup:
        print(x,y)
        if x == y:
            tr.remove(y)

print(new_tup)
            
            


# print the number in words for Example: 1234 => One Two Three Four  
num = 1234
p = 0

# for i in range(0,len(num)):
    

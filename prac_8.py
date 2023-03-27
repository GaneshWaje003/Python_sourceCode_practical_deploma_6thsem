# Write a Python program to create a set, add member(s) in a set and remove one
# item from set

print("Creating a set ")
seta = {1,2,3,4}
print(seta)
print("\nAdding element s in set")
seta.add("s")
print(seta)

print("\nRemoving the element 2 from set")
seta.remove(2)
print(seta)

# Write a Python program to perform following operations on set: intersection of
# sets, union of sets, set difference, symmetric difference, clear a set

s = {1,2,3,5,7}
t ={8,9,3,2,0}

lis =[]
un = s.copy()
diff = s.copy()
sem_diff = set()

for x in s:
    for y in t:
        if x ==y :
            lis.append(y)
            diff.remove(y) 
        if x != y:
            un.add(y) 
        if x in s and x not in t and y in t and y not in s:
            sem_diff.add(x)
            sem_diff.add(y)

print("Set s :",s)
print("Set t :",t)              

            
print("\nIntersection in set s and t : ",lis)
print("union of set s and t          :",un)
print("differnce of set s and t      :",diff)
print("semetric diff of set s and t  :",sem_diff,"\n")

s.clear()
print("deleting set s :",s)


# Write a Python program to find maximum and the minimum value in a set.
seta = {12,34,435,90,0,44,54,15}
max =0
min = 1

for x in seta:
    if x > max:
        max =x
    if x < min:
        min = x
print("set is : ",seta,"\n")
print("Maxmimum number from set is :",max)
print("Minimum  number from set is :",min)

# Write a Python program to find the length of a set.
seta = {12,34,435,90,0,44,54,15}

count =0
for x in seta:
    count+=1
print("set is : ",seta,"\n")  
print("Length of set is : ",count-1)
# Write a Python script to sort (ascending and descending) a dictionary by value.

dict = {'g':1,'s':4,'i':0,'e':2}
con = 0
res = {}
a_new = list(dict.values());


for x in range(0,len(a_new)-1):
    if a_new[x] > a_new[x+1]:
        con = a_new[x+1]
        a_new[x+1] = a_new[x]
        res[a_new[x+1]]
        a_new[x] = con
      
    
print(a_new)
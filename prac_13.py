# Write a Python program to create two matrices and perform addition, subtraction,
# multiplication and division operation on matrix.x``

import numpy as np
a = np.array([[1,2,3],[3,4,5],[5,71,2]])
b = np.array([[2,4,3],[9,8,6],[6,2,7]])

print("Addition of matrices is :\n",np.add(a,b))

print("Subraction of matrices is :\n",np.subtract(a,b))

print("Multiplication of matrices is : \n",np.multiply(a,b))

print("Division of martrices is :\n",np.divide(a,b))


#concanetate the strings in python

import numpy as np
def numconcat():
    print(np.char.add([' hello ','welcoming'],['friends','codemania']))
    
# generate six random numbers using pandas

import numpy as np

def getRandom():
    ran = np.random.randint(low=1,high=10,size=6)
    print(ran)

getRandom()\
    
import prac_14 as p

p.getSizes(12)
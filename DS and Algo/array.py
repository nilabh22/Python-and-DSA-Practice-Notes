# Array Traversal - Its like iteration
from array import *
arr1 = array('i',[1,2,3,4,5,6])
print(arr1)
# Accesing an elemnt in array
def elmntacess(array,index):
    if index>len(array):
        print("No element at this index")
    else:
        return array[index]
print(elmntacess(arr1,2))

# Searching an elemnent in array
# Linear search
# Binary search - if data is sorted
def search(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element does not exist in array"
print(search(arr1,6))

# Deleting an element from array
arr1.remove(4) # to remove specific elemnt
# print(arr1)
arr1.pop() # To remove last elent
print(arr1)

# 16 questions related to 1D array in VSCODE folder

# Creating a 2D  array
#Time complexity - O(1)
# Space complexity - O(mn), m- no of rows, n - no. of columns
import numpy as np
twoDarray= np.array([[10,11,12,13],[20,21,22,23],[30,31,32,33],[40,41,42,43]])
print(twoDarray)

# inserting in 2D array

newtwoDarray= np.insert(twoDarray,1,[1,2,3,4],axis=1) # axis 1 for column, axis 0 for rows
print(newtwoDarray)

# if u want to add in last position - append

# Traversing through a 2D array - Printing all elements in a 2d array
# Time complexity - O(mn) where m= no. of rows, n= no. of columns
# if m =n , then quadratic time complexity
# O(1) is space complexity
def traverse(array):
    for i in range(len(array)): # len(array) will traverse through rows
        for j in range(len(array[0])): # len(array[0]) will traverse through columns
            print(array[i][j])
traverse(twoDarray)

# Searching an element in an 2d array\
# Here we are using linear search
# Time and space compplexity is O(mn) and O(1) respectively

def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== value:
                print("Searching...")
                return f"The value is found at index {[i]}{[j]}"
    else:
        return "The value is not found"
print(search(twoDarray,33))

# Deletion in 2D array
# Time and space complexity are O(mn) and O(1) respectively
print(newtwoDarray)
newTDarray = np.delete(newtwoDarray, 0, axis=0) # axis 0 for rows and axis 1 for columns
print(newTDarray)
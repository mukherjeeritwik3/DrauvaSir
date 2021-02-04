"""
Given two matrix the task is that we will have to create a program to multiply two matrices in python.

Examples:

Input : X = [[1, 7, 3],
             [3, 5, 6],
             [6, 8, 9]]
       Y = [[1, 1, 1, 2],
           [6, 7, 3, 0],
           [4, 5, 9, 1]]

Output : [55, 65, 49, 5]
         [57, 68, 72, 12]
         [90, 107, 111, 21]
"""



# take a 3x3 matrix
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k]*B[k][j]
print(result)


"""
# Using Numpy Method

import numpy as np
A = [[12, 7, 3], 
    [4, 5, 6], 
    [7, 8, 9]]

B = [[5, 8, 1, 2], 
    [6, 7, 3, 0], 
    [4, 5, 9, 1]] 

result= [[0,0,0,0], 
        [0,0,0,0], 
        [0,0,0,0]] 

result = np.dot(A,B)
print(result)
"""